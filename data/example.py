from lightning import Lightning
from numpy import random

lgn = Lightning()

x = random.randn(10)
y = random.randn(10)
mat = random.rand(10,10)
mat[mat>0.75] = 0
group = (random.rand(10) * 5).astype('int')

lgn.graph(x, y, mat, group=group)