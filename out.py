from Neuron import *
from FullyConnectedNeuralNet import *
from LayeredNeuralNet import *

print(Neuron.__doc__)

x = [1, 2, 3, 4, 5]

a = Neuron(q, 5)
b = Neuron('func_2', 5)
c = Neuron('func_4', 5)
neurons = [a, a, a, a, a]
A = FullyConnectedNeuralNet(neurons, 1, x)
print(A.activate())

l1 = LayerInfo('func_1', 5)
l2 = LayerInfo('func_1', 4)
l3 = LayerInfo('func_1', 3)
B = LayeredNeuralNet(x, 3, l1, l2, l3)
print(B.activate())
print(B.activate())
