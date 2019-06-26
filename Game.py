#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 10:58:58 2019

Esta es la clase principal del juego donde los diferentes componentes se
interconectan y permiten la interacción del usuario.

@author: Edward Nicolas Montoya
@author: Surely Berrio
"""
# Clases de utilidad creadas para controlar elementos del juego
from Board import Board
from Object import Object
from Color import Color

# Librerias de python para control visual y de matrices
import cv2
import numpy as np

# Libreria de hilos
from multiprocessing import Process, Event
import time

class Game:
    """    
    Constructor de la clase, contiene los parámetros de configuración
    
    @param camera - numero de camara a usar
    @param highRange - tono alto del color que va a detectar
    @param lowRange - tono bajo del color que va a detectar
    @param pixelSize - Tamaño del pixel del juego (Aún no está completamente funciona)
    """
    def __init__(self, camera, highRange = np.array([125,255,255],np.uint8),
                 lowRange =  np.array([100,100,20],np.uint8), pixelSize = 10):
        self.pixelSize = pixelSize
        # Nombre de ventanas
        self.__controlMoveWindow = 'MoveWindows'
        self.__boardName = 'Board'
        self.board = Board(135,80)
        self.cam = cv2.VideoCapture(camera)
        self._highRange = highRange
        self._lowRange = lowRange
        self.objects = []
        self.score = 0
        self.__state = 3
        # Inicialización de ventanas
        cv2.namedWindow(self.__controlMoveWindow, cv2.WINDOW_AUTOSIZE)
        cv2.moveWindow(self.__controlMoveWindow, 1600,700)
        cv2.namedWindow(self.__boardName, cv2.WINDOW_AUTOSIZE)
        cv2.moveWindow(self.__boardName, 0,0)
    """    
    Inicio del juego, en este método se crea un proceso (Hilo) para controlar
    el tiempo, se configura el análisis de color y movimiento
    """ 
    def startGame(self):
        data = []
        event = Event()
        processObjects = Process(target=self.newObject, args=(event,), name="Creating process")
        processObjects.start()
        while True:
            self.moveControls()
            if event.is_set():
                event.clear()
                element = np.random.randint(3)
                if element == 0:
                    obj = Object(270, 310, 0, 40, Color.getBlue(self.pixelSize, self.pixelSize), "BLUE")
                elif element == 1:
                    obj = Object(580, 620, 0, 40, Color.getGreen(self.pixelSize, self.pixelSize), "GREEN")
                else:
                    obj = Object(890, 930, 0, 40, Color.getRed(self.pixelSize, self.pixelSize), "RED")
                obj.genMatrix()
                data.append(obj)
            matrix = np.copy(self.board.pixels)
            if len(data) > 0:
                for num, printableObject in enumerate(data):
                    initialX, finalX, initialY, finalY, color, name = printableObject.position()
                    matrix[initialY:finalY,initialX:finalX, :] = printableObject.matrix
                    printableObject.move()
                    if (finalY + 1 > 740 and finalY + 1 < 780 and self.check(name)):
                        self.score += 1
                        if self.score == 100:
                            processObjects.terminate()
                            self.cam.release()
                            cv2.destroyAllWindows()
                            im = cv2.imread("winner.png")
                            cv2.imshow("WINNER", im)
                            if cv2.waitKey(0):
                               cv2.destroyAllWindows() 
                               exit()
                        data.pop(num)
                    if (finalY + 1 > 780):
                        data.pop(num)
            if cv2.waitKey(33) == ord('q'):
                processObjects.terminate()
                break
            matrix = self.board.printScore(matrix, self.score)
            cv2.imshow(self.__boardName, matrix)
        self.cam.release()
        cv2.destroyAllWindows()
    """    
    Controla el tiempo de creación de nuevos objectos
    
    @param camera - evento que avisa el programa principal que debe crear un
    nuevo objeto
    """
    def newObject(self, event):
        while True:
            event.set()
            time.sleep(3)
    """    
    Método encargado de revisar si el objeto fue identificado
    
    @param color - indica el color del objeto a análizar
    """
    def check(self, color):
        if (color == "BLUE" and self.__state == 0):
            return True
        elif (color == "GREEN" and self.__state == 1):
            return True
        elif (color == "RED" and self.__state == 2):
            return True
        else:
            return False
    """    
    Método encargado de revisar los movimientos de la persona e identificar
    el color del objeto
    """
    def moveControls(self):
        # Lee la camara
        ret, frame = self.cam.read()
        # Realiza efecto espejo para acoplar la imágen a las direcciones de
        # la persona
        frame = cv2.flip(frame,1)
        # Revisar si fue captada la fotografia
        if ret==True:
            # Convierte el formato de color a HSV
            frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
            # Extrae el rango dinámico del color definido
            mask=cv2.inRange(frameHSV,self.lowLimit, self.highLimit)
            # Busca contornos en la mascara
            _,contornos,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            # Por cada contorno analiza el area y obtiene el centroide en la imagen
            for c in contornos:
                area = cv2.contourArea(c)
                if area > 2000:
                    M = cv2.moments(c)
                    if (M['m00']==0): 
                        M['m00']==1
                    x = int(M['m10']/M['m00'])
                    y = int(M['m01']/M['m00'])
                    # Con el centroide obtenido agrega un punto
                    cv2.circle(frame, (x,y),7,(0,255,0),-1)
                    # evalua uno de los tres estados donde puede estar el objeto
                    # para identificar si impacto                        
                    if x >= 15 and x < 200 and y > 100 and y < 500:
                        self.__state = 0
                    elif x >= 400 and x < 600 and y > 100 and y < 500:
                        self.__state = 1
                    elif x >= 15 and x < 600 and y >= 0 and y <= 100:
                        self.__state = 2
                    else:
                        self.__state = 3
            # Muestra la imágen
            cv2.imshow(self.__controlMoveWindow,frame)
    # Getters de la clase
    @property
    def lowLimit(self):
        return self._lowRange
    @property
    def highLimit(self):
        return self._highRange
            
            