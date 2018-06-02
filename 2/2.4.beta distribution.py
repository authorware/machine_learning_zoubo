from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

if __name__ == '__main__':
    a = [1, 3, 4, 4, 5]
    b = [1, 2, 2, 3, 3]
    c = ['g', 'r', 'b', 'y', 'c']

    x = np.arange(0.1, 1.0, 0.001)
    # print(x)

    mpl.rcParams['font.sans-serif'] = 'SimHei'
    mpl.rcParams['axes.unicode_minus'] = False

    for i in range(len(a)):
        y = stats.beta.pdf(x, a[i], b[i])
        plt.plot(x, y, '%s-' % c[i], linewidth=1, alpha=0.75, label='a=%d,b=%d' % (a[i], b[i]))
    plt.legend(loc='upper left')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(u'Beta分布与参数')
    plt.show()
