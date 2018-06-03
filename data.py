import os

def productdata(width=4):
    datafile = open('datas\\data.txt','w')
    cross_road_file = open('datas\\cross_road.txt', 'w')
    data=[]
    cross_road = set()
    for i in range(width):
        i=float(i)
        for j in range(width-1):
            j=float(j)
            data.append(((i*10,j*10),(i*10,(j+1)*10)))
            cross_road.add((i*10,j*10))
            cross_road.add((i*10,(j+1)*10))
    for j in range(width):
        j=float(j)
        for i in range(width-1):
            i=float(i)
            data.append(((i*10,j*10),((i+1)*10,j*10)))
            cross_road.add((i*10,j*10))
            cross_road.add(((i+1)*10,j*10))

    datafile.write(str(data))
    datafile.close()
    cross_road_file.write(str(list(cross_road)))
    cross_road_file.close()

if __name__ == '__main__':
    productdata()