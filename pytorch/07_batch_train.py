import torch
from torch.autograd import Variable
import torch.utils.data as data
import matplotlib.pyplot as plt

# 批训练

BATCH_SIZE = 5

# 必须加这句话要不会报错，因为下面指定了两个线程
if __name__ == '__main__':

    x = torch.linspace(1, 10, 10)
    y = torch.linspace(10, 1, 10)

    torch_dataset = data.TensorDataset(x, y)

    loader = data.DataLoader(
        dataset=torch_dataset,
        batch_size=BATCH_SIZE,
        shuffle=True,
        num_workers=2
    )

    for epoch in range(3):
        for step, (batch_x, batch_y) in enumerate(loader):
            print('Epoch: ', epoch, '| Step:', step, '| batch x:',
                  batch_x.numpy(), '| batch y:', batch_y.numpy())



