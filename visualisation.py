import matplotlib.pyplot as plt
import numpy as np
from Neuron import *

class Plot:
    def __normalise_input(self, i: list[Neuron.learning_input]):
        x = []
        y = []
        for li in i:
            x.append(li.x[0][0])
            y.append(li.y)
        return x, y

    def __norm_2(self, i: list[Neuron.learning_input]):
        x = []
        y = []
        for li in i:
            x.append(li.x[0])
            y.append(li.y)
        return x, y


    def __init__(self, i1, i2, orig):
        x, y = self.__normalise_input(i1)
        x1, y1 = self.__normalise_input(i2)
        orig_x, orig_y = self.__norm_2(orig)
        # x.sort()
        # y.sort()
        # print(x)
        # print(y)
        # # print(x1)
        # # print(y1)
        # plt.plot(x, y)
        # plt.show()

        self.fig, (self.ax0, self.ax1, self.ax2) = plt.subplots(nrows=1, ncols=3, figsize = (10, 5))
        self.ax0.set_title('Orig')
        self.ax0.scatter(x=orig_x, y=orig_y)
        self.ax1.set_title('Before')
        self.ax1.scatter(x=x, y=y)
        self.ax2.set_title('After')
        self.ax2.scatter(x=x1, y=y1)



    def print(self):
        plt.show()
