#coding:utf-8
import matplotlib.pyplot as plt
import os,numpy as np

def draw_plot():
    pointsInScopeFile = open(os.path.join(os.getcwd(),'datas','points_in_scope.txt'),'r')
    pointsFile = open(os.path.join(os.getcwd(),'datas', 'points.txt'), 'r')
    edges = np.load(os.path.join(os.getcwd(),'datas', 'delta_spanner.npy'))
    points=eval(pointsFile.read())
    pointsInScope = eval(pointsInScopeFile.read())
    k=0
    for i in points:
        plt.scatter(i[0],i[1])
    for i in range(len(pointsInScope)):
        j = i+1
        while j < len(pointsInScope):
            if round(edges[i,j])==1:
                k += 1
                plt.plot([pointsInScope[i][0],pointsInScope[j][0]], [pointsInScope[i][1],pointsInScope[j][1]], c='b')
            j=j+1
    print 'from draw_plot:the number of k' + str(k)
    plt.show()
if __name__ == "__main__":
    draw_plot()
