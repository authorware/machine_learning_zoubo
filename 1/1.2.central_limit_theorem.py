# Python Code示例2
# 验证中心极限定理
# 附1.3.normal_distribution为官方文档给出的正态函数


import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # 在0到1之间随机生成呈均匀分布的10000个值
    u = np.random.uniform(0.0, 1.0, 10000)
    print(u)
    # hist纵坐标数值为相应的x轴数值取到的次数，如x=0.2取到120次
    # 80为长条数
    plt.hist(u, 80, facecolor='g', alpha=0.75)
    plt.show()

    times = 10000

    for time in range(times):
        u += np.random.uniform(0.0, 1.0, 10000)
    # 将u放缩到0与1之间
    u /= times
    print(u)
    plt.hist(u, 80, facecolor='g', alpha=0.75)
    plt.show()
