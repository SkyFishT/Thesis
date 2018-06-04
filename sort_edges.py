import os,math
def dist_of_points(i,j): #distance of two points
    return round(math.sqrt((i[0]-j[0])**2+(i[1]-j[1])**2),2)
def cmp(x,y):
    if x['distance']-y['distance'] <= 0:
        return -1
    else:
        return 1
def sort_edges(cross_point,global_scpoe=False):
    if global_scpoe==True:
        sort_edges_file = open(os.path.join(os.getcwd(),'datas', 'sort_edges.txt'), 'w')
        pointsfile = open(os.path.join(os.getcwd(),'datas', 'points.txt'), 'r')  # set of points
        sorted_edges = []
        points = eval(pointsfile.read())
        num_of_points = len(points)  # number of points
        for i in range(num_of_points):
            j = i
            while j < num_of_points:
                sorted_edges.append({'pointA': i, 'pointB': j, 'distance': dist_of_points(points[i], points[j])})
                j = j + 1
    else:
        sort_edges_file = open(os.path.join(os.getcwd(),'datas', 'sort_edges'+str(cross_point)+'.txt'), 'w')
        pointsfile = open(os.path.join(os.getcwd(),'datas', 'points_in_scope'+str(cross_point)+'.txt'), 'r')  # set of points
        sorted_edges = []
        points = eval(pointsfile.read())
        num_of_points = len(points)  # number of points
        for i in range(num_of_points):
            j = i
            while j < num_of_points:
                sorted_edges.append({'pointA': points[i][0], 'pointB': points[j][0], 'distance': dist_of_points(points[i][1], points[j][1])})
                j = j + 1


    sorted_edges.sort(cmp)
    sort_edges_file.write(str(sorted_edges))
    sort_edges_file.close()
    return sorted_edges

def sort_edges_global():
    sort_edges_file = open(os.path.join(os.getcwd(),'datas', 'sort_edges_global.txt'), 'w')
    pointsfile = open(os.path.join(os.getcwd(),'datas', 'cross_road.txt'), 'r')  # set of points
    sorted_edges = []
    points = eval(pointsfile.read())
    num_of_points = len(points)  # number of points
    for i in range(num_of_points):
        j = i
        while j < num_of_points:
            sorted_edges.append({'pointA': i, 'pointB': j, 'distance': dist_of_points(points[i], points[j])})
            j = j + 1
    sorted_edges.sort(cmp)
    sort_edges_file.write(str(sorted_edges))
    sort_edges_file.close()
    return sorted_edges
if __name__ == "__main__":
    sort_edges(cross_point=())