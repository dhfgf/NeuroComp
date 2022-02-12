from Neuron import *
from FullyConnectedWeb import *
from LayerWeb import *

x = [1, 2, 3, 4, 5]

a = Neuron(func_1, 5)
b = Neuron(func_2, 5)
c = Neuron(func_3, 5)
neurons = [a, a, a, a, a]
A = FullyConnectedWeb(neurons, 1, x)

l1 = LayerInfo(func_1, 5)
l2 = LayerInfo(func_1, 4)
l3 = LayerInfo(func_1, 3)
B = LayerWeb(x, 3, l1, l2, l3)
print(B.activate())
