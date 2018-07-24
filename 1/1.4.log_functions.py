# 3个对数函数


import math
import matplotlib.pyplot as plt


if __name__ == '__main__':

    x = [float(i)/100 for i in range(1, 300)]
    y1 = [math.log(i, 1.5) for i in x]
    y2 = [math.log(i, 2) for i in x]
    y3 = [math.log(i, 3) for i in x]
    a = [1.0, 1.0]
    # y1列表中的第一个值和最后一个值
    b = [y1[0], y1[-1]]
    # print(y1[0])
    # print(y1[-1])
    plt.plot(x, y1, 'r-', linewidth=3, alpha=0.75, label='log1.5(x)')
    plt.plot(x, y2, 'g-', linewidth=3, alpha=0.75, label='log2(x)')
    plt.plot(x, y3, 'y-', linewidth=3, alpha=0.75, label='log3(x)')
    plt.plot(a, b, 'b--')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend(loc='lower right')
    plt.show()
