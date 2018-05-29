import data,edges,points,points_in_scope,sort_edges,delta_spanner,linprog,draw_plot,points_in_scope


if __name__ == "__main__":
    epsilon = 0.7
    delta = 1.1
    cross_roads = 10
    split = 5
    data.productdata(cross_roads)
    edges.productedges(split)
    points.productpoints()
    points_in_scope.points_in_scope_rectangle(0,10,0,10)
    sort_edges.sort_edges()
    delta_spanner.delta_spanner(delta)
    draw_plot.draw_plot()
    linprog.liner_programming(epsilon,delta)