import os,math

def productedges(splitlength):
    datafile = open(os.path.join(os.getcwd(),'data.txt'),'r')
    edgesfile = open(os.path.join(os.getcwd(),'edges.txt'),'w')
    data=eval(datafile.read())
    segment=[]
    for i in data:
        for j in segsplit(i,splitlength):
            segment.append(j)
    edgesfile.write(str(segment))
    edgesfile.close()
    datafile.close()

def segsplit(i,split_length):
    tempArr = [] #store the segments
    start = i[0]#road's start
    end = i[1]#road's end
    length = math.sqrt(pow(abs(start[0]-end[0]),2)+pow(abs(start[1]-end[1]),2))#road's length
    x_length = end[0]-start[0] #road's x_length
    y_length = end[1]-start[1] #road's y_length
    segments =math.ceil(float(length)/split_length) #road's number of segments
    ratio = split_length/length #segments ratio about road's length
    temp_start = start #start of temp segment
    temp_end = (round(temp_start[0]+x_length*ratio,2),round(temp_start[1]+y_length*ratio,2))#end of temp segment
    while(segments-1):
        segments=segments-1
        tempArr.append((temp_start,temp_end))
        temp_start = temp_end
        temp_end = (round(temp_start[0]+x_length*ratio,2),round(temp_start[1]+y_length*ratio,2))
    tempArr.append((temp_start,end))
    return  tempArr

if __name__ == '__main__':
    productedges(10)
