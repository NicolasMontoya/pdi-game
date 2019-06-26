#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 09:33:41 2019

Esta clase contiene los objetos que aparecen en el transcurso del juego

@author: Edward Nicolas Montoya
@author: Surely Berrio
"""
import numpy as np 

class Object:
    """    
    Constructor de la clase, contiene los parámetros de configuración
    
    @param initialX - Posición en x donde inicia el objeto
    @param finalX - Posición en x donde termina el objeto
    @param initialY - Posición en y donde inicia el objeto
    @param finalY - Posición en y donde termina el objeto
    @param color - Color del objeto
    @param name - Nombre del color del objeto (Sirve para identificación rápida)
    """
    def __init__(self, initialX, finalX, initialY, finalY, color, name):
        self.__initialX = initialX
        self.__finalX = finalX
        self.__initialY = initialY
        self.__finalY = finalY
        self.__color = color
        self.__colorName = name
        
    # Función de movimiento del objeto
    def move(self):
        self.__initialY += 1
        self.__finalY += 1
    
    # Función que devuleve los datos generales del objeto
    def position(self):
        return self.__initialX, self.__finalX, self.__initialY, self.__finalY, self.__color, self.__colorName
    
    """    
    Matrix de posiciones que indica de manera espacial (modo RGB) donde se
    encuentra el objeto
    
    """
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