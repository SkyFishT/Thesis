#coding:utf-8
import matplotlib.pyplot as plt
import matplotlib
def draw_exper():
    a=["$\delta=1.5$","$\delta=1.4$","$\delta=1.3$","$\delta=1.2$","$\delta=1.1$","$\delta=1.0$"]
    b1=[42,66,65,131,224,0]
    x= range(6)
    plt.bar(left=x, height=b1, width=0.8, alpha=0.4, color='blue')
    plt.ylabel("time (s)",{'size':18})
    plt.xticks(x, a)
    plt.xlabel("The value of $\delta$",{'size':18})
    plt.title("The time of calculation",{'size':18})
    plt.legend()
    plt.show()
if __name__=='__main__':
    draw_exper()