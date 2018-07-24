# 自己写着玩的
# 基于Taylor公式中，e的麦克劳林公式，算出一个值
# 后与numpy中的e比较


import numpy as np


def calc_n(n):
    if n > 1:
        return calc_n(n-1)*n
    else:
        return 1


def calc_e(x):
    sum = 0
    for i in x:
        sum += 1/calc_n(i)
    return sum


if __name__ == '__main__':

    x = [i for i in range(0, 10)]
    e_cal = calc_e(x)
    # print(calc_n(4))
    print(e_cal)
    print(np.e)
