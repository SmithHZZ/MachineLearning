import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)
print(tf.test.is_gpu_available())

data = pd.read_csv('dataset/advertising.csv')

# print(data.head())

# 查看三种广告投放对销售的影响
# plt.scatter(data.TV, data.Sales)
# plt.show()
# plt.scatter(data.Radio, data.Sales)
# plt.show()
# plt.scatter(data.Newspaper, data.Sales)
# plt.show()

x = data.iloc[:, 1:-1]
y = data.iloc[:, -1]

model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, input_shape=(3,), activation='relu'),
    tf.keras.layers.Dense(1)
])

model.summary()

model.compile(optimizer='adam', loss='mse')

model.fit(x, y, epochs=5000)

test = data.iloc[:10, 1:-1]

res = model.predict(test)

print(res)

