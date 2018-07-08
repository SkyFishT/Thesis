import os
def productdata(width=4):
    road_length = 10
    datafile = open(os.path.join(os.getcwd(), 'datas', 'data.txt'), 'w')
    cross_road_file = open(os.path.join(os.getcwd(), 'datas', 'cross_road.txt'), 'w')
    data=[]
    cross_road = set()
    for i in range(width):
        i=float(i)
        for j in range(width-1):
            j=float(j)
            data.append(((i*road_length,j*road_length),(i*road_length,(j+1)*road_length)))
            cross_road.add((i*road_length,j*road_length))
            cross_road.add((i*road_length,(j+1)*road_length))
    for j in range(width):
        j=float(j)
        for i in range(width-1):
            i=float(i)
            data.append(((i*road_length,j*road_length),((i+1)*road_length,j*road_length)))
            cross_road.add((i*road_length,j*road_length))
            cross_road.add(((i+1)*road_length,j*road_length))

    datafile.write(str(data))
    datafile.close()
    cross_road_file.write(str(list(cross_road)))
    cross_road_file.close()

if __name__ == '__main__':
    productdata()
