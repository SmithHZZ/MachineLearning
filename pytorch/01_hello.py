import torch
import numpy as np

# pytorch版本
print(torch.__version__)
# cuda设备
print(torch.cuda.device(0))
# cuda设备个数
print(torch.cuda.device_count())
# cuda设备名称
print(torch.cuda.get_device_name(0))
# cuda是否可用
print(torch.cuda.is_available())


# np数据
np_data = np.arange(6).reshape((2, 3))
# np数据转为torch数据
torch_data = torch.from_numpy(np_data)
# torch数据转为np数据
torch2np = torch_data.numpy()

print(
    '\n numpy_data', np_data,
    '\n torch_data', torch_data,
    '\n torch2numpy', torch2np
)

# abs
data = [-1, -2, 1, 2]

# 转为32位浮点数
tensor1 = torch.FloatTensor(data)

print(
    '\n sin',
    '\n numpy ', np.sin(data),
    '\n torch ', torch.sin(tensor1)
)

data2 = [[1, 2], [3, 4]]
tensor2 = torch.FloatTensor(data2)

print(
    '\n numpy ', np.matmul(data2, data2),
    '\n torch ', torch.mm(tensor2,tensor2)

)



