import random,math,os
def distance_of_two_point(x, y, ndigits=2):
    return round(math.sqrt(math.pow(x[0] - y[0], 2) + math.pow(x[1] - y[1], 2)), ndigits)
def product_matrix_exponent(epsilon):
    points_file = open(os.path.join(os.getcwd(), 'datas', 'points.txt'), 'r')
    matrix_file = open(os.path.join(os.getcwd(),'datas', 'exponent' + str(epsilon) + '.txt'), 'w')
    points = eval(points_file.read())
    points_len=len(points)
    tmp_mapping_matrix=[]
    max_distance=0
    for i in points:
        for j in points:
            if max_distance<distance_of_two_point(i,j):
                max_distance = distance_of_two_point(i,j)
    # add in raw proportion
    for i in range(points_len):
        tmp_mapping_matrix.append([])
        for j in range(points_len):
            tmp_mapping_matrix[i].append(math.pow(math.e,epsilon*(max_distance-distance_of_two_point(points[i],points[j]))/2))
    print tmp_mapping_matrix[0]
    #traverse proportion by their proportion
    for i in range(points_len):
        sum=0
        for j in range(points_len):
            sum += tmp_mapping_matrix[i][j]
        for j in range(points_len):
            tmp_mapping_matrix[i][j] /= sum
    matrix_file.write(str(tmp_mapping_matrix))
    matrix_file.close()

def map_position_exponent(cars,epsilon):
    points_file = open(os.path.join(os.getcwd(), 'datas', 'points.txt'), 'r')
    matrix_file = open(os.path.join(os.getcwd(), 'datas', 'exponent' + str(epsilon) + '.txt'), 'r')
    points = eval(points_file.read())
    matrix = eval(matrix_file.read())
    travers_cars = []
    def closest_points(x):
        closest_dist = float('Inf')
        for i in points:
            cur_dist = distance_of_two_point(x, i)
            if closest_dist > cur_dist:
                closest_dist = cur_dist
                closest_point = i
        return closest_point

    def traverse(point):
        closest_point = closest_points(point)
        index = -1
        for i in points:
            index += 1
            if closest_point == i:
                break
        map_array = matrix[index]
        probability = random.random()
        sum = 0
        for i in range(len(map_array)):
            sum += map_array[i]
            if sum > probability:
                return points[i]
        return points[-1]

    for i in cars:
        travers_cars.append(traverse(i))
    return travers_cars
if __name__=="__main__":
    print math.e