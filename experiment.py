import data,edges,points,sort_edges,os,time,product_probability_matrix,math,product_cars,map_position_by_matrix
import planeLaplace

def product_matrix(cross_roads,split,epsilon_set,delta,global_scope=False):
    global cur_time
    experiment_files = open(os.path.join(os.getcwd(),'datas', 'experiment.txt'), 'w')
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

def product_error_rate(cross_roads,epsilon_set,experi_times,numofcars):
    height = width = (cross_roads - 1) * 10
    product_cars.product_cars_by_random(numofcars, width, height, 10)
    experiment_files = open(os.path.join(os.getcwd() ,'datas', 'experiment.txt'), 'a')
    cars = eval(open(os.path.join(os.getcwd() ,'datas', 'row_cars.txt'), 'r').read())
    points_file = open(os.path.join(os.getcwd() ,'datas', 'points.txt'), 'r')
    points = eval(points_file.read())
    nums_of_points_set = len(epsilon_set)

    def distance_of_two_point(x, y, ndigits=2):
        #print 'x:'+str(x)
        #print 'y:'+str(y)
        return round(math.sqrt(math.pow(x[0] - y[0], 2) + math.pow(x[1] - y[1], 2)), ndigits)

    def closest_points(x):
        closest_dist = float('Inf')
        for i in points:
            cur_dist = distance_of_two_point(x, i)
            if closest_dist > cur_dist:
                closest_dist = cur_dist
                closest_point = i
        return closest_point
    def experiment_in_error(diff,mae_diff,diff_sum,contrast_diff_sum):
        maping_cars = []
        contrast_maping_cars = []
        for epsilon in epsilon_set:
            traverse_cars = map_position_by_matrix.map_position(cars, epsilon)
            maping_cars.append(traverse_cars)
        for epsilon in epsilon_set:
            traverse_cars = planeLaplace.map_position_planeLaplace(cars, epsilon,closest_points)
            contrast_maping_cars.append(traverse_cars)

        points_file = open(os.path.join(os.getcwd() ,'datas', 'points.txt'), 'r')
        points = eval(points_file.read())
        points_set = maping_cars
        contrast_points_set = contrast_maping_cars
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
                    different += format_points2[i]
                elif format_points.has_key(i) == True and format_points2.has_key(i) == False:
                    different += format_points[i]
                elif format_points.has_key(i) == True and format_points2.has_key(i) == True:
                    different += abs(format_points2[i] - format_points[i])
            avg_diff=float(different)/len(points) 
            diff[index_points].append(avg_diff)
            mae_different=0
            for i in points:
                if format_points.has_key(i) == False and format_points2.has_key(i) == True:
                    mae_different+=(abs(avg_diff-format_points2[i]))
                elif format_points.has_key(i) == True and format_points2.has_key(i) == False:
                    mae_different+=(abs(avg_diff-format_points[i]))
                elif format_points.has_key(i) == True and format_points2.has_key(i) == True:
                    mae_different+=(abs(avg_diff-abs(format_points2[i] - format_points[i])))
                else:
                    mae_different+=(avg_diff)
            mae_different /= float(len(points))
            mae_diff[index_points].append(mae_different)
            different_sum=0
            contrast_different_sum = 0
            for i in range(numofcars):
                different_sum += distance_of_two_point(points_set[index_points][i],tmp_cars[i])
                contrast_different_sum += distance_of_two_point(contrast_points_set[index_points][i], cars[i])
            diff_sum[index_points].append(different_sum)
            contrast_diff_sum[index_points].append(contrast_different_sum)
    diff=[]
    mae_diff=[]
    diff_sum=[]
    contrast_diff_sum=[]
    for i in range(nums_of_points_set):
        diff.append([])
        mae_diff.append([])
        diff_sum.append([])
        contrast_diff_sum.append([])
    for i in range(experi_times):
        experiment_in_error(diff,mae_diff,diff_sum,contrast_diff_sum)
    AVG_diff=[0]*nums_of_points_set
    MAE_diff=[0]*nums_of_points_set
    AVG_DIFF_SUM = [0] * nums_of_points_set
    CONTRAST_AVG_DIFF_SUM1 = [0] * nums_of_points_set
    for i in range(nums_of_points_set):
        for j in range(experi_times):
            AVG_diff[i]+=diff[i][j]
            MAE_diff[i]+=mae_diff[i][j]
            AVG_DIFF_SUM[i]+=diff_sum[i][j]
            CONTRAST_AVG_DIFF_SUM1[i] += contrast_diff_sum[i][j]
    for i in range(nums_of_points_set):
        #experiment_files.write('in epsilon_array-'+str(epsilon_set[i])+':' + str(diff[i])+ '\n')
        AVG_diff[i]=AVG_diff[i]/experi_times
        MAE_diff[i]/=experi_times
        AVG_DIFF_SUM[i] /= experi_times
        CONTRAST_AVG_DIFF_SUM1[i] /= experi_times
    experiment_files.write('avg cars:' + str(float(numofcars)/len(points))+'\n')
    for i in range(nums_of_points_set):
        #experiment_files.write('average_differ:' + str(AVG_diff[i])+ '\n')
        #experiment_files.write('mae_differ:' + str(MAE_diff[i])+'\n')
        experiment_files.write('average_differ_distance_sum:' + str(AVG_DIFF_SUM[i]) + '\n')
        experiment_files.write('contrast_average_differ_distance_sum1:' + str(CONTRAST_AVG_DIFF_SUM1[i]) + '\n')
    experiment_files.close()
    return AVG_DIFF_SUM
if __name__ == "__main__":
    #experiment_files = open(os.path.join(os.getcwd(), 'datas', 'experiment.txt'), 'a')
    epsilon_set = [(x+1)/float(5) for x in range(10)]
    delta = 1.5
    cross_roads = 3
    split = 3.4
    global_ok=[True]
    experiment_times=20
    number_of_cars=500
    two_mode=[]
    diff_rate=[]
    for i in global_ok:
        product_matrix(cross_roads, split, epsilon_set, delta, i)
        two_mode.append(product_error_rate(cross_roads,epsilon_set,experiment_times,number_of_cars))
    #for i in range(len(two_mode[0])):
        #diff_rate.append(abs(two_mode[0][i]-two_mode[1][i])/two_mode[0][i])
    #experiment_files.write(str(diff_rate))
    #experiment_files.close()
    #for i in range(len(split)):
    #    print str(split[i])
    #    for j in range(len(global_ok)):
    #        product_matrix(cross_roads, split[i], epsilon_set, global_ok[j])
    #        product_error_rate(cross_roads, epsilon_set, 40)
