# Python Code 示例1


import math
import matplotlib.pyplot as plt


if __name__ == '__main__':

    # 注意x的范围，也就是i不能从1开始取
    x = [float(i)/100 for i in range(1, 300)]
    # print(x)
    # 以2为底的log图像
    y = [math.log(i, 2) for i in x]
    # print(y)
    # 两个点确定一条直线
    # 两个点各取x,y列表中的第20和第175个数
    # a为x值，b为y值
    a = [x[20], x[175]]
    b = [y[20], y[175]]

    plt.plot(x, y, 'r-', linewidth=3, label='log curve')
    plt.plot(a, b, 'g-', linewidth=2, label='secant line')
    # 突出显示两个点
    plt.plot(a, b, 'b*', markersize=15, alpha=0.75)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.show()
