import torch
from torch.autograd import Variable

# 变量

tensor = torch.FloatTensor([[1, 2], [3, 4]])

variable = Variable(tensor)

t_out = torch.mean(tensor*tensor)  # tensor^2

v_out = torch.mean(variable*variable)

print(t_out)
print(v_out)

