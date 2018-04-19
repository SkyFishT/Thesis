from scipy.optimize import linprog
import os,math,numpy as np

def liner_programming():
    points_file = open(os.path.join(os.getcwd(), 'points.txt'), 'r')
    points = eval(points_file.read())
    sort_egdes_file = open(os.path.join(os.getcwd(), 'sort_edges.txt'), 'r')
    sort_egdes = eval(sort_egdes_file.read())
    delta_spanner_pairs = np.load(os.path.join(os.getcwd(), 'delta_spanner.npy'))
    delta=1.4
    epsilon=0.1
    ratio = math.pow(math.e,epsilon/delta)
    dimension = len(points)
    c = [0]*dimension*dimension
    for i in sort_egdes:
        x = i['pointA']
        y = i['pointB']
        c[x*dimension+y] = i['distance']
        c[y*dimension+x] = i['distance']
    a_ub = []
    b_ub = []
    a_eq = []
    b_eq = []
    r = []
    for i in range(dimension):
        for j in range(dimension):
            if delta_spanner_pairs[i,j] == 1:
                for k in range(dimension):
                    tmp_a = [0] * dimension * dimension
                    tmp_a[i*dimension+k] = 1
                    tmp_a[j*dimension+k] = -ratio
                    a_ub.append(tmp_a)
                    b_ub = b_ub + [0]
    for i in range(dimension):
        tmp_a = []
        for j in range(dimension):
            if i == j:
                tmp_a = tmp_a + [1]*dimension
            tmp_a = tmp_a + [0] * dimension
        a_eq.append(tmp_a)
        b_eq=b_eq+[1]
    for i in range(dimension*dimension):
        r.append((0.1,None))
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

if __name__ == "__main__":
    liner_programming()