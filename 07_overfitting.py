import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

'''
过拟合
    在训练数据上的分很高，在测试数据上得分很低
    抑制过拟合手段
      dropout
      正则化
      图像增强
      最好方法是增加训练数据
      
欠拟合
    在训练数据上得分比较低，在测试数据上得分相对较低
    
'''

(train_image, train_label), (test_image, test_label) = tf.keras.datasets.fashion_mnist.load_data()

plt.imshow(train_image[0])
plt.show()

model = tf.keras.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(128, activation='relu'))
# 添加dropout层
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(128, activation='relu'))
# 添加dropout层
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(128, activation='relu'))
# 添加dropout层
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(10, activation='softmax'))

model.summary()

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss='sparse_categorical_crossentropy', metrics=['acc'])

history = model.fit(train_image, train_label, epochs=10, validation_data=(test_image, test_label))

plt.plot(history.epoch, history.history.get('loss'), label='loss')
plt.plot(history.epoch, history.history.get('val_loss'), label='val_loss')
plt.legend()

plt.show()

plt.plot(history.epoch, history.history.get('acc'), label='acc')
plt.plot(history.epoch, history.history.get('val_acc'), label='val_acc')
plt.legend()

plt.show()


