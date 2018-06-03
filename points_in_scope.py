import os,math

def points_in_scope_global():
    pointsfile = open(os.path.join(os.getcwd(), 'points.txt'), 'r')  # set of points
    points_in_scope_file = open(os.path.join(os.getcwd(), 'points_in_scope.txt'), 'w')  # set of points
    points_in_scope_file.write(pointsfile.read())
    pointsfile.close()
    points_in_scope_file.close()

def points_in_scope_round(cross_point,radius):
    pointsfile = open(os.path.join(os.getcwd(), 'points.txt'), 'r')  # set of points
    points_in_scope_file = open(os.path.join(os.getcwd(), 'points_in_scope'+str(cross_point)+'.txt'), 'w')  # set of points
    points = eval(pointsfile.read())
    points_in_scope_array = []
    def distance_of_two_point(x,y):
        return math.sqrt(math.pow(x[0]-y[0],2)+math.pow(x[1]-y[1],2))
    for i in range(len(points)):
        if distance_of_two_point(cross_point,points[i]) <= radius:
            points_in_scope_array.append((i,points[i]))
    points_in_scope_file.write(str(points_in_scope_array))
    points_in_scope_file.close()

def points_in_scope_rectangle(xs,xe,ys,ye):
    pointsfile = open(os.path.join(os.getcwd(), 'points.txt'), 'r')  # set of points
    points_in_scope_file = open(os.path.join(os.getcwd(), 'points_in_scope.txt'), 'w')  # set of points
    points = eval(pointsfile.read())
    points_in_scope_array = []
    for i in points:
        if i[0] >=xs and i[0]<=xe and i[1] >=ys and i[1] <= ye:
            points_in_scope_array.append(i)
    points_in_scope_file.write(str(points_in_scope_array))
    points_in_scope_file.close()
if __name__ == "__main__":
    do=1