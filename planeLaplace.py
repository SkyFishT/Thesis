import random,math
def map_position_planeLaplace(cars,epsilon,closest_points):
    traverse_cars=[]
    for i in cars:
        tmp_i=[0,0]
        r = random.random()
        dist = math.log(1 - r) / (-epsilon)
        angle = random.random() * math.pi * 2
        tmp_i[0] = i[0] + dist * math.cos(angle)
        tmp_i[1] = i[1] + dist * math.sin(angle)
        tmp_i = closest_points(tmp_i)
        traverse_cars.append(tmp_i)
    return traverse_cars
if __name__ == '__main__':
    def a(x):
        print x+1
    def b(a):
        a(1)
    b(a)