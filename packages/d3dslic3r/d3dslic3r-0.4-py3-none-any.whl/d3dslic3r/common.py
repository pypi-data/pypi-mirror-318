#!/usr/bin/env python
'''
Functions and methods that are common to d3dslic3r calculation routines
'''

__author__ = "M.J. Roy"
__version__ = "0.4"
__email__ = "matthew.roy@manchester.ac.uk"
__status__ = "Experimental"
__copyright__ = "(c) M. J. Roy, 2024--"

import numpy as np
import vtk
from scipy.spatial.distance import cdist
from scipy.spatial import Delaunay
from vtk.util.numpy_support import vtk_to_numpy as v2n
from vtk.util.numpy_support import numpy_to_vtk as n2v
from shapely.ops import unary_union, polygonize
from pyclipper import PyclipperOffset, scale_to_clipper, scale_from_clipper, JT_SQUARE, ET_CLOSEDPOLYGON
from scipy.interpolate import interp1d
from shapely.geometry import LineString, Polygon

def get_slice_data(inp_polydata,param,num_slices = True):
    """
    Obtains x,y pairs corresponding to a vtkCutter operation on input polydata 
    Params:
    polydata is a vtkPolydata object to be sliced
    param is either the number of slices or height of each slice
    num_slices sets slicing on number of total slices (True, default)
    Returns:
    slices: list of numpy arrays to grouped loops from the polydata entries
    break_point_indices: list of paired loop break points
    slice_actor_collection: vtkAssembly of slices for display
    TO DO: improve enumeration of parent/child slice determination
    """
    #make sure that incoming polydata isn't connected to anything
    polydata = vtk.vtkPolyData()
    polydata.DeepCopy(inp_polydata)
    #suppress output from the vtk logger
    vtk.vtkLogger.SetStderrVerbosity(vtk.vtkLogger.VERBOSITY_OFF)
    
    bbox = polydata.GetBounds()
    xy_origin = [(bbox[1] + bbox[0]) / 2.0,
                    (bbox[3] + bbox[2]) / 2.0]
    #Assumes polydata starts at 0.001 above minimum z value of the bounding box, and the first slice is the 'footprint' of the polydata. Additional value is to avoid the last 'slice' consistent with the upper boundary.
    if num_slices:
        z_vals = np.linspace(bbox[4]+0.01,bbox[5],param+1)[0:-1]
    else:
        # z_vals based on fixed height of each layer
        num_z_vals = int(np.floor((bbox[5] - bbox[4]+0.001)/param))
        z_vals = np.linspace(bbox[4]+0.001,bbox[5],num_z_vals+1)[0:-1]
    
    slice_actor_collection = vtk.vtkAssembly()
    slices = []
    break_point_indices = []
    for z in z_vals:
        loop_list = []
        plane = vtk.vtkPlane()
        plane.SetNormal(0, 0, 1)
        plane.SetOrigin(xy_origin[0], xy_origin[1], z)
        
        cutter = vtk.vtkCutter()
        cutter.SetCutFunction(plane)
        cutter.SetInputData(polydata)
        cutter.Update()
        
        #create loop extractor
        loops_extract = vtk.vtkContourLoopExtraction()
        #make sure loops are closed
        loops_extract.SetOutputModeToPolylines()
        #remove any duplicates etc.
        loops_extract.CleanPointsOn()
        loops_extract.SetInputData(cutter.GetOutput())
        loops_extract.Update()
        
        #get output from loop extractor
        output = loops_extract.GetOutput()
        loop_points = output.GetPoints().GetData()
        loops = output.GetLines().GetData()
        num_loops = output.GetLines().GetNumberOfCells()
        
        #acquire discrete loops from loop extractor. index references the specific loop in each slice
        index = 0
        for i in range(num_loops):
            #poly_point_count is the number of points that comprise each loop
            poly_point_count = np.asarray(loops)[index]
            #generate local index of points that comprise each loop
            poly_point_ind = np.asarray(loops)[index + 1:index + 1 + poly_point_count]
            #push to slices
            loop_list.append(np.asarray(loop_points)[poly_point_ind,:])
            index += poly_point_count + 1
            
        #add to overall slice data
        slices.append(loop_list)
        break_point_indices.append([])
        # Create a mapper and actor for visualization
        cutter_mapper = vtk.vtkPolyDataMapper()
        cutter_mapper.SetInputConnection(cutter.GetOutputPort())

        actor = vtk.vtkActor()
        actor.GetProperty().SetColor(vtk.vtkNamedColors().GetColor3d('LightSteelBlue'))
        actor.GetProperty().SetLineWidth(2)
        actor.SetMapper(cutter_mapper)
        slice_actor_collection.AddPart(actor)
    
    #now check for encompassed outlines on each slice
    #for each slice, check if there are loops that are inside of other loops recursively.
    break_point_indices = [[] for s in slices] #pre-allocate
    k = 0
    for s in slices:
        #if there's only one loop, then it's a parent
        if len(s) == 1:
            k+=1 #maintain count through slices, but skip the rest
            continue

        #otherwise, make truth table of parent and children loops
        outer = np.full((len(s), len(s)), False, dtype=bool)
        for i in range(len(s)):
            for j in range(len(s)):
                outer[i,j] = Polygon(s[i]).contains(Polygon(s[j]))
                
        #if the diagonal of the truth table is identity, then all loops are parents, otherwise:
        if not np.array_equal(np.diag([True for i in range(len(outer))]), outer):
            collection = np.vstack((np.sum(outer, axis=0),np.sum(outer, axis=1)))
            
            ind = np.lexsort((collection[1,:],collection[0,:])) #sort by parent, then by child
            collection = collection[:,ind]
            #re-index the list of local loops
            local_slice = [s[ind[i]] for i in range(len(ind))]
            
            intervals = sum(1- n % 2 for n in collection[0,:]) -1
            
            even_values = [x for x in list(set(collection[0,:])) if x % 2 == 0] #removing duplicates, how many intervals there are
            last_even = []
            first_even = []
            for value in even_values:
                first_even.append(min(loc for loc, val in enumerate(collection[0,:]) if val == value))
                last_even.append(max(loc for loc, val in enumerate(collection[0,:]) if val == value))
                
            #interval 0 is zero to the last of the next even numbers
            #interval n is the last of the next odd numbers to the last of the even numbers
            #concatenate entries of local_slice from the first_even -1 to the last_even
            concat_slice = []
            concat_ind = []
            for i in range(len(even_values)):
                # print('catenating ',(first_even[i]-1), 'to', last_even[i]) #debug, stop val is -1
                list_to_pad = local_slice[(first_even[i]-1):last_even[i]+1]
                end_ind = [len(arr) for arr in list_to_pad[:-1]] #exclude the last entry in list_to_pad
                # head = list(chain(*[(arr, pad) for arr in list_to_pad[:-1]])) #DEPRECATED create list with 'pad' between entries
                concat_slice.append(np.concatenate(list_to_pad)) #concatenate all elements
                concat_ind.append(end_ind)
            #indices of loops that have been removed:
            removed_ind = []
            for i in range(len(even_values)):
                for j in range((first_even[i]-1),last_even[i]+1):
                    removed_ind.append(j)
            #remove loops that have been concatenated
            local_slice = [i for j, i in enumerate(local_slice) if j not in removed_ind]
            #add remainder
            concat_slice = concat_slice + local_slice
            concat_ind = concat_ind + [[] for entry in local_slice]
            slices[k] = concat_slice
            break_point_indices[k] = concat_ind

        k+=1
    return slices, break_point_indices, slice_actor_collection


