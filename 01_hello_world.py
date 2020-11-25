import tensorflow as tf
import pandas as pd

from sklearn import linear_model

print(tf.__version__)

m1 = tf.constant([[2, 3]])
m2 = tf.constant([[2], [1]])
op = tf.matmul(m1, m2)

print(op.numpy())


state = tf.Variable(9, name='hello')

for _ in range(5):
    new_value = tf.add(state, 1)
    print(new_value.numpy())

# 年龄 年薪 是否有车 案例

x = [[20, 3],
     [23, 7],
     [31, 10],
     [42, 13],
     [50, 7],
     [60, 5]]

y = [0, 1, 1, 1, 0, 0]

# 逻辑回归
lr = linear_model.LogisticRegression()
lr.fit(x, y)

testx = [[28, 8]]

label = lr.predict(testx)

print("predict label :", label)

prob = lr.predict_proba(testx)
print("prob :", prob)

