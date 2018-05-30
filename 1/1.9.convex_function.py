#凸函数举例

import numpy as np
import matplotlib.pyplot as plt

if __name__=='__main__':

    fig = plt.figure(figsize=(6,10))
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)
    u = np.linspace(0.0,4.0,1000,dtype = np.float)
    x,y = np.meshgrid(u,u)
    # print(np.shape(x))
    # print('-------------')
    # print(y)
    z = np.log(np.exp(x)+np.exp(y))
    ax1.contourf(x, y, z, 80)
    ax2.contourf(x, y, z, 30)
    plt.show()

