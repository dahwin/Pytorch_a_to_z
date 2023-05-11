import torch

# create two matrices
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])

# compute the element-wise product of a and b
c = torch.einsum('ij,ij->ij', a, b)
print(c)