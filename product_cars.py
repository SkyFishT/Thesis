import random,os
def product_cars_by_random(numbers,width,height,segment):
    row_cars_file = open(os.path.join(os.getcwd(), 'row_cars.txt'), 'w')
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

    print 'cols:'+str(cols)+'rows:'+str(rows)

    for i in range(numbers):
        x = random.random()
        y = random.random()
        cars.append([x*width,y*height])
    print 'cars:' + str(cars)
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
            print 'add cars in x,position is:'+str(cars[i])
            cars[i][0] = cols[index]
            print 'travers position is:' + str(cars[i])
        else:
            print 'add cars in y,position is:'+str(cars[i])
            cars[i][1] = rows[index]
            print 'travers position is:' + str(cars[i])
    row_cars_file.write(str(cars))
    row_cars_file.close()
    return cars