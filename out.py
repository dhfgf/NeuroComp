from Neuron import *
from NeuronWeb import *

x = [1, 2, 3, 4, 5]

a = Neuron(func_1, 5)
b = Neuron(func_2, 5)
c = Neuron(func_3, 5)

neurons = [a, a, a, a, a]
A = FullyConnectedWeb(neurons, 1, x)
print(A.activate())
