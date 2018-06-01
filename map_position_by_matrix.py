import os,math,random
def map_position(cars,epsilon):
    points_file = open(os.path.join(os.getcwd(), 'points.txt'), 'r')
    matrix_file = open(os.path.join(os.getcwd(), 'linprog'+str(epsilon)+'.txt'), 'r')
    points = eval(points_file.read())
    matrix=eval(matrix_file.read())
    travers_cars=[]
    def distance_of_two_point(x,y,ndigits=2):
        return round(math.sqrt(math.pow(x[0]-y[0],2)+math.pow(x[1]-y[1],2)),ndigits)
    def closest_points(x):
        closest_dist=float('Inf')
        for i in points:
            cur_dist=distance_of_two_point(x,i)
            if closest_dist > cur_dist:
                closest_dist = cur_dist
                closest_point=i
        return closest_point

    def traverse(point):
        closest_point = closest_points(point)
        index=-1
        for i in points:
            index+=1
            if closest_point == i:
                break;
        map_array=matrix[index]
        probability = random.random()
        sum=0
        for i in range(len(map_array)):
            sum+=map_array[i]
            if sum>probability:
                return points[i]

    for i in cars:
        travers_cars.append(traverse(i))
    return travers_cars
