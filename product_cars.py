import random,os
def product_cars_by_random(numbers,width,height,segment):
    row_cars_file = open(os.path.join(os.getcwd(),'datas', 'row_cars.txt'), 'w')
    cars=[]
    cols=[]
    rows=[]
    col=0
    row=0
    cols.append(col)
    rows.append(row)
    while col<=width:
        col+=segment
        cols.append(col)
    while row<=height:
        row+=segment
        rows.append(row)
    for i in range(numbers):
        x = random.random()
        y = random.random()
        cars.append([x*width,y*height])
    for i in range(len(cars)):
        x=True
        index=0
        min_dist=float('Inf')
        for j in range(len(cols)):
            if min_dist> abs(cols[j]-cars[i][0]):
                index = j
                min_dist = abs(cols[j]-cars[i][0])
        for j in range(len(rows)):
            if min_dist> abs(rows[j]-cars[i][1]):
                x=False
                index = j
                min_dist = abs(rows[j]-cars[i][1])
        if x==True:
            cars[i][0] = cols[index]
        else:
            cars[i][1] = rows[index]
    row_cars_file.write(str(cars))
    row_cars_file.close()
    return cars