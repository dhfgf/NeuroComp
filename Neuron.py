import random
from math import exp


class Neuron:
    def __init__(self, func, len):
        """Creates neuron with specified function and input length

        Parameters:
            func (str): neuron function type
                'func_1' - linear
                'func_2' - linear with saturation
                'func_3' - threshold
            len (int): length of input array
        """
        self.func = self.__get_func(func)
        self.weights = []
        for i in range(len):
            self.weights.append(random.uniform(1, 2))
        self.bias = random.uniform(1, 2)
        self.len = len

    def activate(self, x: list):
        if len(x) != self.len:
            raise ValueError('Длины не совпадают')

        return self.func(self.weights, x, self.bias)




\ь
    class learning_input:
        def __init__(self, learning_input: list):
            self.x = learning_input[0: len(learning_input) - 1]
            self.y = learning_input[len(learning_input) - 1]



    def __func_o(self, weights, x, bias):
        return 1 / (1 + exp(-(self.__sum(weights, x, bias) - bias)))

    def o(self, i: learning_input):
        return 1 / (1 + exp(-(self.__sum(self.weights, i.x, self.bias) - self.bias)))

    def __change_weights(self, ETA, learning_inputs: list[learning_input]):
        for i in learning_inputs:
            o = self.o(i)
            for j in range(len(self.weights)):
                self.weights[j] += ETA * (i.y - o) * o * (1 - o) * i.x[j]

    def calculate_sum_error(self, learning_inputs: list[learning_input]):
        E = 0
        for i in learning_inputs:
            o = self.o(i)
            E += 1/2 * (i.y - o) * (i.y - o)
        #     print(o, i.y)
        # print('\n\n\n')
        return E

    def learn(self, ETA, cycles, accuracy, learning_inputs: list[learning_input]):
        for i in range(cycles):
            E = self.calculate_sum_error(learning_inputs)
            # print(E)
            if E < accuracy:
                break
            self.__change_weights(ETA, learning_inputs)
            # print(self.weights)





    def __sum(self, weights: list, x: list, bias):
        sum = bias
        for i in range(len(weights)):
            sum += weights[i] * x[i]
        return sum

    # линейная
    def __func_1(self, weights: list, x: list, bias):
        return self.__sum(weights, x, bias)

    # линейная с насыщением
    def __func_2(self, weights: list, x: list, bias):
        s = self.__sum(weights, x, bias)
        if s >= 1:
            return 1
        elif s <= -1:
            return -1
        else:
            return s

    # пороговая
    def __func_3(self, weights: list, x: list, bias):
        s = self.__sum(weights, x, bias)
        if s < 0:
            return 0
        else:
            return 1

    def __get_func(self, func: str):
        try:
            return {
                'o': self.__func_o,
                'func_1': self.__func_1,
                'func_2': self.__func_2,
                'func_3': self.__func_3,
            }[func]
        except KeyError:
            return self.__func_1
