"""
rgw stands for Random Grid World. This module contains
the code necesary to initialize a GridWorld with obstacles 
in random places
"""
import numpy as np
import matplotlib.pyplot as plt
class GridWorld:
    def __init__(self,height:int=10,width:int=10, p:float=0.1) -> None:
        self.height = height
        self.width = width
        self.grid = np.random.choice(a=[0, 1], size=(height, width), p=[1-p, p])
        self.goalRowIndex = np.random.randint(height)
        self.goalColIndex = np.random.randint(width)
        self.grid[self.goalRowIndex][self.goalColIndex] = 2
        return
    def plot(self) -> None:
        plt.imshow(self.grid, cmap='brg',  interpolation='nearest')
        plt.show()
        return
    def print():
        print("hello world")
        return

    