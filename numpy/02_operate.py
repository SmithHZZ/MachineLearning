import numpy as np

# 快速产生一个矩阵
a = np.arange(12)
print(a)
a = a.reshape(-1, 2, 2)
print(a)
a = a.reshape(3, 4)
print(a)


# 数组相加 形状一致
b = np.arange(10)
print(b)
c = np.arange(start=10, stop=20)
print(c)
d = b+c
print(d)
print(d/2)
print(d * 2)
print(b ** 2)

# 矩阵（二位数组运算）
e = np.eye(4, 4)*3
print(e)
f = np.eye(4, 4)*2
print(f)
print(e*f)

print(np.matmul(e, f))
print(np.dot(e, f))

# 矩阵转置
print(a)
print(np.transpose(a))
# 求逆矩阵
print(f)
print(np.linalg.inv(f))

# 数组间的运算
print(a)

# 对所有元素求和
print(np.sum(a))
# 行求和
print(np.sum(a, axis=1))
# 列求和
print(np.sum(a, axis=0))

# 求均值
print(np.average(a))

# 求积
print(np.prod(a))

# 求相邻元素的差
print(np.diff(a))

# 各元素的平方根
print(np.sqrt(a))

# 各元素的指数值
print(np.exp(a))

# 各元素的绝对值
print(np.abs(a))

# 数组堆叠，几个低维度组成高维度
x = np.array([1, 2, 3, 4])
y = np.array([2, 3, 4, 5])
print(np.stack((x, y), 0))
print(np.stack((x, y), 1))


