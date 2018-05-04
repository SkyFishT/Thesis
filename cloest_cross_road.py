import os,math

def cloest_cross_road():
    pointsfile = open(os.path.join(os.getcwd(), 'points.txt'), 'r')  # set of points
    points = eval(pointsfile.read())
    cross_road_file = open(os.path.join(os.getcwd(), 'cross_road.txt'), 'r')  # set of points
    cross_roads = eval(cross_road_file.read())
    cloest_cross_road_file = open('cloest_cross_road.txt','w')
    cloest_cross_road_array = []
    def distance_of_two_point(x,y):
        return math.sqrt(math.pow(x[0]-y[0],2)+math.pow(x[1]-y[1],2))
    for i in points:
        min_distance=float('Inf');
        tmp_cross_road=0;
        for j in cross_roads:
            tmp_distance = distance_of_two_point(i,j)
            if tmp_distance < min_distance:
                min_distance = tmp_distance
                tmp_cross_road = j
        cloest_cross_road_array.append((points.index(i),points.index(tmp_cross_road)))
    cloest_cross_road_file.write(str(cloest_cross_road_array))
    cloest_cross_road_file.close()

if __name__ == "__main__":
    cloest_cross_road()