def get_polydata_from_stl(fname):
    """
    Load the given STL file, and return a vtkPolyData object from it.
    Params:
    fname the filename of the stl file
    Returns: 
    vtkPolydata object for processing/rendering
    """
    
    reader = vtk.vtkSTLReader()
    reader.SetFileName(fname)
    reader.Update()
    
    polydata = reader.GetOutput()

    return polydata


def actor_from_polydata(polydata):
    """
    Wrap the provided vtkPolyData object in a mapper and an actor, returning
    the actor.
    """
    
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(polydata)

    stl_actor = vtk.vtkActor()
    stl_actor.SetMapper(mapper)

    stl_actor.GetProperty().SetColor(vtk.vtkNamedColors().GetColor3d('PowderBlue'))

    return stl_actor

def sort_ccw(inp):
    """
    Sorts in 2D x,y pairs according to ccw position from the centroid.
    Params:
    inp is a numpy array of shape (N, 3) corresponding to 3D points with uniform z values
    Returns:
    Points are sorted ccw based on angular position. Points with the same angular position are subsequently sorted such that shortest distance from the centroid come first. Ensures that the polygon is closed, such that the first point is the last point.
    """
    
    points = inp[:,0:2]
    # Get centroid/centre of mass
    cent = np.reshape(np.mean(points, axis=0), (-1, 2))
    
    # Compute angles
    angles = np.arctan2((points-cent)[:, 1], (points-cent)[:, 0])

    # Calculate distances from centroid to point
    dist = cdist(points,cent)
    dist = np.reshape(dist,(-1,1))
    
    # Transform angles from [-pi,pi] -> [0, 2*pi]
    angles[angles < 0] = angles[angles < 0] + 2 * np.pi
    angles = np.reshape(angles,(-1,1))

    # Stack angles and dist together for sorting
    c = np.hstack((angles,dist))
    
    # Sort with angles as the first criteria, distance the second: if the same angle is found then the shortest distance should come first
    ind = np.lexsort((c[:,1],c[:,0]))
    B = inp[ind]
    return np.vstack((B, B[0,:]))

