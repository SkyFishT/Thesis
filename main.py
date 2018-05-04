import data,edges,points,sort_edges,delta_spanner,linprog,draw_plot,cloest_cross_road


if __name__ == "__main__":
    epsilon = 0.1
    delta = 1.4
    cross_roads = 4
    split = 5
    data.productdata(cross_roads)
    edges.productedges(split)
    points.productpoints()
    sort_edges.sort_edges()
    delta_spanner.delta_spanner(delta)
    draw_plot.draw_plot()
    cloest_cross_road.cloest_cross_road()
    linprog.liner_programming(epsilon,delta)