import tensorflow as tf
import pandas as pd

print(tf.__version__)

m1 = tf.constant([[2, 3]])
m2 = tf.constant([[2], [1]])
op = tf.matmul(m1, m2)

print(op.numpy())


state = tf.Variable(9, name='hello')

for _ in range(5):
    new_value = tf.add(state, 1)
    print(new_value.numpy())
