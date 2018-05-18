import os,math
def dist_of_points(i,j): #distance of two points
    return round(math.sqrt((i[0]-j[0])**2+(i[1]-j[1])**2),2)
def sort_edges():
    sort_edges_file = open(os.path.join(os.getcwd(), 'sort_edges.txt'), 'w')
    pointsfile = open(os.path.join(os.getcwd(), 'points_in_scope.txt'), 'r')  # set of points
    sorted_edges=[]
    points = eval(pointsfile.read())
    num_of_points = len(points)  # number of points
    for i in range(num_of_points):
        j = i
        while j<num_of_points:
            sorted_edges.append({'pointA':i,'pointB':j,'distance':dist_of_points(points[i],points[j])})
            j = j + 1
    def cmp(x,y):
        if x['distance']-y['distance'] <= 0:
            return -1
        else:
            return 1
    sorted_edges.sort(cmp)
    sort_edges_file.write(str(sorted_edges))
    sort_edges_file.close()
    return sorted_edges

if __name__ == "__main__":
    sort_edges()