import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

(train_image, train_label), (test_image, test_label) = tf.keras.datasets.fashion_mnist.load_data()

print(train_image.shape)
print(train_label.shape)

print(test_image.shape)
print(test_label.shape)

# plt.imshow(train_image[0])
# plt.show()

print(np.max(train_image[0]))
print(train_label[0])

train_image = train_image/255
test_image = test_image/255

model = tf.keras.Sequential()
# 添加Flatten层将数据变为一维的
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))

model.summary()

# 使用独热编码
train_label_onehot = tf.keras.utils.to_categorical(train_label)

# model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
# 使用优化器实例
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.01))

model.fit(train_image, train_label_onehot, epochs=10)

res = model.predict(test_image)

print(res.shape)

print(res[0])

print(np.argmax(res[0]))

print(test_label[0])

# 独热编码结束

# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['acc'])

# model.fit(train_image, train_label, epochs=10)

# model.evaluate(test_image, test_label)


