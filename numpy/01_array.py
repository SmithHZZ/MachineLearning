import numpy as np

# 创建数组

# 一维数组
a = np.array([1, 2, 3, 4])
print(a)
print(a.shape)

# 二维数组
b = np.array([[1, 2, 3, 4], [2, 3, 4, 5]])
print(b)
print(b.shape)

# 三维数组
c = np.array([[[1, 2, 3, 4], [2, 3, 4, 5]], [[1, 2, 3, 4], [2, 3, 4, 5]]])
print(c)
print(c.shape)

# 创建时指定数组类型
d = np.array([1, 2, 4, 5], dtype=np.int64)
print(d)
print(d.dtype)
print(d.itemsize)

# 特殊的数组创建

# 全0的数组
e = np.zeros((2, 3))
print(e)

# 序列
f = np.arange(0, 100, 10)
print(f)

# 单位矩阵
g = np.eye(4)
print(g)

# 等差数列
h = np.linspace(1, 50, num=50)
print(h)

# 等比数列
i = np.logspace(1, 5, 5, base=2)
print(i)

