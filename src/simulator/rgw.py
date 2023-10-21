"""
rgw stands for Random Grid World. This module contains
the code necesary to initialize a GridWorld with obstacles 
in random places
"""
import numpy as np
from scipy import sparse
class GridWorld:
    def __init__(self,height:int=10,width:int=10,density:float=0.1) -> None:
        self.height = height
        self.width = width


        # Init Random Grid With FAST Code stolen from
        # https://stackoverflow.com/questions/43528637/create-large-random-boolean-matrix-with-numpy
        
        return