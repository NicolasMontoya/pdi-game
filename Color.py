#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 09:03:25 2019

Clase de utilizada que genera los colores básicos del juego

@author: Edward Nicolas Montoya
@author: Surely Berrio
"""
import numpy as np

class Color:
    
    @staticmethod
    def fullChannel(x, y):
        return np.array(([[255 for x in range(x)] for y in range(y)]), dtype = "uint8")
    @staticmethod
    def emptyChannel(x, y):
        return np.zeros((x,y), dtype = "uint8")
    @staticmethod
    def getBlue(x, y):
        return np.dstack((Color.fullChannel(x, y), Color.emptyChannel(x,y), Color.emptyChannel(x,y)))
    @staticmethod
    def getRed(x, y):
        return np.dstack((Color.emptyChannel(x,y), Color.emptyChannel(x,y), Color.fullChannel(x, y)))
    @staticmethod
    def getGreen(x, y):
        return np.dstack((Color.emptyChannel(x,y), Color.fullChannel(x, y), Color.emptyChannel(x,y)))
    @staticmethod
    def getCustomColor(blueChannel, greenChannel, redChannel):
        return np.dstack((blueChannel, greenChannel, redChannel))
    @staticmethod
    def getBlack(x,y):
        return np.zeros((x, y, 3), dtype="uint8")
    def getWhite(x,y):
        return np.dstack((Color.fullChannel(x,y), Color.fullChannel(x, y), Color.fullChannel(x,y)))
    @staticmethod
    def getRandom(x, y):
        randomInt = np.random.randint(3)
        if randomInt == 0:
            return Color.getBlue(x, y)
        elif randomInt == 1:
            return Color.getGreen(x, y)
        else:
            return Color.getRed(x, y)