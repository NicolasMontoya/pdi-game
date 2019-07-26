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
from pygame import mixer
# Libreria de hilos
from multiprocessing import Process, Event
import time

class Game:
    """    
    Constructor de la clase, contiene los parámetros de configuración
    
    @param camera - numero de camara a usar
    @param highRange - tono alto del color que va a detectar
    @param lowRange - tono bajo del color que va a detectar
    @param pixelSize - Tamaño del pixel del juego 
    """
    def __init__(self, camera, highRange = np.array([140,255,255],np.uint8),
                 lowRange =  np.array([100,150,20],np.uint8), pixelSize = 10):
        # Objeto de PyGame para usar musica de fondo.
        self.mixer = mixer
        # Initialización del objeto para manipular la musica.
        self.mixer.init()
        # Cargado de archivo con canción de fondo
        self.mixer.music.load('paint.mp3')
        # Inicio de canción
        self.mixer.music.play()
        # Definición del tamaño del pixel (cuadricula minima)
        self.pixelSize = pixelSize
        # Nombre de ventanas
        self.__controlMoveWindow = 'MoveWindows'
        self.__boardName = 'Board'
        # Creación del tablero de juego
        self.board = Board(135,80)
        self.cam = cv2.VideoCapture(camera)
        # Rangos de colores para detección de la imagen
        self._highRange = highRange
        self._lowRange = lowRange
        self.objects = []
        # Definición de puntuación positiva y negativa
        self.score = 0
        self.__negativePoint = 0 
        self.__state = 3
        # Inicialización de ventanas
        cv2.namedWindow(self.__controlMoveWindow, cv2.WINDOW_AUTOSIZE)
        cv2.moveWindow(self.__controlMoveWindow, 1600,700)
        cv2.namedWindow(self.__boardName, cv2.WINDOW_AUTOSIZE)
        cv2.moveWindow(self.__boardName, 0,0)
    """    
    Inicio del juego, en este método se crea un proceso (HhighLimitilo) para controlar
    el tiempo, se configura el análisis de color y movimiento
    """ 
    def startGame(self):
        # Inicialización de arreglo de objetos
        data = []
        # Creación de evento para control de la generación de objetos
        event = Event()
        # Definición de proceso en segundo plano para conteo de tiempo
        processObjects = Process(target=self.newObject, args=(event,), name="Creating process")
        # Inicio de proceso
        processObjects.start()
        # While infinito que da inicio al juego
        while True:
            # Verifica el estado del juego mediante la lectura de la cámara
            self.moveControls()
            # Si hay un evento identificado, se crea un nuevo objeto
            if event.is_set():
                event.clear()
                element = np.random.randint(3)
                if element == 0:
                    obj = Object(270, 310, 0, 40, Color.getBlue(self.pixelSize, self.pixelSize), "BLUE")
                elif element == 1:
                    obj = Object(580, 620, 0, 40, Color.getGreen(self.pixelSize, self.pixelSize), "GREEN")
                else:
                    obj = Object(890, 930, 0, 40, Color.getRed(self.pixelSize, self.pixelSize), "RED")
                # Creación del objeto
                obj.genMatrix()
                # Adición al arreglo general (lista)
                data.append(obj)
            # Copia de la matriz referencia
            matrix = np.copy(self.board.pixels)
            if len(data) > 0:
                # Impresión de objetos en la pantalla
                for num, printableObject in enumerate(data):
                    # Trae coordenadas del objeto
                    initialX, finalX, initialY, finalY, color, name = printableObject.position()
                    # Obtiene matriz de posición
                    matrix[initialY:finalY,initialX:finalX, :] = printableObject.matrix
                    # Desplaza objeto
                    printableObject.move()
                    # Revisa si el objeto esta en la franja para puntuar y es interceptado por el estado correspondiente de juego
                    if (finalY + 1 > 740 and finalY + 1 < 780 and self.check(name)):
                        # Si es interceptado suma un punto
                        self.score += 1
                        # Verifica si el usuario gano y termina el juego con la pantalla de ganador
                        if self.score == 20:
                            processObjects.terminate()
                            self.cam.release()
                            cv2.destroyAllWindows()
                            im = cv2.imread("winner.png")
                            cv2.imshow("WINNER", im)
                            if cv2.waitKey(0):
                                self.mixer.music.stop()
                                cv2.destroyAllWindows()
                                exit()
                        data.pop(num)
                    # Verifica si el usuario no logro atinar al cuadro y le suma un punto negativo
                    if (finalY + 1 > 780):
                        self.__negativePoint+=1
                        # Elimina el objeto en la parte inferior de la pantalla
                        data.pop(num)
                        # Si el usuario suma 5 puntos negativos pierde
                        if(self.__negativePoint == 5):
                            processObjects.terminate()
                            cv2.destroyAllWindows()
                            im = cv2.imread("loser.jpg")
                            cv2.imshow("PERDISTE", im)
                            if cv2.waitKey(0):
                                self.mixer.music.stop()
                                cv2.destroyAllWindows()
                                exit()
            # Tecla para salirse del juego
            if cv2.waitKey(33) == ord('q'):
                self.mixer.music.stop()
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
            if (len(contornos) == 0):
                self.__state = 3
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
                    elif x >= 500 and x < 600 and y > 100 and y < 500:
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
            
            