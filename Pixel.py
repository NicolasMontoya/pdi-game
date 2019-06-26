#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 09:03:39 2019

@author: nicolas
"""
from Color import Color

class Pixel:
    def __init__(self, width = 10, heigth = 10):
        self.__width = width
        self.__heigth = heigth
        self.color = Color.getWhite(width, heigth)
    @property
    def width(self):
        return self.__width
    @property
    def heigth(self):
        return self.__heigth
    def setRandomColor(self):
        self.color = Color.getRandom(self.width, self.heigth)
