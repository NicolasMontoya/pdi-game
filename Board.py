#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 09:33:41 2019

Esta clase contiene el tablero de juego y los labels definidos para identificar
el estado del juego

@author: Edward Nicolas Montoya
@author: Surely Berrio
"""
from Object import Object
from Color import Color
import numpy as np

class Board:
    # Variable para correr los label
    generalOffset = 80
    """    
    Constructor de la clase, contiene los parámetros de configuración
    
    @param widthBoard - Ancho del tablero de juego
    @param heigthBoard - Alto del tablero de juego
    @param name - Nombre de la board
    """
    def __init__(self, widthBoard, heigthBoard, name = 'Board'):
        self.__widthBoard = widthBoard
        self.__heigthBoard = heigthBoard
        self._windowName = name
        self.__pixels = np.array([[[255 for z in range(3)] for x in range(10*widthBoard)] for y in range(10*heigthBoard)], dtype="uint8")
        self.printLabel()
    """    
    Imprime los label de SCORE en la pantalla
    
    """   
    def printLabel(self):
        # Pixeles impresos en el Board que representan la letra S
        self.__pixels[10:20,880+self.generalOffset:920+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
        self.__pixels[10:30,880+self.generalOffset:890+self.generalOffset, :] = np.zeros((20,10,3), dtype="uint8")
        self.__pixels[30:40,880+self.generalOffset:920+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
        self.__pixels[40:60,910+self.generalOffset:920+self.generalOffset, :] = np.zeros((20,10,3), dtype="uint8")
        self.__pixels[50:60,880+self.generalOffset:920+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
        # Pixeles impresos en el Board que representan la letra C
        self.__pixels[10:20,930+self.generalOffset:970+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
        self.__pixels[10:60,930+self.generalOffset:940+self.generalOffset, :] = np.zeros((50,10,3), dtype="uint8")
        self.__pixels[50:60,930+self.generalOffset:970+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
        # Pixeles impresos en el Board que representan la letra O
        self.__pixels[10:20,980+self.generalOffset:1020+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
        self.__pixels[10:60,980+self.generalOffset:990+self.generalOffset, :] = np.zeros((50,10,3), dtype="uint8")
        self.__pixels[50:60,980+self.generalOffset:1020+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
        self.__pixels[10:60,1010+self.generalOffset:1020+self.generalOffset, :] = np.zeros((50,10,3), dtype="uint8")
        # Pixeles impresos en el Board que representan la letra R
        self.__pixels[10:20,1030+self.generalOffset:1070+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
        self.__pixels[10:60,1030+self.generalOffset:1040+self.generalOffset, :] = np.zeros((50,10,3), dtype="uint8")
        self.__pixels[30:40,1030+self.generalOffset:1070+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
        self.__pixels[10:40,1060+self.generalOffset:1070+self.generalOffset, :] = np.zeros((30,10,3), dtype="uint8")
        self.__pixels[40:60,1050+self.generalOffset:1060+self.generalOffset, :] = np.zeros((20,10,3), dtype="uint8")
        # Pixeles impresos en el Board que representan la letra E
        self.__pixels[10:20,1080+self.generalOffset:1120+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
        self.__pixels[10:60,1080+self.generalOffset:1090+self.generalOffset, :] = np.zeros((50,10,3), dtype="uint8")
        self.__pixels[30:40,1080+self.generalOffset:1120+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
        self.__pixels[50:60,1080+self.generalOffset:1120+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
        # Pixeles impresos en el Board que representan el simbolo :
        self.__pixels[20:30,1130+self.generalOffset:1140+self.generalOffset, :] = np.zeros((10,10,3), dtype="uint8")
        self.__pixels[40:50,1130+self.generalOffset:1140+self.generalOffset, :] = np.zeros((10,10,3), dtype="uint8")
        
        # Pixeles impresos en el Board que representan el simbolo :
        self.__pixels[730:740,0:1350, :] = np.zeros((10,1350,3), dtype="uint8")
    
        # Panel inicial con los colores que indican la dirección para obtener puntos
        obj = Object(1000,1080,100,140,Color.getBlue(10,10),"BLUE")
        obj.genMatrix()
        obj2 = Object(1000,1080,100,140,Color.getGreen(10,10),"GREEN")
        obj2.genMatrix()
        obj3 = Object(1000,1040,100,200,Color.getRed(10,10),"RED")
        obj3.genMatrix()
        self.__pixels[150:230, 1050:1090, :] = obj.matrix
        self.__pixels[150:230, 1250:1290, :] = obj2.matrix
        self.__pixels[100:140, 1120:1220, :] = obj3.matrix
    
    """    
    Imprime la puntuación, esta configurado a dos digitos
    
    @param ref - variable referencia (matriz de datos)
    @param score - puntuación actual del jugador
    """
    def printScore(self, ref, score):
        number = score
        if (number > 9):
            digit = int(number / 10)
            ref = self.printNumber(ref, digit)
            number = score % 10
        ref = self.printNumber(ref, number, 50)
        return ref
    """    
    Imprime los labels de la puntuación (configurado con offset para numeros de dos cifras)
    
    @param pixels - matrix de referencia
    @param digit - digito a imprimir
    @offset - espaciado para trasladar el numero
    """
    def printNumber(self, pixels, digit, offset = 0):
        # Imprime el digito 0
        if digit == 0:
            pixels[10:20,1150+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
            pixels[10:60,1150+offset+self.generalOffset:1160+offset+self.generalOffset, :] = np.zeros((50,10,3), dtype="uint8")
            pixels[50:60,1150+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
            pixels[10:60,1180+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((50,10,3), dtype="uint8")
            # Imprime el digito 1
        elif digit == 1:
            pixels[10:60,1180+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((50,10,3), dtype="uint8")
            # Imprime el digito 2
        elif digit == 2:
            pixels[10:20,1150+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
            pixels[10:30,1180+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((20,10,3), dtype="uint8")
            pixels[30:40,1150+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
            pixels[40:60,1150+offset+self.generalOffset:1160+offset+self.generalOffset, :] = np.zeros((20,10,3), dtype="uint8")
            pixels[50:60,1150+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
            # Imprime el digito 3
        elif digit == 3:
            pixels[10:20,1150+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
            pixels[10:30,1180+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((20,10,3), dtype="uint8")
            pixels[30:40,1150+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
            pixels[40:60,1180+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((20,10,3), dtype="uint8")
            pixels[50:60,1150+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
            # Imprime el digito 4
        elif digit == 4:
            pixels[10:60,1180+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((50,10,3), dtype="uint8")
            pixels[30:40,1150+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
            pixels[10:30,1150+offset+self.generalOffset:1160+offset+self.generalOffset, :] = np.zeros((20,10,3), dtype="uint8")
            # Imprime el digito 5
        elif digit == 5:
            pixels[10:20,1150+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
            pixels[10:30,1150+offset+self.generalOffset:1160+offset+self.generalOffset, :] = np.zeros((20,10,3), dtype="uint8")
            pixels[30:40,1150+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
            pixels[40:60,1180+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((20,10,3), dtype="uint8")
            pixels[50:60,1150+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
            # Imprime el digito 6
        elif digit == 6:
            pixels[10:60,1150+offset+self.generalOffset:1160+offset+self.generalOffset, :] = np.zeros((50,10,3), dtype="uint8")
            pixels[30:40,1150+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
            pixels[50:60,1150+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
            pixels[30:60,1180+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((30,10,3), dtype="uint8")
            # Imprime el digito 7
        elif digit == 7:
            pixels[10:60,1180+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((50,10,3), dtype="uint8")
            pixels[10:20,1150+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
            # Imprime el digito 8
        elif digit == 8:
            pixels[10:20,1150+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
            pixels[10:60,1150+offset+self.generalOffset:1160+offset+self.generalOffset, :] = np.zeros((50,10,3), dtype="uint8")
            pixels[10:60,1180+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((50,10,3), dtype="uint8")
            pixels[30:40,1150+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
            pixels[50:60,1150+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
            # Imprime el digito 9
        elif digit == 9:
            pixels[10:60,1180+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((50,10,3), dtype="uint8")
            pixels[30:40,1150+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
            pixels[10:30,1150+offset+self.generalOffset:1160+offset+self.generalOffset, :] = np.zeros((20,10,3), dtype="uint8")
            pixels[10:20,1150+offset+self.generalOffset:1190+offset+self.generalOffset, :] = np.zeros((10,40,3), dtype="uint8")
        return pixels

    # Sección de parámetros de retorno
    @property
    def width(self):
        return self.__widthBoard
    
    @property
    def heigth(self):
        return self.__heigthBoard
    
    @property
    def pixels(self):
        return self.__pixels
    

