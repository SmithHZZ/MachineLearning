import matplotlib.pyplot as plt
import numpy as np

n = 24
y1 = np.random.randint(27, 37, n)
y2 = np.random.randint(40, 60, n)

plt.plot(y1, label='温度')
plt.plot(y2, label='湿度')

plt.show()

plt.bar(range(len(y1)), y1, width=0.8, label='温度', facecolor='blue', edgecolor='white')
plt.bar(range(len(y2)), y2*(-1), width=0.8, label='湿度', facecolor='green', edgecolor='white')

plt.show()