def check_self_intersecting(contour_points):
    """
    Check if a given contour is self-intersecting.
    
    Params:
    contour_points: A sequence of (x, y, [,z]) numeric coordinate pairs or triples, or an array-like with shape (N, 2) or (N, 3). Also can be a sequence of Point objects.

    Returns:
    bool: True if the contour is self-intersecting
    """
    line = LineString(contour_points)
    return not line.is_simple

def sort_alpha(inp, alpha = 1):
    """
    Triangulates incoming points and performs an alpha-shape sort suited for outlines that have concave features.
    Params:
        inp is a numpy array of shape (N, 3) corresponding to 3D points with uniform z values
        sp is the semiperimeter cutoff corresponding to the alpha shape to be used. The higher this value, the more points will remain.
    Returns:
        Ordered, closed polygon with the last point equal to the first point
    """
    points = inp[:,0:2]
    zval = np.mean(inp[:,-1])
    tri = Delaunay(points)
    
    coords = points.copy()
    
    triangles = coords[tri.simplices]
    a = ((triangles[:,0,0] - triangles[:,1,0]) ** 2 + (triangles[:,0,1] - triangles[:,1,1]) ** 2) ** 0.5
    b = ((triangles[:,1,0] - triangles[:,2,0]) ** 2 + (triangles[:,1,1] - triangles[:,2,1]) ** 2) ** 0.5
    c = ((triangles[:,2,0] - triangles[:,0,0]) ** 2 + (triangles[:,2,1] - triangles[:,0,1]) ** 2) ** 0.5
    s = ( a + b + c ) / 2.0 #semiperimeter
    areas = (s*(s-a)*(s-b)*(s-c)) ** 0.5 #Heron's formula
    triangles = coords[tri.simplices]
    
    #make sure the areas are valid
    valid = np.isreal(areas) & ~np.isnan(areas) & ~np.isinf(areas)

    np.seterr(divide='ignore', invalid='ignore')
    co = a[valid] * b[valid] * c[valid] / (4.0 * areas[valid]) #circumradius
    np.seterr(divide='warn', invalid='warn')
    
    cutoff = np.mean(co[np.isreal(co) & ~np.isnan(co) & ~np.isinf(co)])
    filtered = triangles[valid][co < (alpha*cutoff)] #as opposed to the published 1 / alpha

    edge1 = filtered[:,(0,1)]
    edge2 = filtered[:,(1,2)]
    edge3 = filtered[:,(2,0)]
    edge_points = np.unique(np.concatenate((edge1,edge2,edge3)), axis = 0).tolist()
    m = geometry.MultiLineString(edge_points)
    triangles = list(polygonize(m))
    chull = unary_union(triangles)
    try:
        x,y = chull.exterior.coords.xy
        outline = np.column_stack((x,y,np.ones(len(x))*zval)) #return outline appearing at z=0
        return outline
    except:
        #if chull doesn't have the exterior attribute (alpha was too small)
        return None

def do_transform(points, T):
    '''
    Applies 4x4 transformation matrix to points and returns the result
    @Param - points, Nx3 matrix of points; T - 4x4 homologous matrix
    '''
    X = points.copy()
    X = X.transpose()
    X = np.append(X, np.ones((1, X.shape[1])), axis=0) #pad with 1's
    X = T @ X #apply by matrix multiplication
    return X[0:3].transpose() #return an Nx3

