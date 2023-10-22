"""
This module contains code necesary to initialize GridWorld with obstacles in random locations.
"""
import numpy as np
import matplotlib.pyplot as plt
from copy import copy
from matplotlib.colors import ListedColormap
from enum import Enum

class ActionSpace(Enum):
    left = 1
    right = 2
    up = 3
    down = 4
    idle = 5

class RandomGridWorld():
    def __init__(self,height:int=25,width:int=25, p:float=0.1) -> None:
        """
        Init a random grid world. 

        RandomGridWorld.grid literal defintions:
        0 -> empty state
        1 -> occupied state
        2 -> goal state
        3 -> agent position
        """
        self.width = width
        self.height = height 
        self.ic = (np.floor_divide(height,2),np.floor_divide(width,2))
        self.agentPosition = self.ic
        self.terminateFlag = False
        self.cumulativeReturn = 0
        # Populate Grid
        self.grid = np.random.choice(a=[0, 1], size=(height, width), p=[1-p, p])
        goalState = (np.random.randint(height),np.random.randint(width)) # Indeces that store location of goal
        self.goalState = goalState
        return
    
    def plot(self) -> None:
        cmap = ListedColormap(["gainsboro", "crimson", "forestgreen", "darkorchid"])
        grid = copy(self.grid)
        grid[self.agentPosition] = 3
        grid[self.goalState] = 2
        plt.imshow(grid,cmap=cmap)
        plt.axis('off')
        plt.show()
        return
    
    def step(self,action: ActionSpace) -> None:
        match action:
            case ActionSpace.left:
                self.__moveLeft()
            case ActionSpace.right:
                self.__moveRight()
            case ActionSpace.up:
                self.__moveUp()
            case ActionSpace.down:
                self.__moveDown()
            case ActionSpace.idle:
                self.__idle()
        return

    
    def __idle(self) -> None:
        self.__updatePosition(newAgentPosition=self.agentPosition)
        return
    
    def __moveLeft(self) -> None:
        pos = self.agentPosition
        newAgentPosition = (pos[0],pos[1] - 1)
        self.__updatePosition(newAgentPosition)
        return
    
    def __moveRight(self) -> None:
        pos = self.agentPosition
        newAgentPosition = (pos[0],pos[1] + 1)
        self.__updatePosition(newAgentPosition)
        return
    
    def __moveUp(self) -> None:
        pos = self.agentPosition
        newAgentPosition = (pos[0] - 1, pos[1])
        self.__updatePosition(newAgentPosition)
        return
    
    def __moveDown(self) -> None:
        pos = self.agentPosition
        newAgentPosition = (pos[0] + 1, pos[1])
        self.__updatePosition(newAgentPosition)
        return
    
    def __updatePosition(self,newAgentPosition):
        if self.__isPositionOutOfBounds(newAgentPosition):
            self.idle()
            reward = 0 # Reward here is zero because `idle()` collects the appropriate reward when it calls `_updatePosition()` 
        elif self.__isPositionOccupied(newAgentPosition):
            print("Ouch! D:")
            self.agentPosition = newAgentPosition
            self.terminateFlag = True
            reward = -10
        elif self._isPositionGoalState(newAgentPosition):
            print("GOLAZO! :D")
            self.agentPosition = newAgentPosition
            self.terminateFlag = True
            reward = 100
        else:
            self.agentPosition = newAgentPosition
            reward = -1
        self.cumulativeReturn += reward
        return
    
    def __isPositionOutOfBounds(self,position) -> bool:
        """
        Returns true if position is out of bounds Or In Occupied Grid. Position is given by row index, followed by column index
        """
        isValidPosition = False
        rowIndex = position[0]
        colIndex = position[1]
        if rowIndex < 0 or colIndex < 0:
            isValidPosition = True
        if rowIndex >= self.height or colIndex >= self.width:
            isValidPosition = True
        return isValidPosition
    
    def __isPositionOccupied(self,position) -> bool:
        if self.grid[position] == 1:
            return True
        else:
            return False
    
    def _isPositionGoalState(self,position) -> bool:
        if position == self.goalState:
            return True
        else:
            return False