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
names = [("test.obj",0,0,0)]

for name in names:
    obj.load_obj(name[0],name[1],name[2],name[3])

def init_vbo():
    global vbo, color_vbo
    vbo = glGenBuffers(1)
    color_vbo = glGenBuffers(1)
    vertices = []
    colors = []
    random.seed(10)
    for i in obj.arrettes:
        A = obj.coins[i.x-1]
        B = obj.coins[i.y-1]
        C = obj.coins[i.z-1]
        color = (random.random(), random.random(), random.random())
        vertices.extend([A.x, A.y, A.z, B.x, B.y, B.z, C.x, C.y, C.z])
        colors.extend([color[0], color[1], color[2]] * 3)

    # Envoie les données au GPU
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, len(vertices)*4, (ctypes.c_float * len(vertices))(*vertices), GL_STATIC_DRAW)

    glBindBuffer(GL_ARRAY_BUFFER, color_vbo)
    glBufferData(GL_ARRAY_BUFFER, len(colors)*4, (ctypes.c_float * len(colors))(*colors), GL_STATIC_DRAW)

def display():
    global camrot, campos, DeltaTemps, temps_avant, vbo, color_vbo
    DeltaTemps = time.time() - temps_avant
    temps_avant = time.time()
    print(1/DeltaTemps)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(campos.x, campos.y, campos.z, camrot.x, camrot.y, camrot.z, 0, 1, 0)

    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_COLOR_ARRAY)

    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glVertexPointer(3, GL_FLOAT, 0, None)

    glBindBuffer(GL_ARRAY_BUFFER, color_vbo)
    glColorPointer(3, GL_FLOAT, 0, None)

    glDrawArrays(GL_TRIANGLES, 0, len(obj.arrettes)*3)

    glDisableClientState(GL_VERTEX_ARRAY)
    glDisableClientState(GL_COLOR_ARRAY)

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
    init_vbo()
    glutDisplayFunc(display)
    glutReshapeFunc(redimensionner)
    glutIdleFunc(idle)
    glutMainLoop()

main()
