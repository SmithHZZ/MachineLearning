import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

# 散点图
plt.scatter([1, 2, 3], [1, 2, 3])

plt.show()

n = 1024
# 正态分布
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
# 均匀分布
x1 = np.random.uniform(-4, 4, (1, n))
y1 = np.random.uniform(-4, 4, (1, n))

# 散点图
plt.scatter(x, y, color='blue', marker='*', label='正态分布')
plt.scatter(x1, y1, color='red', marker='o', label='均匀分布')

plt.legend()

plt.title('标准正态分布', fontsize=20)

plt.text(2.5, 2.5, '均值： 0\n标准差：1')

plt.show()



