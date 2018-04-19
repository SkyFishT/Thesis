import os

def productdata():
    width = 4
    datafile = open('data.txt','w')
    data=[]
    for i in range(width):
        for j in range(width-1):
            data.append(((i*10,j*10),(i*10,(j+1)*10)))
    for j in range(width):
        for i in range(width-1):
            data.append(((i*10,j*10),((i+1)*10,j*10)))
    datafile.write(str(data))
    datafile.close()

if __name__ == '__main__':
    productdata()