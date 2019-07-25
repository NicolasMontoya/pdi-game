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
    # Genera un arreglo que presenta una capa de color con sus elementos 255
    @staticmethod
    def fullChannel(x, y):
        return np.array(([[255 for x in range(x)] for y in range(y)]), dtype = "uint8")
    # Genera un arreglo que presenta una capa de color con sus elementos 0
    @staticmethod
    def emptyChannel(x, y):
        return np.zeros((x,y), dtype = "uint8")
    # Genera un arreglo que presenta el color azul
    @staticmethod
    def getBlue(x, y):
        return np.dstack((Color.fullChannel(x, y), Color.emptyChannel(x,y), Color.emptyChannel(x,y)))
    # Genera un arreglo que presenta el color rojo
    @staticmethod
    def getRed(x, y):
        return np.dstack((Color.emptyChannel(x,y), Color.emptyChannel(x,y), Color.fullChannel(x, y)))
    # Genera un arreglo que presenta el color verde
    @staticmethod
    def getGreen(x, y):
        return np.dstack((Color.emptyChannel(x,y), Color.fullChannel(x, y), Color.emptyChannel(x,y)))
    # Genera un arreglo que presenta un color definido por el usuario
    @staticmethod
    def getCustomColor(blueChannel, greenChannel, redChannel):
        return np.dstack((blueChannel, greenChannel, redChannel))
    # Genera un arreglo que presenta el color negro
    @staticmethod
    def getBlack(x,y):
        return np.zeros((x, y, 3), dtype="uint8")
    # Genera un arreglo que presenta el color blanco
    def getWhite(x,y):
        return np.dstack((Color.fullChannel(x,y), Color.fullChannel(x, y), Color.fullChannel(x,y)))
    # Genera un arreglo que presenta un color aleatorio
    @staticmethod
    def getRandom(x, y):
        randomInt = np.random.randint(3)
        if randomInt == 0:
            return Color.getBlue(x, y)
        elif randomInt == 1:
            return Color.getGreen(x, y)
        else:
            return Color.getRed(x, y)