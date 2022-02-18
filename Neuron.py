import random


class Neuron:
    def __init__(self, func, len):
        """Neuron with specified function and input length

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
                'func_1': self.__func_1,
                'func_2': self.__func_2,
                'func_3': self.__func_3,
            }[func]
        except KeyError:
            return self.__func_1
