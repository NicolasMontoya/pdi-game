#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 09:33:41 2019

@author: nicolas
"""

import numpy as np

class Board:
    
    def __init__(self, widthBoard, heigthBoard, name = 'Board'):
        self.__widthBoard = widthBoard
        self.__heigthBoard = heigthBoard
        self._windowName = name
        self.__pixels = np.array([[[255 for z in range(3)] for x in range(10*widthBoard)] for y in range(10*heigthBoard)], dtype="uint8")
        self.__pixels[730:740,:,:] = np.array([[[0 for z in range(3)] for x in range(10*120)] for y in range(10)], dtype="uint8")
    @property
    def width(self):
        return self.__widthBoard
    
    @property
    def heigth(self):
        return self.__heigthBoard
    
    @property
    def pixels(self):
        return self.__pixels
    
    def setPixel(self, x, y):
        self.pixels[x][y].setRandomColor()

