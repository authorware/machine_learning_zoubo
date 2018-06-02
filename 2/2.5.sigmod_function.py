import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

if __name__ == "__main__":
    x = np.arange(-6, 6, 0.1)
    print(x)
    y = 1 / (np.exp(-x)+1)
    print(y)
    plt.plot(x, y, 'r-', linewidth=3, alpha=0.75, label='sigmod')
    plt.plot([0, 0], [-0.1, 1], 'k-',  linewidth=1)
    plt.plot([-6, 6], [0, 0], 'k-', linewidth=1)
    mpl.rcParams['font.sans-serif'] = 'SimHei'
    mpl.rcParams['axes.unicode_minus'] = False
    plt.legend(loc='upper left')
    plt.title(u'Sigmod函数')
    plt.grid(True)
    plt.show()
