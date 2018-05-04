def productpoints():
    edgesfile = open('edges.txt', 'r')
    pointsfile = open('points.txt', 'w')
    points=set() # acquire all points
    data = eval(edgesfile.read())
    print data
    for i in data:
        points.add(i[0])
        points.add(i[1])
    points_array=list(points)
    def sort_points(x,y):
        if(x[0]<y[0]):
            return -1
        if(x[0]==y[0]):
            if(x[1]<=y[1]):
                return -1
            else:
                return 1
        return 1
    points_array.sort(sort_points)
    pointsfile.write(str(points_array))
    pointsfile.close()

if __name__ == '__main__':
    productpoints()