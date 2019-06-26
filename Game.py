#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 10:58:58 2019

@author: nicolas
"""

from Board import Board
from Object import Object
import cv2
import numpy as np
from Color import Color

from multiprocessing import Process, Event
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

class Game:
    def __init__(self, camera, highRange = np.array([125,255,255],np.uint8),
                 lowRange =  np.array([100,100,20],np.uint8), pixelSize = 10):
        self.pixelSize = pixelSize
        self.__controlMoveWindow = 'MoveWindows'
        self.__boardName = 'Board'
        self.board = Board(120,80)
        self.cam = cv2.VideoCapture(camera)
        self._highRange = highRange
        self._lowRange = lowRange
        self.objects = []
        self.score = 0
        self.__state = 3
        cv2.namedWindow(self.__controlMoveWindow, cv2.WINDOW_AUTOSIZE)
        cv2.moveWindow(self.__controlMoveWindow, 1400,0)
        cv2.namedWindow(self.__boardName, cv2.WINDOW_AUTOSIZE)
        cv2.moveWindow(self.__boardName, 0,0)
        
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
                        print(self.score)
                        data.pop(num)
                    if (finalY + 1 > 780):
                        data.pop(num)
            if cv2.waitKey(33) == ord('q'):
                processObjects.terminate()
                break
            cv2.imshow(self.__boardName, matrix)
        self.cam.release()
        cv2.destroyAllWindows()
    def newObject(self, event):
        while True:
            event.set()
            time.sleep(3)            
    def check(self, color):
        if (color == "BLUE" and self.__state == 0):
            return True
        elif (color == "GREEN" and self.__state == 1):
            return True
        elif (color == "RED" and self.__state == 2):
            return True
        else:
            return False
    def moveControls(self):
        ret, frame = self.cam.read()
        frame = cv2.flip(frame,1)
        if ret==True:
            frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
            mask=cv2.inRange(frameHSV,self.lowLimit, self.highLimit)
            _,contornos,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            for c in contornos:
                area = cv2.contourArea(c)
                if area > 2000:
                    M = cv2.moments(c)
                    if (M['m00']==0): 
                        M['m00']==1
                    x = int(M['m10']/M['m00'])
                    y = int(M['m01']/M['m00'])
                    cv2.circle(frame, (x,y),7,(0,255,0),-1)
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(frame,'{},{}'.format(x,y),(x+10,y),font,0.75,
                                (0,255,0),1,cv2.LINE_AA)                           
                    if x >= 15 and x < 200 and y > 100 and y < 500:
                        self.__state = 0
                    elif x >= 400 and x < 600 and y > 100 and y < 500:
                        self.__state = 1
                    elif x >= 15 and x < 600 and y >= 0 and y <= 100:
                        self.__state = 2
                    else:
                        self.__state = 3
#                    newContour=cv2.convexHull(c)                
#                    cv2.drawContours(frame,[newContour],0,(255,0,0),3)
            cv2.imshow(self.__controlMoveWindow,frame)
                    
    @property
    def lowLimit(self):
        return self._lowRange
    @property
    def highLimit(self):
        return self._highRange
            
            