# -*- coding: utf-8 -*-

import numpy as np 

class Object:
    def __init__(self, initialX, finalX, initialY, finalY, color, name):
        self.__initialX = initialX
        self.__finalX = finalX
        self.__initialY = initialY
        self.__finalY = finalY
        self.__color = color
        self.__colorName = name
    def move(self):
        self.__initialY += 1
        self.__finalY += 1
    def position(self):
        return self.__initialX, self.__finalX, self.__initialY, self.__finalY, self.__color, self.__colorName
    
    @property
    def matrix(self):
        return self.__matrix
    def genMatrix(self):
        partialMatrix = self.__color
        flag = False
        limitY = ((self.__finalY - self.__initialY)/10)
        limitX = ((self.__finalX - self.__initialX)/10)
        for y in range(int(limitY)):
            for x in range(int(limitX-1)):
                partialMatrix = np.concatenate((partialMatrix, self.__color), axis=0)
            if flag is False:
                matrix = partialMatrix
                partialMatrix = self.__color
                flag = True
            else:
                matrix = np.concatenate((matrix, partialMatrix), axis=1)
                partialMatrix = self.__color
        self.__matrix = matrix