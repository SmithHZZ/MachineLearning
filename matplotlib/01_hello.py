import matplotlib.pyplot as plt

# 创建画布
plt.figure(figsize=(3, 2), facecolor='lightgrey')
# 绘制空白图形
plt.plot()

# 划分子图
plt.subplot(2, 2, 1)
plt.subplot(2, 2, 2)
plt.subplot(2, 2, 3)
plt.subplot(2, 2, 4)

# 设置中文字体
plt.rcParams['font.sans-serif'] = 'SimHei'

plt.suptitle('我是Hello')
plt.tight_layout(rect=[0, 0, 1, 0.9])

plt.show()
