import sys
from functions.MSSclient import *
from utils.MSSutils import *
from utils.CLParser import *
from utils.DrawDisplay import*
import socket
from random import randint
from functions.MSScam import *
import numpy as np
from math import *

# Inicializar la pantalla de frame
dibujarCanvas=DrawDisplay()

sock = -1

# parse command line arguments (if any)
(ipAddress, port, cfgpath) = CLParser(sys.argv[1:len(sys.argv)])

# display demo information in console
print("RACameraDemo Experimento2: VIDEO WALL (30 camaras = 15 RGB y 15 MapaSemantico)\n")
print(" > Usar este ejemplo con el escenario <Experimento2> del simulador Unity")
print(" (1) Conexion como cliente en el simulador")
print(" (2) Ejecutar script para un Simulador con minimo de 6 Camaras en Escenario")
print(" (3) Al objeto creado y registrado 'cam' acceder a la funcion 'setNameRACamera()' para visualzar las camaras  ")
print(" (4) Visualizar las camaras en una pared de pantallas")

# initialize client
cli = MSSclient()
cli.connectTosimulator(ipAddress, port, sock)

numcam = MSScam()
numCam= numcam.readTosimulator(cli.sock, ipAddress, port)


name = "Experimento4_" + str(randint(0, 99))
cam = MSScam(name, 640, 480, 10)
cam.configRACamera(cli.sock, ipAddress, port)

print("Numero de camaras Disponibles "+ str(numCam))

if numCam == 0:
    print("No hay camaras moviles en el simulador")
else:
    i = 0
    while i < numCam:
        print("Acceder a las camaras con el nombre: "+ name+"_" + str(i))
        i += 1

