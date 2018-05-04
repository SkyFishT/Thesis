from scipy.optimize import linprog
import os,math,time,numpy as np
def liner_programming(epsilon=0.1,delta=1.1):
    points_file = open(os.path.join(os.getcwd(), 'points.txt'), 'r')
    points = eval(points_file.read())
    sort_egdes_file = open(os.path.join(os.getcwd(), 'sort_edges.txt'), 'r')
    sort_egdes = eval(sort_egdes_file.read())
    cloest_cross_road_file = open(os.path.join(os.getcwd(), 'cloest_cross_road.txt'), 'r')
    cloest_cross_road_array = eval(cloest_cross_road_file.read())
    delta_spanner_pairs = np.load(os.path.join(os.getcwd(), 'delta_spanner.npy'))
    linpro_file = open(os.path.join(os.getcwd(), 'linpro.txt'), 'w')
    ratio = math.pow(math.e,epsilon/delta)
    dimension = len(points)
    c = [0]*dimension*dimension
    print 'dimension is:'+str(dimension)
    def distance_of_two_point(x,y):
        return math.sqrt(math.pow(x[0]-y[0],2)+math.pow(x[1]-y[1],2))
    def get_cloest_cross_road(point):
        for i in cloest_cross_road_array:
            if i[0]==point:
                return i[1]
    for i in range(dimension):
        for j in range(dimension):
            closest_cross_road = get_cloest_cross_road(i)
            c[i*dimension+j] = distance_of_two_point(points[closest_cross_road],points[j])
    print "c is:"+str(c)
    a_ub = []
    b_ub = []
    a_eq = []
    b_eq = []
    r = []
    #product the a_ub and b_ub
    for i in range(dimension):
        for j in range(dimension):
            if delta_spanner_pairs[i,j] == 1:
                for k in range(dimension):
                    tmp_a = [0] * dimension * dimension
                    tmp_a[i*dimension+k] = 1
                    tmp_a[j*dimension+k] = -ratio
                    a_ub.append(tmp_a)
                    b_ub = b_ub + [0]

    print "a_ub size:"+str(len(a_ub))+","+str(len(a_ub[0]))+",b_ub size:"+str(len(b_ub))
    # product the a_eq and b_eq
    for i in range(dimension):
        tmp_a = []
        for j in range(dimension):
            if i == j:
                tmp_a = tmp_a + [1]*dimension
            else:
                tmp_a = tmp_a + [0] * dimension
        a_eq.append(tmp_a)
        b_eq=b_eq+[1]
    print "a_eq size:" + str(len(a_eq)) + "," + str(len(a_eq[0])) + ",b_ub size:" + str(len(b_eq))
    for i in range(dimension*dimension):
        r.append((0.001,1))
    len_a_ub = len(a_ub)
    np_a_ub = np.zeros((len_a_ub,dimension*dimension))
    for i in range(len_a_ub):
        for j in range(dimension*dimension):
            np_a_ub[i,j] = a_ub[i][j]
    len_a_eq = len(a_eq)
    np_a_eq = np.zeros((len_a_eq, dimension * dimension))
    for i in range(len_a_eq):
        for j in range(dimension * dimension):
            np_a_eq[i, j] = a_eq[i][j]
    res = linprog(np.array(c), np_a_ub, b_ub, np_a_eq, b_eq, bounds=tuple(r))
    print res
    linpro_file.write(str(res))
    linpro_file.close()

if __name__ == "__main__":
    cur_time = time.time()
    liner_programming(2,1.5)