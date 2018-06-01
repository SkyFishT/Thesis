import os,math,matplotlib.pyplot as plt

def draw_plot(cars,mapping_cars,level):
    points_file = open(os.path.join(os.getcwd(), 'points.txt'), 'r')
    points = eval(points_file.read())
    points_set=mapping_cars
    nums_of_subplot=len(points_set)
    def distance_of_two_point(x,y,ndigits=2):
        return round(math.sqrt(math.pow(x[0]-y[0],2)+math.pow(x[1]-y[1],2)),ndigits)
    def closest_points(x):
        closest_dist=float('Inf')
        for i in points:
            cur_dist=distance_of_two_point(x,i)
            if closest_dist > cur_dist:
                closest_dist = cur_dist
                closest_point=i
        return closest_point

    for index_points in range(nums_of_subplot):
        plt.subplot(nums_of_subplot,2,(index_points+1)*2-1)
        format_points={}
        print points_set[index_points]
        for i in points_set[index_points]:
            if format_points.has_key(i)==False:
                format_points[i]=1
            else :
                format_points[i]+=1
        #max_num = 0
        #for i in format_points.iterkeys():
        #    if max_num < format_points[i]:
        #        max_num = format_points[i]
        for i in format_points.iterkeys():
            if format_points[i]<level:
                plt.scatter(i[0],i[1],c='#D8BFD8')
            elif format_points[i]>=level and format_points[i]<level*2:
                plt.scatter(i[0], i[1], c='#DA70D6')
            elif format_points[i]>=level*2 and format_points[i]<level*3:
                plt.scatter(i[0], i[1], c='#800080')
            else:
                plt.scatter(i[0], i[1], c='#000000')
        plt.subplot(nums_of_subplot, 2, (index_points + 1) * 2)
        tmp_cars=[]
        for i in cars:
            tmp_cars.append(closest_points(i))
        format_points2 = {}
        for i in tmp_cars:
            if format_points2.has_key(i) == False:
                format_points2[i] = 1
            else:
                format_points2[i] += 1
        for i in format_points2.iterkeys():
            if format_points2[i]<level:
                plt.scatter(i[0],i[1],c='#D8BFD8')
            elif format_points2[i]>=level and format_points2[i]<level*2:
                plt.scatter(i[0], i[1], c='#DA70D6')
            elif format_points2[i]>=level*2 and format_points2[i]<level*3:
                plt.scatter(i[0], i[1], c='#800080')
            else:
                plt.scatter(i[0], i[1], c='#000000')
        different=0
        for i in points:
            if format_points.has_key(i)==False and format_points2.has_key(i)==True:
                if format_points2[i]>level:
                    different += 1
            elif format_points.has_key(i)==True and format_points2.has_key(i)==False:
                if format_points[i]>level:
                    different += 1
            elif format_points.has_key(i)==True and format_points2.has_key(i)==True:
                if abs(format_points2[i]- format_points[i])>level:
                    different+=1
        rate=float(different)/len(points)
        print 'different rate is:'+str(rate*100)+'%'
    plt.show()
if __name__ == "__main__":
    draw_plot()
