from scipy.optimize import linprog
import os,math,time,numpy as np
def liner_programming(epsilon=0.1,delta=1.1,global_scope=False):
    points_file = open(os.path.join(os.getcwd(),'datas', 'points.txt'), 'r')
    points = eval(points_file.read())
    numbers_of_points = len(points)
    numbers_of_various = numbers_of_points * numbers_of_points
    c = [0] * numbers_of_various
    ratio = math.pow(math.e, epsilon / delta)
    if global_scope==True:
        print 'global differentiate'
        print 'the number of points is ' + str(numbers_of_points)
        print points
        print 'numbers_of_various is:' + str(numbers_of_various)
        delta_spanner_pairs = np.load(os.path.join(os.getcwd(),'datas', 'delta_spanner.npy'))
        def distance_of_two_point(x,y,ndigits=2):
            return round(math.sqrt(math.pow(x[0]-y[0],2)+math.pow(x[1]-y[1],2)),ndigits)
        #set the objective function arguments
        for i in range(len(points)):
            for j in range(len(points)):
                c[i*len(points)+j] = distance_of_two_point(points[i],points[j])
        print "c is:"+str(c)
        a_ub = []
        b_ub = []
        a_eq = []
        b_eq = []
        r = []
        #product the a_ub and b_ub
        for i in range(len(points)):
            for j in range(len(points)):
                if delta_spanner_pairs[i,j] == 1:
                    for k in range(len(points)):
                        tmp_a = [0] * numbers_of_various
                        tmp_a[i*len(points)+k] = 1
                        tmp_a[j*len(points)+k] = -ratio
                        a_ub.append(tmp_a)
                        b_ub = b_ub + [0]
        print "a_ub size:"+str(len(a_ub))+","+str(len(a_ub[0]))+",b_ub size:"+str(len(b_ub))

    else:
        print 'subareas differentiate'
        print 'the number of points is ' + str(numbers_of_points)
        print points
        print 'numbers_of_various is:' + str(numbers_of_various)
        crossroad_file = open(os.path.join(os.getcwd(),'datas', 'cross_road.txt'), 'r')
        crossroad = eval(crossroad_file.read())
        a_ub = []
        b_ub = []
        a_eq = []
        b_eq = []
        r = []
        #the dictionary that stores the points of crossroad
        points_in_scpoe_array_dict={}
        #product a_ub and b_ub
        for i in crossroad:
            points_in_scpoe_array_dict[i]=[]
            points_in_scope_file = open(os.path.join(os.getcwd(),'datas', 'points_in_scope'+str(i)+'.txt'), 'r')
            points_in_scope_array=(eval(points_in_scope_file.read()))
            delta_spanner_pairs=np.load(os.path.join(os.getcwd(),'datas', 'delta_spanner'+str(i)+'.npy'))
            for item in points_in_scope_array:
                points_in_scpoe_array_dict[i].append(item[0])
                for item2 in points_in_scope_array:
                    if delta_spanner_pairs[item[0],item2[0]]==1:
                        print 'a:'+str(item[0])+',b:'+str(item2[0])
                        for k in range(len(points)):
                            tmp_a = [0] * numbers_of_various
                            tmp_a[item[0] * len(points) + k] = 1
                            tmp_a[item2[0] * len(points) + k] = -ratio
                            a_ub.append(tmp_a)
                            b_ub = b_ub + [0]
        delta_spanner_global = np.load(os.path.join(os.getcwd(),'datas', 'delta_spanner_global.npy'))
        for i in range(len(crossroad)):
            for j in range(len(crossroad)):
                if delta_spanner_global[i,j]==1:
                    for k in range(len(points)):
                        tmp_a = [0] * numbers_of_various
                        for argu_eq_one in points_in_scpoe_array_dict[crossroad[i]]:
                            tmp_a[argu_eq_one*len(points)+k] = 1
                        for argu_eq_epsilon in points_in_scpoe_array_dict[crossroad[j]]:
                            tmp_a[argu_eq_epsilon*len(points)+k] = -ratio
                        a_ub.append(tmp_a)
                        b_ub = b_ub + [0]

        def distance_of_two_point(x, y, ndigits=2):
            return round(math.sqrt(math.pow(x[0] - y[0], 2) + math.pow(x[1] - y[1], 2)), ndigits)

        # set the objective function arguments
        for i in range(len(points)):
            for j in range(len(points)):
                c[i * len(points) + j] = distance_of_two_point(points[i], points[j])
        print "c is:" + str(c)
        print "a_ub size:" + str(len(a_ub)) + "," + str(len(a_ub[0])) + ",b_ub size:" + str(len(b_ub))
    # product the a_eq and b_eq
    for i in range(len(points)):
        tmp_a = []
        for j in range(len(points)):
            if i == j:
                tmp_a = tmp_a + [1] * len(points)
            else:
                tmp_a = tmp_a + [0] * len(points)
        a_eq.append(tmp_a)
        b_eq = b_eq + [1]

    print "a_eq size:" + str(len(a_eq)) + "," + str(len(a_eq[0])) + ",b_ub size:" + str(len(b_eq))
    print "b_eq:" + str(b_eq)
    for i in range(numbers_of_various):
        r.append((0, 1))
    len_a_ub = len(a_ub)
    np_a_ub = np.zeros((len_a_ub, numbers_of_various))
    for i in range(len_a_ub):
        for j in range(numbers_of_various):
            np_a_ub[i, j] = a_ub[i][j]
    len_a_eq = len(a_eq)
    np_a_eq = np.zeros((len_a_eq, numbers_of_various))
    for i in range(len_a_eq):
        for j in range(numbers_of_various):
            np_a_eq[i, j] = a_eq[i][j]
    res = linprog(c, np_a_ub, b_ub, np_a_eq, b_eq, bounds=tuple(r),method='interior-point',options={'maxiter':500})
    print res
    return res.x.tolist()

if __name__ == "__main__":
    cur_time = time.time()
    liner_programming()