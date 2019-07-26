#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 18:53:08 2019

Esta clase es el punto de enganche del juego, es decir la función principal o
main donde todo el juego se configura e inicia.

@author: Edward Nicolas Montoya
@author: Surely Berrio
@author: Meliza Sanchez
"""
    
from Game import Game

# Función de enganche
def main():
    # Inicialización del Juego
    game = Game(2)
    # Comienzo del juego
    game.startGame()

# Definición de main en python
if __name__ == "__main__":
    main()



