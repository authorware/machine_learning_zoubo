import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

# 数据
mu = 100  # mean of distribution
sigma = 15  # standard deviation of distribution
# np.random.randn(10000)随机生成在(0,1)之间呈正态分布的10000个数
# 为了更好的呈现效果，x加入了均值和标准差偏移
x = mu + sigma * np.random.randn(10000)
print(x)

num_bins = 50
# the histogram of the data
n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='blue', alpha=0.5)

# add a 'best fit' line
y = mlab.normpdf(bins, mu, sigma)
plt.plot(bins, y, 'r--')
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()
