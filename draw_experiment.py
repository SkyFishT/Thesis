#coding:utf-8
import matplotlib.pyplot as plt

def draw_exper():
    x1 = [(x+1)*0.2 for x in range(20)]
    # 体重
    y1 = [6849, 3849, 2159, 1263, 757, 485, 317, 192, 133, 75, 48, 26, 18, 11, 7, 3, 3, 1.7, 1.6, 0.8]
    y2 = [3885, 1927, 1257, 908, 698, 555, 467, 416, 341, 311, 279, 260, 233, 218, 202, 195, 186, 168, 155, 154]
    y3 = [9255,6353,4302,2859,1924,1308,926,612,443,297,195,142,106,69,48,35,30,19,13,8]

    # 设置画布大小
    #plt.figure(figsize=(16, 4))

    # 标题
    #plt.title("my weight")
    # 数据
    plt.plot(x1, y1, label='ours', linewidth=3, color='r', marker='o',
              markersize=10)
    plt.plot(x1, y2, label='Laplace', linewidth=3, color='b', marker='v',
              markersize=10)
    plt.plot(x1, y3, label='exponent', linewidth=3, color='y', marker='s',
              markersize=10)
    # 横坐标描述
    plt.xlabel('$\epsilon$')
    # 纵坐标描述
    plt.ylabel('TDE (m)')
    plt.legend()
    plt.show()

if __name__=='__main__':
    draw_exper()