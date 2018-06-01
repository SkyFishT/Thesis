import os,points_in_scope,sort_edges,delta_spanner,linprog,numpy as np

def product_matrix(epsilon = 0.8,delta = 1.5,radius=4.9):
    crossroad_file = open(os.path.join(os.getcwd(), 'cross_road.txt'), 'r')
    crossroad = eval(crossroad_file.read())
    points_file = open(os.path.join(os.getcwd(), 'points.txt'), 'r')
    points = eval(points_file.read())
    nums_of_points=(len(points))
    print 'nums_of_points'+str(nums_of_points)
    result = np.zeros((nums_of_points,nums_of_points))
    linpro_file = open(os.path.join(os.getcwd(), 'linpro.txt'), 'w')
    def fuzhi2result(result,result_index,linprog_result,lingpro_index):
        print 'result_index,lingpro_index:' + str(result_index) + ',' + str(lingpro_index)
        for i in range(nums_of_points):
            result[result_index,i]=linprog_result[lingpro_index*len(points)+i]
    for i in crossroad:
        points_in_scope.points_in_scope_round(i, 4.9)  # points in scope to join differential privacy
        sort_edges.sort_edges()  # sort segment roads
        delta_spanner.delta_spanner(delta)  # product delta spanner tree
        linprog_result = linprog.liner_programming(epsilon, delta)
        points_in_scope_file = open(os.path.join(os.getcwd(), 'points_in_scope.txt'), 'r')
        points_in_scope_array = eval(points_in_scope_file.read())
        linprog_index=-1
        for i in points_in_scope_array:
            linprog_index+=1
            result_index=-1
            for j in points:
                result_index+=1
                if i==j:
                    print 'i:'+str(i)+' j:'+str(j)+' result_index:'+str(result_index)
                    fuzhi2result(result,result_index,linprog_result,linprog_index)
    result_buffer=[]
    for i in range(nums_of_points):
        result_buffer_tmp=[0]*nums_of_points
        for j in range(nums_of_points):
            if(result[i,j]<=1e-5):
                result_buffer_tmp[j] = 0
            else:
                result_buffer_tmp[j] = round(result[i,j],3)
        result_buffer.append(result_buffer_tmp)
    linpro_file.write(str(result_buffer))
    linpro_file.close()

if __name__=='__main__':
    product_matrix()