from copy import *
from Neuron import *


class LayerInfo:
    def __init__(self, func, neuron_count):
        self.func = func
        self.neuron_count = neuron_count


class LayerWeb:
    def __init__(self, input: list, layers_count: int, *layers: LayerInfo):
        self.input = input
        self.layers_count = layers_count
        self.neuron_layers = []  # лист листов со сгенерированными нейронами
        input_len = len(self.input)
        for cur_layer in range(self.layers_count):
            neurons = []
            for i in range(layers[cur_layer].neuron_count):
                neurons.append(Neuron(layers[cur_layer].func, input_len))
            input_len = layers[cur_layer].neuron_count
            self.neuron_layers.append(neurons)

    def activate(self):
        input_prev = copy(self.input)
        for cur_layer in range(self.layers_count):
            output = []
            for i in range(len(self.neuron_layers[cur_layer])):
                output.append(self.neuron_layers[cur_layer][i].activate(input_prev))
            input_prev = output
        return input_prev
