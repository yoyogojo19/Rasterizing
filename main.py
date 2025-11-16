from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from camera import *
import obj_loader as obj
import random
import time

width = 1500
height = 818
temps_avant = 0
DeltaTemps = 0
names = ["cube.obj","sol.obj","suzane.obj"]

for name in names:
    obj.load_obj(name)

exec(open("obj_loader.py").read())

def glDrawTriangle(A : vec3, B : vec3, C : vec3, color : vec3):
    glBegin(GL_TRIANGLES)
    glColor3f(color.x, color.y, color.z)
    glVertex3f(A.x, A.y, A.z)
    glVertex3f(B.x, B.y, B.z)
    glVertex3f(C.x, C.y, C.z)
    glEnd()

def display():
    global camrot
    global campos
    global DeltaTemps
    global temps_avant
    DeltaTemps = time.time() - temps_avant
    temps_avant = time.time()
    print(1/DeltaTemps)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(campos.x, campos.y, campos.z, camrot.x, camrot.y, camrot.z, 0, 1, 0)
    random.seed(10)
    for i in obj.arrettes:
        glDrawTriangle(obj.coins[i.x-1],
                        obj.coins[i.y-1], 
                        obj.coins[i.z-1],
                        vec3(random.random(),random.random(),random.random())
                        )
    CamMove(DeltaTemps)
    CamRot(DeltaTemps)
    glutSwapBuffers()

def idle():
    glutPostRedisplay()

def redimensionner(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w/h, 0.1, 1000.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    global width
    global height
    global temps_avant
    global DeltaTemps
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Rasterizer")
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(display)
    glutReshapeFunc(redimensionner)
    glutIdleFunc(idle)
    glutMainLoop()

main()
