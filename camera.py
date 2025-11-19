import keyboard
from vec import *
from numpy import *

campos = vec3(0.0,0.0,-5.0)
camrotH = 0
camrotV = 0
camrotH_rad = radians(camrotH)
camrotV_rad = radians(camrotV)
camrot = vec3(sin(camrotH)+campos.x,cos(camrotV)+campos.y,cos(camrotH)+campos.z)

def CamRot(DT): 
    global camrotH
    global camrotV
    global campos
    global camrot
    if keyboard.is_pressed("left"):
        camrotH += 50 * DT
    if keyboard.is_pressed("right"):
        camrotH -= 50 * DT
    if keyboard.is_pressed("up"):
        camrotV += 50 * DT
    if keyboard.is_pressed("down"):
        camrotV -= 50 * DT

    camrotV = clip(camrotV, -89, 89)
    
    camrotH_rad = radians(camrotH)
    camrotV_rad = radians(camrotV)

    camrot.x = sin(camrotH_rad) * cos(camrotV_rad) + campos.x
    camrot.y = sin(camrotV_rad) + campos.y
    camrot.z = cos(camrotH_rad) * cos(camrotV_rad) + campos.z

def CamMove(DT):
    global camrotH_rad, camrotH
    global camrotV_rad, camrotV
    camrotH_rad = radians(camrotH)
    camrotV_rad = radians(camrotV)
    global campos
    global camrot
    if keyboard.is_pressed("w"):
        campos.x += 5 * DT * sin(camrotH_rad) * cos(camrotV_rad)
        campos.z += 5 * DT * cos(camrotH_rad) * cos(camrotV_rad)
    if keyboard.is_pressed("s"):
        campos.x -= 5 * DT * sin(camrotH_rad) * cos(camrotV_rad)
        campos.z -= 5 * DT * cos(camrotH_rad) * cos(camrotV_rad)
    if keyboard.is_pressed("a"):
        campos.x += 5 * DT * sin(camrotH_rad + pi/2) * cos(camrotV_rad)
        campos.z += 5 * DT * cos(camrotH_rad + pi/2) * cos(camrotV_rad)
    if keyboard.is_pressed("d"):
        campos.x -= 5 * DT * sin(camrotH_rad + pi/2) * cos(camrotV_rad)
        campos.z -= 5 * DT * cos(camrotH_rad + pi/2) * cos(camrotV_rad)
    if keyboard.is_pressed("space"):
        campos.y += 5 * DT
    if keyboard.is_pressed("shift"):
        campos.y -= 5 * DT
