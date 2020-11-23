from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = Image.open('../images/lena_color.tiff')

plt.imshow(img)

plt.show()

print(img.format)
print(img.size)
print(img.mode)

# 图像色彩模式转换
img_gray = img.convert('L')
plt.imshow(img_gray, cmap='gray')
plt.show()

# 分割颜色通道
img_r, img_g, img_b = img.split()
plt.subplot(131)
plt.imshow(img_r, cmap='gray')
plt.subplot(132)
plt.imshow(img_g, cmap='gray')
plt.subplot(133)
plt.imshow(img_b, cmap='gray')

plt.show()

# 转换为数组
data = np.array(img)

# print(data)
print(data.shape)

# 图像缩放
img_resize = img.resize((64, 64))
plt.imshow(img_resize)
plt.show()

# 对图像的原地操作
# img.thumbnail((64, 64))

# 图像旋转
img_rot = img.transpose(Image.ROTATE_90)
plt.imshow(img_rot)
plt.show()

# 截取图像某部分
img_crop = img.crop((100, 100, 400, 400))
plt.imshow(img_crop)
plt.show()

