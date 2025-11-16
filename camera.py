import keyboard
from vec import *
from numpy import *

campos = vec3(0.0,0.0,-5.0)
camrotH = 0
camrotV = 0
camrot = vec3(sin(camrotH)+campos.x,cos(camrotV)+campos.y,cos(camrotH)+campos.z)

def CamRot(DT): 
    global camrotH
    global camrotV
    global campos
    global camrot
    if keyboard.is_pressed("left"):
        camrotH += 5 * DT
    if keyboard.is_pressed("right"):
        camrotH -= 5 * DT
    if keyboard.is_pressed("up"):
        camrotV += 5 * DT
    if keyboard.is_pressed("down"):
        camrotV -= 5 * DT
    if camrotV >= 90:
        camrotV = 90
    if camrotV <= -90:
        camrotV = -90
    camrot.x = sin(camrotH)+campos.x
    camrot.y = cos(camrotV)+campos.y
    camrot.z = cos(camrotH)+campos.z

def CamMove(DT):
    global camrotH
    global camrotV
    global campos
    global camrot
    if keyboard.is_pressed("a"):
        campos.z += 5 * DT * -sin(camrotH)
        campos.x += 5 * DT * cos(camrotH)
    if keyboard.is_pressed("d"):
        campos.z -= 5 * DT * -sin(camrotH)
        campos.x -= 5 * DT * cos(camrotH)
    if keyboard.is_pressed("w"):
        campos.z += 5 * DT * cos(camrotH)
        campos.x += 5 * DT * sin(camrotH)
    if keyboard.is_pressed("s"):
        campos.z -= 5 * DT * cos(camrotH)
        campos.x -= 5 * DT * sin(camrotH)
    if keyboard.is_pressed("space"):
        campos.y += 5 * DT
    if keyboard.is_pressed("shift"):
        campos.y -= 5 * DT