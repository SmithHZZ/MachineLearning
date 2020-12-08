import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.utils.data as data
import torchvision
import matplotlib.pyplot as plt

# hyper parameter
EPOCH = 100
BATCH_SIZE = 50
LR = 0.001
DOWNLOAD_MNIST = False

train_data = torchvision.datasets.MNIST(
    root='./mnist',
    train=True,
    transform=torchvision.transforms.ToTensor(),
    download=DOWNLOAD_MNIST
)

print(train_data.data.size())
print(train_data.targets.size())

plt.imshow(train_data.data[0].numpy(), cmap='gray')
plt.title('%i' % train_data.targets[0])
plt.show()


