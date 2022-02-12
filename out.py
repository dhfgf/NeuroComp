from Neuron import *
from NeuronWeb import *

x = [1, 1, 1, 1, 1]
a = Neuron(func_1)
neurons = [a, a, a, a, a]
A = FullyConnectedWeb(neurons, 1, x)
print(A.activate())
