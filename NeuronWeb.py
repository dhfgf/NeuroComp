from copy import *
from Neuron import *


class FullyConnectedWeb:
    def __init__(self, neurons: list[Neuron], cycles_count, input: list):
        self.neurons = neurons
        self.cycles_count = cycles_count
        self.input = input

    def activate(self):
        for i in range(self.cycles_count):
            # new_input = copy(self.input)
            new_input = self.input
            for j in range(len(self.neurons)):
                new_input[j] = self.neurons[j].activate(self.input)
            self.input = new_input
        return self.input


class LayerInfo:
    def __init__(self, func, neuron_count):
        self.func = func
        self.neuron_count = neuron_count


class LayerWeb:
    class Layer:
        def __init__(self, func, count):
            self.func = func
            self.count = count

    def __init__(self, input: list, layers_count: int, *layers: LayerInfo):
        self.input = input
        self.layers_count = layers_count
        self.layers = layers

    def activate(self):
        input_len = len(self.input)
        input_prev = copy(self.input)
        for cur_layer in range(self.layers_count):
            neurons = []
            output = []
            for i in range(self.layers[cur_layer].neuron_count):
                neurons.append(Neuron(self.layers[cur_layer].func, input_len))
                output.append(neurons[i].activate(input_prev))
            input_len = self.layers[cur_layer].neuron_count
            input_prev = output
        return input_prev

