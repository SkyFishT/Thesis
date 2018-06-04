import data,edges,points,sort_edges,os,time,product_probability_matrix,math,product_cars,map_position_by_matrix

def product_matrix(cross_roads,split,epsilon_set,global_scope=False):
    global cur_time
    experiment_files = open(os.path.join(os.getcwd(),'datas', 'experiment.txt'), 'w')
    delta = 1.5
    data.productdata(cross_roads)  # product cross road
    edges.productedges(split)  # split roads by segment road
    points.productpoints()  # product points according to segment road
    times=[]
    for epsilon in epsilon_set:
        cur_time = time.time()
        product_probability_matrix.product_matrix(epsilon,delta,global_scope)
        times.append({'epsilon':epsilon,'time':time.time()-cur_time})
    experiment_files.write(str(times)+'\n')
    experiment_files.close()

def product_error_rate(cross_roads,epsilon_set,experi_times):
    experiment_files = open(os.path.join(os.getcwd() + '\\datas', 'experiment.txt'), 'a')
    cars = eval(open(os.path.join(os.getcwd() + '\\datas', 'row_cars.txt'), 'r').read())
    points_file = open(os.path.join(os.getcwd() + '\\datas', 'points.txt'), 'r')
    points = eval(points_file.read())
    height = width = (cross_roads - 1) * 10
    nums_of_points_set = len(epsilon_set)
    level = len(cars) / float(len(points))
    def distance_of_two_point(x, y, ndigits=2):
        return round(math.sqrt(math.pow(x[0] - y[0], 2) + math.pow(x[1] - y[1], 2)), ndigits)

    def closest_points(x):
        closest_dist = float('Inf')
        for i in points:
            cur_dist = distance_of_two_point(x, i)
            if closest_dist > cur_dist:
                closest_dist = cur_dist
                closest_point = i
        return closest_point
    def experiment_in_error(rates):
        product_cars.product_cars_by_random(1000, width, height, 10)
        maping_cars = []
        for epsilon in epsilon_set:
            traverse_cars = map_position_by_matrix.map_position(cars, epsilon)
            maping_cars.append(traverse_cars)
        points_file = open(os.path.join(os.getcwd() + '\\datas', 'points.txt'), 'r')
        points = eval(points_file.read())
        points_set = maping_cars
        for index_points in range(nums_of_points_set):
            format_points = {}
            for i in points_set[index_points]:
                if format_points.has_key(i) == False:
                    format_points[i] = 1
                else:
                    format_points[i] += 1
            tmp_cars = []
            for i in cars:
                tmp_cars.append(closest_points(i))
            format_points2 = {}
            for i in tmp_cars:
                if format_points2.has_key(i) == False:
                    format_points2[i] = 1
                else:
                    format_points2[i] += 1
            different = 0
            for i in points:
                if format_points.has_key(i) == False and format_points2.has_key(i) == True:
                    if format_points2[i] > level:
                        different += 1
                elif format_points.has_key(i) == True and format_points2.has_key(i) == False:
                    if format_points[i] > level:
                        different += 1
                elif format_points.has_key(i) == True and format_points2.has_key(i) == True:
                    if abs(format_points2[i] - format_points[i]) > level:
                        different += 1
            rate = float(different) / len(points)
            rates[index_points].append(rate)
    rates=[]
    for i in range(nums_of_points_set):
        rates.append([])
    for i in range(experi_times):
        experiment_in_error(rates)
    avg_rate=[0]*nums_of_points_set
    for i in range(nums_of_points_set):
        for j in range(experi_times):
            avg_rate[i]+=rates[i][j]
    for i in range(nums_of_points_set):
        experiment_files.write('in epsilon_array'+str(i)+':' + str(rates[i])+ '\n')
        avg_rate[i]=avg_rate[i]/experi_times
    experiment_files.write('level:' + str(level) + '\n')
    experiment_files.write('average_rates:' + str(avg_rate)+ '\n')
    experiment_files.close()
if __name__ == "__main__":
    epsilon_set = [0.69, 1.38, 1.79, 2.07]
    delta = 1.5
    cross_roads = 2
    split = 3.4
    global_ok=[True,False]
    product_matrix(cross_roads,split,epsilon_set,True)
    product_error_rate(cross_roads,epsilon_set,200)
    #for i in range(len(split)):
    #    print str(split[i])
    #    for j in range(len(global_ok)):
    #        product_matrix(cross_roads, split[i], epsilon_set, global_ok[j])
    #        product_error_rate(cross_roads, epsilon_set, 40)