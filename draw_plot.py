#coding:utf-8
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import os,numpy as np

def draw_plot():
    pointsfile = open(os.path.join(os.getcwd(),'points_in_scope.txt'),'r')
    edges = np.load(os.path.join(os.getcwd(), 'delta_spanner.npy'))
    print edges
    points = eval(pointsfile.read())
    for i in points:
        plt.scatter(i[0],i[1])

    for i in range(len(points)):
        j = i+1
        while j < len(points):
            if round(edges[i,j])==1:
                plt.plot([points[i][0],points[j][0]], [points[i][1],points[j][1]], c='b')
            j=j+1
    plt.show()
if __name__ == "__main__":
    draw_plot()
    plt.show()
