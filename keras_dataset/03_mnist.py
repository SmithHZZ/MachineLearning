import tensorflow as tf
import matplotlib.pyplot as plt

(train_image, train_label), (test_image, test_label) = tf.keras.datasets.mnist.load_data()

plt.axis('off')
plt.imshow(train_image[0], cmap='gray')
plt.show()

