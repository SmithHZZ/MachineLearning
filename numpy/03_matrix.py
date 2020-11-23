import numpy as np

# 矩阵对象
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.mat(a)
c = np.mat(a)
print(type(a))
print(type(b))
print(b)

# 基本的矩阵运算
# 乘法
print(b*c)

# 求逆矩阵
d = np.eye(4)*4
e = np.mat(d)
print(e.I)

# 矩阵转置
print(e.A)

# 打乱序列(每行元素)
np.random.shuffle(d)
print(d)

