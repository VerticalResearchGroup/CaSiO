import torch

from utils import params
from utils.torch_wrapper import benchmark_wrapper2

from .model import *

device = torch.device(params.devname)
net = Dlrm()
net.to(params.dtype_torch).to(device)

dense_x = torch.randn(params.bs, 13, device=device, dtype=params.dtype_torch)
sparse_x = torch.randint(0, 1, (params.bs, 26), device=device)
opt = torch.optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

def roi():
    opt.zero_grad()
    yp = net(dense_x, sparse_x)
    loss = torch.sum(yp)
    loss.backward()
    opt.step()

benchmark_wrapper2(roi)
