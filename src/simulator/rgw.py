"""
rgw stands for Random Grid World. This module contains
the code necesary to initialize a GridWorld with obstacles 
in random places
"""
import numpy as np
import matplotlib.pyplot as plt
class GridWorld:
    def __init__(self,height:int=10,width:int=10,density:float=0.1) -> None:
        self.height = height
        self.width = width
        self.grid = np.random.choice(a=[False, True], size=(height, width), p=[density, 1-density])
        return
    def plot