# Guitar Hero Basico openCV

Este juego fue diseñado para la materia procesamiento digital de imagenes,
su objetivo es introducir a las mécanicas de control y procesado
de imagenes mediante la manipulación de matrices.

## Requisitos

- Python 3
- numpy
- OpenCV 3.2
- Libreria multiprocessing de python
- Tener instalado Git o descargar el repositorio

## Instalación para ubuntu (distro que usen APT)

1. Instalar python 3.

```bash
    sudo apt install python3
```
2. Instalar pip3
```bash
    sudo apt install pip3
```
3. Instalar openCV 3.2
```bash
    sudo apt install python3-opencv
```
4. Bajar el repositorio de GitLab con el comando, o en su defecto ir al repositorio y descargarlo manualmente
```bash
    git clone https://github.com/NicolasMontoya/pdi-game.git
```

5. Abrir el archivo main.py y en la configuración del juego 
indicar la camara que se desea usar. Es posible reconocer las cámaras habilitadas con el siguieten comando LINUX

```bash
    ls -ltrh /dev/video*
```

6. Una vez configurado el juego, se debe correr el siguiente comando:

```bash
    python3 main.py
```

Listo, a jugar...