import os,points_in_scope,sort_edges,delta_spanner,linprog,time,numpy as np

def product_matrix(epsilon = 0.8,delta = 1.5,global_scope=False):
    radius = 4.9
    points_file = open(os.path.join(os.getcwd()+'\\datas', 'points.txt'), 'r')
    points = eval(points_file.read())
    nums_of_points = (len(points))
    result = np.zeros((nums_of_points, nums_of_points))
    linpro_file = open(os.path.join(os.getcwd()+'\\datas', 'linprog' + str(epsilon) + '.txt'), 'w')

    def fuzhi2result(result, result_index, linprog_result, lingpro_index):
        for i in range(nums_of_points):
            result[result_index, i] = linprog_result[lingpro_index * len(points) + i]

    if global_scope==True:
        cur_time = time.time()
        points_in_scope.points_in_scope_global()
        sort_edges.sort_edges(None,True)  # sort segment roads
        delta_spanner.delta_spanner(None,delta,True)  # product delta spanner tree
        linprog_result = linprog.liner_programming(epsilon, delta,True)
    else:
        crossroad_file = open(os.path.join(os.getcwd()+'\\datas', 'cross_road.txt'), 'r')
        crossroad = eval(crossroad_file.read())
        for i in crossroad:
            global cur_time
            cur_time = time.time()
            points_in_scope.points_in_scope_round(i, radius)  # points in scope to join differential privacy
            sort_edges.sort_edges(i)  # sort segment roads
            delta_spanner.delta_spanner(i,delta)  # product delta spanner tree
        sort_edges.sort_edges_global()  # sort segment roads
        delta_spanner.delta_spanner_global(delta)
        linprog_result = linprog.liner_programming(epsilon, delta)
    linprog_index=-1
    for i in points:
        linprog_index+=1
        result_index=-1
        for j in points:
            result_index+=1
            if i==j:
                fuzhi2result(result,result_index,linprog_result,linprog_index)
    result_buffer=[]
    for i in range(nums_of_points):
        result_buffer_tmp=[0]*nums_of_points
        for j in range(nums_of_points):
            if(result[i,j]<=1e-5):
                result_buffer_tmp[j] = 0
            else:
                result_buffer_tmp[j] = round(result[i,j],5)
        result_buffer.append(result_buffer_tmp)
    linpro_file.write(str(result_buffer))
    linpro_file.close()

if __name__=='__main__':
    product_matrix()
