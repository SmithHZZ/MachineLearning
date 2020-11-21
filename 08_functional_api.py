from tensorflow import keras
import pandas as pd
import matplotlib.pyplot as plt

# 函数式API

(train_image, train_label), (test_image, test_label) = keras.datasets.fashion_mnist.load_data()

train_image = train_image / 255.0
test_image = test_image / 255.0

input1 = keras.Input(shape=(28, 28))

# 直接调用该层
x = keras.layers.Flatten()(input1)

# 直接调用该层
x = keras.layers.Dense(32, activation='relu')(x)

x = keras.layers.Dropout(0.5)(x)

x = keras.layers.Dense(64, activation='relu')(x)

output = keras.layers.Dense(10, activation='softmax')(x)

model = keras.Model(input1, output)

model.summary()

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(train_image, train_label, epochs=10)

test_loss, test_acc = model.evaluate(test_image, test_label)

print(test_loss)
print(test_acc)
