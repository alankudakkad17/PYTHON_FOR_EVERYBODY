import torch
import torch.nn as nn
from torch import sigmoid
class simple(nn.Module):
    def __init__(self,d_in,h,d_out):
        super(simple,self).__init__()
        self.linear1=nn.Linear(d_in,h)
        self.linear2=nn.Linear(h,d_out)
    def forward(self,x):
        x=self.linear1(x)
        x=sigmoid(x)
        x=self.linear2(x)
        return x
model=simple(3,4,1)
x=torch.randn(5,3)  # batch size=2, input dimension=3
y=model(x)  # forward pass  to get output
print(y)                