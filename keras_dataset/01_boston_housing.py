import tensorflow.keras.datasets as ds
import matplotlib.pyplot as plt

# 波士顿房价数据集可视化

(train_x, train_y), (_, _) = ds.boston_housing.load_data()

plt.figure(figsize=(5, 5))
plt.scatter(train_x[:, 5], train_y)
plt.xlabel('RM')
plt.ylabel("Price($1000's)")
plt.title("5. RM-Price")
plt.show()

plt.figure(figsize=(12, 12))
for i in range(13):
    plt.subplot(4, 4, i+1)
    plt.scatter(train_x[:, i], train_y)
plt.show()



