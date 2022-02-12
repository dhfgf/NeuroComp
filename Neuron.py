class Neuron:
    def __init__(self, func):
        self.func = func
        self.w = [1, 1, 1, 1, 1]
        self.b = 0

    def activate(self, x: list):
        return self.func(self.w, x, self.b)


def __sum(w: list, x: list, b):
    s = b
    for i in range(len(w)):
        s += w[i] * x[i]
    return s


# линейная
def func_1(w: list, x: list, b):
    return __sum(w, x, b)


# линейная с насыщением
def func_2(w: list, x: list, b):
    s = __sum(w, x, b)
    if s >= 1:
        return 1
    elif s <= -1:
        return -1
    else:
        return s


# пороговая
def func_3(w: list, x: list, b):
    s = __sum(w, x, b)
    if s < 0:
        return 0
    else:
        return 1
