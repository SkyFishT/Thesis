import data,edges,points,points_in_scope,sort_edges,delta_spanner,linprog,os#,draw_plot
import product_probability_matrix#,draw_plot_by_points,product_cars,map_position_by_matrix

if __name__ == "__main__":
    epsilon_set = [0.7,1.5,2]
    delta = 1.5
    radius =100 
    cross_roads = 4
    height = width = (cross_roads - 1) * 10
    split = 5
    data.productdata(cross_roads)  # product cross road
    edges.productedges(split)  # split roads by segment road
    points.productpoints()  # product points according to segment road
    #product_cars.product_cars_by_random(500, width, height, 10)
    #cars = eval(open(os.path.join(os.getcwd(), 'row_cars.txt'), 'r').read())
    #maping_cars=[]
    for epsilon in epsilon_set:
        product_probability_matrix.product_matrix(epsilon,delta,radius)
        #traverse_cars = map_position_by_matrix.map_position(cars,epsilon)
        #maping_cars.append(traverse_cars)
    #positions=((cross_roads-1)*10/split+1)*cross_roads*2-cross_roads*cross_roads
    #level=len(cars)/float(positions)
    #print len(cars),positions
    #draw_plot_by_points.draw_plot(cars,maping_cars,level)
    #draw_plot_by_points.draw_plot(traverse_cars)
    #points_in_scope.points_in_scope_round((0,0),4.9) #points in scope to join differential privacy
    #sort_edges.sort_edges() #sort segment roads
    #delta_spanner.delta_spanner(delta) #product delta spanner tree
    #draw_plot.draw_plot()
    #linprog.liner_programming(epsilon,delta) #product