while True:
    vecImgs=[]

    ## cam 1
    cam.setNameRACamera(name +"_0")
    frame1=cam.operator()
    if isinstance(frame1,np.ndarray):
        width, height = frame1.shape[:2]
        if width>0 and height>0:
            vecImgs.append(frame1)

    ## cam 2
    cam.setNameRACamera(name +"_1")
    frame2=cam.operator()
    if isinstance(frame2,np.ndarray):
        width, height = frame2.shape[:2]
        if width>0 and height>0:
            vecImgs.append(frame2)


    ## cam 3
    cam.setNameRACamera(name +"_2")
    frame3=cam.operator()
    if isinstance(frame3,np.ndarray):
        width, height = frame3.shape[:2]
        if width>0 and height>0:
            vecImgs.append(frame3)

    ## cam 4
    cam.setNameRACamera(name +"_3")
    frame4=cam.operator()
    if isinstance(frame4,np.ndarray):
        width, height = frame4.shape[:2]
        if width>0 and height>0:
            vecImgs.append(frame4)

    ## cam 5
    cam.setNameRACamera(name +"_4")
    frame5=cam.operator()
    if isinstance(frame5,np.ndarray):
        width, height = frame5.shape[:2]
        if width>0 and height>0:
            vecImgs.append(frame5)

    ## cam 6
    cam.setNameRACamera(name +"_5")
    frame6=cam.operator()
    if isinstance(frame6,np.ndarray):
        width, height = frame6.shape[:2]
        if width>0 and height>0:
            vecImgs.append(frame6)

    ## cam 7
    cam.setNameRACamera(name +"_6")
    frame7=cam.operator()
    if isinstance(frame7,np.ndarray):
        width, height = frame7.shape[:2]
        if width>0 and height>0:
            vecImgs.append(frame7)

    ## cam 8
    cam.setNameRACamera(name +"_7")
    frame8=cam.operator()
    if isinstance(frame8,np.ndarray):
        width, height = frame8.shape[:2]
        if width>0 and height>0:
            vecImgs.append(frame8)

    ## cam 9
    cam.setNameRACamera(name +"_8")
    frame9=cam.operator()
    if isinstance(frame9,np.ndarray):
        width, height = frame9.shape[:2]
        if width>0 and height>0:
            vecImgs.append(frame9)

    ## cam 10
    cam.setNameRACamera(name +"_9")
    frame10=cam.operator()
    if isinstance(frame10,np.ndarray):
        width, height = frame10.shape[:2]
        if width>0 and height>0:
            vecImgs.append(frame10)
    
    ## cam 11
    cam.setNameRACamera(name +"_10")
    frame11=cam.operator()
    if isinstance(frame11,np.ndarray):
        width, height = frame11.shape[:2]
        if width>0 and height>0:
            vecImgs.append(frame11)

    ## cam 12
    cam.setNameRACamera(name +"_11")
    frame12=cam.operator()
    if isinstance(frame12,np.ndarray):
        width, height = frame12.shape[:2]
        if width>0 and height>0:
            vecImgs.append(frame12)

    ## cam 13
    cam.setNameRACamera(name +"_12")
    frame13=cam.operator()
    if isinstance(frame13,np.ndarray):
        width, height = frame13.shape[:2]
        if width>0 and height>0:
            vecImgs.append(frame13)

    ## cam 14
    cam.setNameRACamera(name +"_13")
    frame14=cam.operator()
    if isinstance(frame14,np.ndarray):
        width, height = frame14.shape[:2]
        if width>0 and height>0:
            vecImgs.append(frame14)

    ## cam 15
    cam.setNameRACamera(name +"_14")
    frame15=cam.operator()
    if isinstance(frame15,np.ndarray):
        width, height = frame15.shape[:2]
        if width>0 and height>0:
            vecImgs.append(frame15)

    ## cam 16
    cam.setNameRACamera(name + "_15")
    frame16 = cam.operator()
    if isinstance(frame16, np.ndarray):
        width, height = frame16.shape[:2]
        if width > 0 and height > 0:
            vecImgs.append(frame16)

    ## cam 17
    cam.setNameRACamera(name + "_16")
    frame17 = cam.operator()
    if isinstance(frame17, np.ndarray):
        width, height = frame17.shape[:2]
        if width > 0 and height > 0:
            vecImgs.append(frame17)

    ## cam 18
    cam.setNameRACamera(name + "_17")
    frame18 = cam.operator()
    if isinstance(frame18, np.ndarray):
        width, height = frame18.shape[:2]
        if width > 0 and height > 0:
            vecImgs.append(frame18)

    ## cam 19
    cam.setNameRACamera(name + "_18")
    frame19 = cam.operator()
    if isinstance(frame19, np.ndarray):
        width, height = frame19.shape[:2]
        if width > 0 and height > 0:
            vecImgs.append(frame19)

    ## cam 20
    cam.setNameRACamera(name + "_19")
    frame20 = cam.operator()
    if isinstance(frame20, np.ndarray):
        width, height = frame20.shape[:2]
        if width > 0 and height > 0:
            vecImgs.append(frame20)

    ## cam 21
    cam.setNameRACamera(name + "_20")
    frame21 = cam.operator()
    if isinstance(frame21, np.ndarray):
        width, height = frame21.shape[:2]
        if width > 0 and height > 0:
            vecImgs.append(frame21)

    ## cam 22
    cam.setNameRACamera(name + "_21")
    frame22 = cam.operator()
    if isinstance(frame22, np.ndarray):
        width, height = frame22.shape[:2]
        if width > 0 and height > 0:
            vecImgs.append(frame22)

    ## cam 23
    cam.setNameRACamera(name + "_22")
    frame23 = cam.operator()
    if isinstance(frame23, np.ndarray):
        width, height = frame23.shape[:2]
        if width > 0 and height > 0:
            vecImgs.append(frame23)

    ## cam 24
    cam.setNameRACamera(name + "_23")
    frame24 = cam.operator()
    if isinstance(frame24, np.ndarray):
        width, height = frame24.shape[:2]
        if width > 0 and height > 0:
            vecImgs.append(frame24)

    ## cam 25
    cam.setNameRACamera(name + "_24")
    frame25 = cam.operator()
    if isinstance(frame25, np.ndarray):
        width, height = frame25.shape[:2]
        if width > 0 and height > 0:
            vecImgs.append(frame25)

    ## cam 26
    cam.setNameRACamera(name + "_25")
    frame26 = cam.operator()
    if isinstance(frame26, np.ndarray):
        width, height = frame26.shape[:2]
        if width > 0 and height > 0:
            vecImgs.append(frame26)

    ## cam 27
    cam.setNameRACamera(name + "_26")
    frame27 = cam.operator()
    if isinstance(frame27, np.ndarray):
        width, height = frame27.shape[:2]
        if width > 0 and height > 0:
            vecImgs.append(frame27)

    ## cam 28
    cam.setNameRACamera(name + "_27")
    frame28 = cam.operator()
    if isinstance(frame28, np.ndarray):
        width, height = frame28.shape[:2]
        if width > 0 and height > 0:
            vecImgs.append(frame28)

    ## cam 29
    cam.setNameRACamera(name + "_28")
    frame29 = cam.operator()
    if isinstance(frame29, np.ndarray):
        width, height = frame29.shape[:2]
        if width > 0 and height > 0:
            vecImgs.append(frame29)

    ## cam 30
    cam.setNameRACamera(name + "_29")
    frame30 = cam.operator()
    if isinstance(frame30, np.ndarray):
        width, height = frame30.shape[:2]
        if width > 0 and height > 0:
            vecImgs.append(frame30)

    ## generate video wall image
    videowall = dibujarCanvas.makeCanvas(vecImgs, 640, 4)
    # videowall = dibujarCanvas.makeCanvas(vecImgs, 980, 5)

    ## show image
    if videowall.shape[0]>0 and videowall.shape[1]>0:
        cv2.imshow("Video Wall Remote Acces Camera", videowall) ## display frame

   ## close window & exit preview loop if ESC pressed
    if cv2.waitKey(5) == KEYESCAPE:
        break

## wait 1 sec before closing this demo
time.sleep(1) ## time in seconds

cli.resetSimulator(cli.sock)
# disconnect from the simulator
cli.disconnectFromSimulator(cli.sock)
