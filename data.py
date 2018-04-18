import os

def productdata():
    datafile = open('data.txt','w')
    data=[]
    for i in range(4):
        for j in range(3):
            data.append(((i*10,j*10),(i*10,(j+1)*10)))
    for j in range(4):
        for i in range(3):
            data.append(((i*10,j*10),((i+1)*10,j*10)))
    datafile.write(str(data))
    datafile.close()

if __name__ == '__main__':
    productdata()