def get_limits(pts, factor = 0.1):
    '''
    Returns a bounding box with x,y values bumped out by factor, ignores NaNs
    '''
    RefMin = np.nanmin(pts,axis=0)
    RefMax = np.nanmax(pts,axis=0)

    extents=RefMax-RefMin #extents
    rl=factor*(np.nanmin(extents[0:2])) #linear 'scale' to set up interactor
    return [RefMin[0]-rl, \
      RefMax[0]+rl, \
      RefMin[1]-rl, \
      RefMax[1]+rl, \
      RefMin[2],RefMax[2]]

def get_intersections(outline, angular_offset, width, bead_offset = 0.5, break_point_index = None):
    """
    Returns intersections running from a series of lines drawn from -x to +x, -y to +y for a constant z value
    Params:
        outline - ordered 3D outline points, z must be constant
        angular_offset - rotation which intersection lines are solved for
        width - target bead width
        bead_offset - ratio of bead width to offset each path (0.5 = 50%)
        break_point_index - index of the outline where a single parent outline terminates and a single child outline begins
    Returns:
        path_list - A list of intersecting lines with dual entry Numpy arrays describing the start and end of each line
        actual_bead_offset - and the bead_offset achieved
    """

    trans_cent = np.eye(4)
    #move outline to centroid
    trans_cent[0:3,-1] = -np.mean(outline, axis=0)
    X = do_transform(outline,trans_cent)
    #and rotate by angular_offset
    trans = np.eye(4)
    a = np.deg2rad(angular_offset) #negative for counterclockwise
    trans[0:2,0:2]=np.array([[np.cos(a),-np.sin(a)],[np.sin(a),np.cos(a)]])
    X = do_transform(X,trans)
    
    zval = np.mean(X[:,-1])
    
    limits = get_limits(X,0.)

    yrange = [limits[2]*2,limits[3]*2]
    #break up on the basis of bead width
    num_passes = int(np.floor((limits[1]-(width*bead_offset) - limits[0]+(width*bead_offset))/(width*bead_offset)))
    xrange = np.linspace(limits[0]+(width*bead_offset),limits[1]-(width*bead_offset),num_passes)

    if len(xrange) < 2:
        actual_bead_offset = 0
    else:
        actual_bead_offset = (xrange[1]-xrange[0])/width
    
    intersections = []
    point_list = []  
    previous_max_point_num = 0
    mode_change_times = 0
    for k in range(len(xrange)):
        line = np.array([[xrange[k],yrange[0]], [xrange[k],yrange[1]]])
        line1 = tuple([tuple(x) for x in line.tolist()])

        point_index = 0
        for i in range(len(X)-1):
            #TO AMEND!!: should iterate for more break_points than one.
            if break_point_index is not None:# and len(break_point_index) == 1:
                if i == break_point_index[0]-1:
                    continue
            
                # for j in break_point_index:
                    # if i == j-1:
                        # print('continuing',break_point_index,i,j-1)
                        # continue
                
            line2 = tuple([tuple(x) for x in X[i:i+2,:]])
            local_intersection = line_intersection(line1, line2)
            if local_intersection is not None:
                point_index += 1
                
                intersections.append(np.array([local_intersection[0],local_intersection[1],zval]))
        if point_index != previous_max_point_num:
            previous_max_point_num = point_index
            if previous_max_point_num % 2 != 0:
                print('Warning: odd number of intersections found')
            mode_change_times += 1
        temp_list = [x + mode_change_times*100 for x in range(point_index)]
        temp_list = [str(x) for x in temp_list]
        point_list.extend(temp_list)
    
    #Needs to be 3D for transformation
    intersections = np.asarray(intersections)
    if len(intersections) > 1:
        intersections = intersections[np.lexsort((intersections[:, 1], intersections[:, 0]))]
        trans_intersections = do_transform(intersections,np.linalg.inv(trans))
        trans_intersections = do_transform(trans_intersections,np.linalg.inv(trans_cent))
    
        #pack up/pair intersections for line paths
        path_list = []
        line_index_list = []
        for i in np.arange(len(trans_intersections)-1)[::2]:
            path_list.append(np.array([trans_intersections[i,:], trans_intersections[i+1,:]]))
            line_index_list.append(point_list[i])
    else:
        path_list = []
        line_index_list = []
    #return intersections , actual bead offset
    return path_list, actual_bead_offset, line_index_list

