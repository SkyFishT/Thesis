import matplotlib.pyplot as plt
import os,numpy as np
import csv

if __name__== '__main__':
    file_name='C:\\workspace\\python\\CapMetrics\data\\vehicle_positions\\2015-03-01.csv'
    positions=[]
    positions2=[]
    with open(file_name) as f:
        reader=csv.reader(f)
        reader.next()
        first_item=reader.next()
        id=first_item[0]
        positions.append((first_item[5],first_item[6]))
        sec_item=reader.next()
        positions2.append((sec_item[5], sec_item[6]))
        for row in reader:
            if id==row[0]:
                continue
            else:
                id=row[0]
                positions.append((row[5], row[6]))
                tmp_item=reader.next()
                positions2.append((tmp_item[5], tmp_item[6]))
    for i in range(50):
        plt.scatter(positions[i][0],positions[i][1])
        plt.scatter(positions2[i][0],positions2[i][1])
    plt.show()