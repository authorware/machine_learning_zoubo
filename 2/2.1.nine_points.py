# 9点分布

import numpy as np
import matplotlib.pyplot as plt


def func(x):
    while x > 10:
        x /= 10
    return int(x)


if __name__ == '__main__':

    N = 100
    m = 1
    f = [0]*9  # 初始化列表 9个数 0-8
    x = np.arange(1, 10)
    # print(x)
    for i in range(1, N+1):
        m *= i
        n = func(m)
        f[n-1] += 1   # 保存到列表顺序为0-8
    # print(f)
    plt.plot(x, f, 'r-', linewidth=3, alpha=0.5)
    plt.plot(x, f, 'go', markersize=8)
    plt.grid(True)
    plt.show()

