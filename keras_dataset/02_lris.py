import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 鸢尾花数据集
data = pd.read_csv('../dataset/iris.csv')

print(data.head())

d = np.array(data)

plt.scatter(d[:, 2], d[:, 3])
plt.show()

