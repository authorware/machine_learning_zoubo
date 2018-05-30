#Gini系数、熵、分类误差率三者之间的关系


import numpy as np
import matplotlib.pyplot as plt


if __name__=='__main__':

    x = np.arange(0.001,1.0,0.001,dtype=np.float)
    gini = 2*x*(1-x)
    h = -(x*np.log2(x)+(1-x)*np.log2(1-x))/2
    err = 1 - np.max(np.vstack((x,1-x)),axis=0)
    plt.plot(x,gini,'r-',linewidth=2,label='Gini')
    plt.plot(x,h,'g-', linewidth=2, label='Entropy')
    plt.plot(x, err, 'b--', linewidth=2, label='Error')
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.show()