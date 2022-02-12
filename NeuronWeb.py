from copy import *
from Neuron import *


class FullyConnectedWeb:
    def __init__(self, neurons: list[Neuron], cycles_count, input: list):
        self.neurons = neurons
        self.cycles_count = cycles_count
        self.input = input

    def activate(self):
        for i in range(self.cycles_count):
            new_input = copy(self.input)
            for j in range(len(self.neurons)):
                new_input[j] = self.neurons[j].activate(self.input)
            self.input = new_input
        return self.input