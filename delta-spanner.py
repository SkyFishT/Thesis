import os,math,time
import numpy as np
cur_time=time.time()
edges_file = open(os.path.join(os.getcwd(),'edges.txt'),'r')
sort_edges_file = open(os.path.join(os.getcwd(),'sort_edges.txt'),'r')
pointsfile = open(os.path.join(os.getcwd(), 'points.txt'), 'r') #set of points
points = eval(pointsfile.read())
edges = eval(edges_file.read()) #list of graph edges
sort_edges = eval(sort_edges_file.read()) #list of sorted euclid distance between all points
num_of_points = len(points) #number of points
delta_spanner_edges = np.zeros((num_of_points,num_of_points))
delta_spanner_edges[delta_spanner_edges == 0] = float('Inf') #initialize all edges to -1 which means points between i and j is disconnect

class AdjacentNode:#link node
    def __init__(self,index,distance=float('Inf'),next_adjacent=None):
        self.index=index
        self.distance=distance
        self.next_adjacent=next_adjacent
    def get_next_adjacent(self):
        return self.next_adjacent
class GraphNode:#node of graph which has elements:index,adjacent_node(link list)
    def __init__(self,index=-1,adjacent_node=None):
        self.index=index
        self.adjacent_node=adjacent_node
    def set_index(self,index):
        self.index = index
    def add_adjacent_node(self,adjacent_node):
        tmp_node=self.adjacent_node
        if tmp_node==None:#if ths node don't have adjacent node
            self.adjacent_node=adjacent_node
        else :
            while tmp_node.next_adjacent!=None:
                tmp_node=tmp_node.next_adjacent
            tmp_node.next_adjacent=adjacent_node
    def get_first_adjacent_nodes(self):
        return self.adjacent_node


def delta_spanner(delta):
    delta_spanner_edges = np.zeros((num_of_points, num_of_points))
    delta_spanner_edges[delta_spanner_edges == 0] = float('Inf')  # initialize all path to -1 which equal to infinity
    points_shortest_array = np.zeros((num_of_points, num_of_points))
    points_shortest_array[points_shortest_array == 0] = float('Inf')  # initialize all path to -1 which equal to infinity
    graph=[]#adjacent table that store structure of points
    for point in points:
        tmp_point = GraphNode(points.index(point))
        graph.append(tmp_point)
    def minpath(points_shortest_array,index,graph):# the shortest path of node of index
        v=[]#the points that have determined the distance
        dist=[float('Inf') for i in graph]
        min_v=index
        dist[index]=0
        while(len(v)<len(dist)):
            v.append(min_v)
            tmp_adjacent = graph[min_v].adjacent_node#get the adjacent node of point of min_v
            while tmp_adjacent!=None:
                if dist[min_v]+tmp_adjacent.distance<dist[tmp_adjacent.index]:
                    dist[tmp_adjacent.index] = dist[min_v]+tmp_adjacent.distance
                tmp_adjacent=tmp_adjacent.next_adjacent
            min_dist=float('Inf')
            for i in range(len(dist)):
                if i in v:
                    continue
                if(dist[i]<min_dist):
                    min_v=i
                    min_dist=dist[i]
        for i in range(len(dist)):
            points_shortest_array[index,i]=dist[i]

    for i in range(len(graph)):
        minpath(points_shortest_array, i, graph)
    for i in sort_edges:
        if points_shortest_array[i['pointA'],i['pointB']]>i['distance']*delta:
            tmp_adj_nodeA = AdjacentNode(i['pointB'],i['distance'])
            tmp_adj_nodeB = AdjacentNode(i['pointA'], i['distance'])
            graph[i['pointA']].add_adjacent_node(tmp_adj_nodeA)
            graph[i['pointB']].add_adjacent_node(tmp_adj_nodeB)
            delta_spanner_edges[i['pointA'], i['pointB']] = 1
            delta_spanner_edges[i['pointB'], i['pointA']] = 1
        for j in range(len(graph)):
            minpath(points_shortest_array,j,graph)
    print delta_spanner_edges
    np.save(os.path.join(os.getcwd(), 'delta_spanner.npy'),delta_spanner_edges)

if __name__ == '__main__':
    delta_spanner(1.4)
    cur_time=time.time()-cur_time
    print cur_time
