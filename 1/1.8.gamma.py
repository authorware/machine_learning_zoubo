#阶乘与Gamma函数的对应关系
#Gamma函数是阶乘在实数域上的推广

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.special import gamma,factorial

if __name__=='__main__':

    N = 5
    x1 = np.linspace(0,N,500)
    #print(x1)
    g = gamma(x1+1)
    x2 = np.arange(0,N+1)
    f = factorial(x2)
    # print(g)
    #print(f)
    plt.plot(x1,g,'r-',linewidth=2,label='Gamma')
    plt.plot(x2,f,'go', linewidth=2,markersize=9)
    plt.legend(loc='upper left')
    mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体,就可正常显示中文
    mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像时，负号'-'显示为方块的问题
    plt.title(u'Gamma函数与阶乘',fontsize=16)
    plt.show()