def simple_fill(outline, width = 1, theta = 0, offset = 1):
    '''
    Returns paths corresponding to a simple fill by hatching
    '''
    path_list = []
    midline = offset_poly(outline,-width*0.5)
    innie = offset_poly(outline,-width)
    intersecting_lines, param, _ = get_intersections(
                                innie,theta,width,offset)
    path_list.append(midline)
    path_list.extend(intersecting_lines)
    return path_list


def line_intersection(line1, line2):
    '''
    Returns the x,y intersection intersection of line1 and line2 if it exists.
    Params:
    line1, line2: tuple pairs of x,y points
    Returns:
    x & y values of intersection
    '''

    x1, x2, x3, x4 = line1[0][0], line1[1][0], line2[0][0], line2[1][0]
    y1, y2, y3, y4 = line1[0][1], line1[1][1], line2[0][1], line2[1][1]

    dx1 = x2 - x1
    dx2 = x4 - x3
    dy1 = y2 - y1
    dy2 = y4 - y3
    dx3 = x1 - x3
    dy3 = y1 - y3

    det = dx1 * dy2 - dx2 * dy1
    det1 = dx1 * dy3 - dx3 * dy1
    det2 = dx2 * dy3 - dx3 * dy2

    if det == 0.0:  # lines are parallel
    
        if np.array_equal(line1[0], line2[0]) or np.array_equal(line1[1], line2[0]):
            return line2[0]
        elif np.array_equal(line1[0], line2[1]) or np.array_equal(line1[1], line2[1]):
            return line2[1]
        
        #Special cases
        # if det1 != 0.0 or det2 != 0.0:  # lines are not co-linear
            # pass  # so no solution (or return None)

        # if dx1:
            # if x1 < x3 < x2 or x1 > x3 > x2:
                # pass  # infinitely many solutions (or return np.inf)
        # else:
            # if y1 < y3 < y2 or y1 > y3 > y2:
                # pass  # infinitely many solutions (or return np.inf)

        return None #no intersection

    s = det1 / det
    t = det2 / det

    if 0.0 < s < 1.0 and 0.0 < t < 1.0:
        return x1 + t * dx1, y1 + t * dy1

def respace_equally(X,val, closed = False):
    '''
    Takes X, a 2D array of points, respaces them on the basis of 'val', either a floating point value of what the target interval between points is, or an integer which is the total number of points. Returns the new array of points, the perimeter and the number of points. Setting closed to be True will force the last point to be the same as the first point.
    '''

    distance=np.sqrt(np.sum(np.diff(X,axis=0)**2,axis=1))
    s=np.insert(np.cumsum(distance),0,0)
    Perimeter=np.sum(distance)

    if not isinstance(val,(int)):
        nPts=round(Perimeter/val)
    else:
        nPts = val
    
    sNew=np.linspace(0,s[-1],nPts)
    fx = interp1d(s,X[:,0])
    fy = interp1d(s,X[:,1])
    
    Xnew=fx(sNew)
    Ynew=fy(sNew)
    
    X_new=np.stack((Xnew,Ynew),axis=-1)
    if closed:
        X_new = np.vstack((X_new, X_new[0,:]))#make sure last point is the same as the first point
    return X_new,Perimeter,nPts

def offset_poly(poly, offset):
    '''
    Uses pyclipper to offset param poly and return an offset polygon according to offset param.
    Assumes that the poly is located at a fixed z value
    Poly is 3D (XYZ by N), and returns the same.
    '''
    zval = np.mean(poly[:,-1])
    X = tuple(map(tuple, poly[:,:2]))
    scaled_poly = scale_to_clipper(X)
    pco = PyclipperOffset()
    pco.AddPath(scaled_poly, JT_SQUARE, ET_CLOSEDPOLYGON)
    scaled_result = pco.Execute(scale_to_clipper(offset))
    
    result = scale_from_clipper(scaled_result)
    if result:
        two_d = np.asarray(result[0])
    
        # #make sure the number of points and therefore polygon interval is preserved
        # two_d = respace_equally(two_d,len(poly))[0]
        
        return np.column_stack((two_d,np.ones(len(two_d))*zval))
    else:
        return None