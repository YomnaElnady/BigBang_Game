from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import numpy as np


def Mr_Robot():
    #glClearColor(1, 1, 1, 1) # clear background
    #glClear(GL_COLOR_BUFFER_BIT)

    glScale(10, 10, 0)

    glBegin(GL_POLYGON) # triangle
    glColor(0.75, 0.75, 0.75)
    glVertex2d(0, 0.8)
    glVertex2d(0.08, 0.5)
    glVertex2d(-0.08, 0.5)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON) # red circle
    glColor(1, 0, 0)
    for angle in np.arange(0, 2 * pi, 0.01):
        x = 0.06 * sin(angle)
        y = 0.06 * cos(angle) + 0.75
        glVertex2d(x, y)
    glEnd()
    #glFlush()

    glBegin(GL_POLYGON)  # face borders
    glColor(0, 0, 0)
    glVertex2d(0.31, 0.51)
    glVertex2d(-0.31, 0.51)
    glVertex2d(-0.31, 0.16)
    glVertex2d(0.31, 0.16)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON) #face
    glColor(0.75,0.75, 0.75)
    glVertex2d(0.3,0.5)
    glVertex2d(-0.3,0.5)
    glVertex2d(-0.3,0.15)
    glVertex2d(0.3,0.15)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)  # face shadow
    glColor(0.85, 0.85, 0.85)
    glVertex2d(0.2, 0.5)
    glVertex2d(-0.3, 0.5)
    glVertex2d(-0.3, 0.15)
    glVertex2d(0.2, 0.15)
    glEnd()
    #glFlush()

    glBegin(GL_POLYGON)  # ear
    glColor(0.75, 0.75, 0.75)
    glVertex2d(0.35, 0.37)
    glVertex2d(0.3, 0.37)
    glVertex2d(0.3, 0.27)
    glVertex2d(0.35, 0.27)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)  # ear
    glColor(0.75, 0.75, 0.75)
    glVertex2d(-0.35, 0.37)
    glVertex2d(-0.3, 0.37)
    glVertex2d(-0.3, 0.27)
    glVertex2d(-0.35, 0.27)
    glEnd()
    #glFlush()


    glBegin(GL_POLYGON)  # mouth borders
    glColor(0, 0, 0)
    glVertex2d(0.38, 0.155)
    glVertex2d(-0.38, 0.155)
    glVertex2d(-0.38, -0.01)
    glVertex2d(0.38, -0.01)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)  # mouth
    glColor(0.78, 0.78, 0.78)
    glVertex2d(0.37,0.15)
    glVertex2d(-0.37,0.15)
    glVertex2d(-0.37,0)
    glVertex2d(0.37,0)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)  # cutting mouth
    glColor(1, 1, 1)
    glVertex2d(0.27, 0.15)
    glVertex2d(-0.27, 0.15)
    glVertex2d(-0.17, 0.1)
    glVertex2d(0.17, 0.1)
    glEnd()
    #glFlush()

    glBegin(GL_POLYGON)  # eye
    glColor(1, 1, 1)
    for angle in np.arange(0, 2 * pi, 0.01):
        x = 0.07 * sin(angle) + 0.12
        y = 0.07 * cos(angle) + 0.38
        glVertex2d(x, y)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)  # eye
    glColor(1, 1, 1)
    for angle in np.arange(0, 2 * pi, 0.01):
        x = 0.07 * sin(angle) - 0.12
        y = 0.07 * cos(angle) + 0.38
        glVertex2d(x, y)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)  # eye
    glColor(0, 0, 0)
    for angle in np.arange(0, 2 * pi, 0.01):
        x = 0.04 * sin(angle) + 0.11
        y = 0.04 * cos(angle) + 0.36
        glVertex2d(x, y)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)  # eye
    glColor(0, 0, 0)
    for angle in np.arange(0, 2 * pi, 0.01):
        x = 0.04 * sin(angle) - 0.11
        y = 0.04 * cos(angle) + 0.36
        glVertex2d(x, y)
    glEnd()
    #glFlush()

    glBegin(GL_POLYGON)  # neck borders
    glColor(0,0,0)
    glVertex2d(0.105,0.005)
    glVertex2d(-0.105,0.005)
    glVertex2d(-0.105, -0.021)
    glVertex2d(0.105,-0.021)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)  # neck
    glColor(0.78, 0.78, 0.78)
    glVertex2d(0.1,0)
    glVertex2d(-0.1,0)
    glVertex2d(-0.1,-0.02)
    glVertex2d(0.1,-0.02)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)  # neck borders
    glColor(0, 0, 0)
    glVertex2d(0.13,-0.021)
    glVertex2d(-0.13,-0.021)
    glVertex2d(-0.13,-0.081)
    glVertex2d(0.13,-0.081)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)  # neck
    glColor(0.78, 0.78, 0.78)
    glVertex2d(0.12,-0.03)
    glVertex2d(-0.12,-0.03)
    glVertex2d(-0.12,-0.08)
    glVertex2d(0.12, -0.08)
    glEnd()
    #glFlush()

    glBegin(GL_POLYGON)  # right arm
    glColor(0.78, 0.78, 0.78)
    glVertex2d(0.31, -0.1)
    glVertex2d(0.23, -0.12)
    glVertex2d(0.31, -0.33)
    glVertex2d(0.38, -0.31)
    glEnd()
    #glFlush()

    glBegin(GL_POLYGON)  # right arm
    glColor(0.78, 0.78, 0.78)
    glVertex2d(0.47, -0.12)
    glVertex2d(0.33, -0.34)
    glVertex2d(0.38, -0.38)
    glVertex2d(0.479, -0.22)
    glEnd()
    #glFlush()

    glBegin(GL_POLYGON) # arm circle borders
    glColor(0, 0, 0)
    for angle in np.arange(0, 2 * pi, 0.01):
        x = 0.07 * sin(angle) - 0.36
        y = 0.07 * cos(angle) - 0.34
        glVertex2d(x, y)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)  # left arm
    glColor(0.78, 0.78, 0.78)
    glVertex2d(-0.31, -0.1)
    glVertex2d(-0.23, -0.12)
    glVertex2d(-0.31, -0.33)
    glVertex2d(-0.38, -0.31)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)  # left arm
    glColor(0.78, 0.78, 0.78)
    glVertex2d(-0.47, -0.12)
    glVertex2d(-0.33, -0.34)
    glVertex2d(-0.38, -0.38)
    glVertex2d(-0.479, -0.22)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON) # arm borders
    glColor(0, 0, 0)
    for angle in np.arange(0, 2 * pi, 0.01):
        x = 0.07 * sin(angle) - 0.36
        y = 0.07 * cos(angle) - 0.34
        glVertex2d(x, y)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON) # arm circle
    glColor(0.78, 0.78, 0.78)
    for angle in np.arange(0, 2 * pi, 0.01):
        x = 0.06 * sin(angle) - 0.36
        y = 0.06 * cos(angle) - 0.34
        glVertex2d(x, y)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON) # arm borders
    glColor(0, 0, 0)
    for angle in np.arange(0, 2 * pi, 0.01):
        x = 0.07 * sin(angle) + 0.36
        y = 0.07 * cos(angle) - 0.34
        glVertex2d(x, y)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON) # arm circle
    glColor(0.78, 0.78, 0.78)
    for angle in np.arange(0, 2 * pi, 0.01):
        x = 0.06 * sin(angle) +0.36
        y = 0.06 * cos(angle) - 0.34
        glVertex2d(x, y)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)
    glColor(0, 0, 0)
    for angle in np.arange(0, 2 * pi, 0.01):
        x = 0.07 * sin(angle) + 0.479
        y = 0.07 * cos(angle) - 0.18
        glVertex2d(x, y)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)
    glColor(0, 0, 0)
    for angle in np.arange(0, 2 * pi, 0.01):
        x = 0.07 * sin(angle) - 0.479
        y = 0.07 * cos(angle) - 0.18
        glVertex2d(x, y)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)
    glColor(0.78, 0.78, 0.78)
    for angle in np.arange(0, 2 * pi, 0.01):
        x = 0.06 * sin(angle) + 0.479
        y = 0.06 * cos(angle) - 0.18
        glVertex2d(x, y)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)
    glColor(0.78, 0.78, 0.78)
    for angle in np.arange(0, 2 * pi, 0.01):
        x = 0.06 * sin(angle) - 0.479
        y = 0.06 * cos(angle) - 0.18
        glVertex2d(x, y)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)
    glColor(0, 0, 0)
    for angle in np.arange(0, 2 * pi, 0.01):
        x = 0.09 * sin(angle) + 0.24
        y = 0.09 * cos(angle) - 0.12
        glVertex2d(x, y)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)
    glColor(0, 0, 0)
    for angle in np.arange(0, 2 * pi, 0.01):
        x = 0.09 * sin(angle) - 0.24
        y = 0.09 * cos(angle) - 0.12
        glVertex2d(x, y)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)
    glColor(0.78, 0.78, 0.78)
    for angle in np.arange(0, 2 * pi, 0.01):
        x = 0.08 * sin(angle) + 0.24
        y = 0.08 * cos(angle) - 0.12
        glVertex2d(x, y)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)
    glColor(0.78,0.78,0.78)
    for angle in np.arange(0, 2 * pi, 0.01):
        x = 0.08 * sin(angle) -0.24
        y = 0.08 * cos(angle) - 0.12
        glVertex2d(x, y)
    glEnd()
    #glFlush()

    glBegin(GL_POLYGON)  # body borders
    glColor(0, 0, 0)
    glVertex2d(0.25,-0.07)
    glVertex2d(-0.25,-0.07)
    glVertex2d(-0.25,-0.41)
    glVertex2d(0.25,-0.41)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)  # body
    glColor(0.78, 0.78, 0.78)
    glVertex2d(0.24,-0.08)
    glVertex2d(-0.24,-0.08)
    glVertex2d(-0.24,-0.4)
    glVertex2d(0.24, -0.4)
    glEnd()
    #glFlush()

    glBegin(GL_POLYGON)  # lines
    glColor(0.5, 0.5, 0.5)
    glVertex2d(0.1, -0.16)
    glVertex2d(-0.1, -0.16)
    glVertex2d(-0.1, -0.19)
    glVertex2d(0.1, -0.19)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)  # lines
    glColor(0.5,0.5,0.5)
    glVertex2d(0.1, -0.21)
    glVertex2d(-0.1, -0.21)
    glVertex2d(-0.1, -0.24)
    glVertex2d(0.1, -0.24)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON) # red circles in body
    glColor(1, 0, 0)
    for angle in np.arange(0, 2 * pi, 0.01):
        x = 0.04 * sin(angle)+ 0.18
        y = 0.04 * cos(angle)- 0.31
        glVertex2d(x, y)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)
    glColor(1, 0, 0)
    for angle in np.arange(0, 2 * pi, 0.01):
        x = 0.04 * sin(angle) - 0.18
        y = 0.04 * cos(angle) - 0.31
        glVertex2d(x, y)
    glEnd()
    #glFlush()

    glBegin(GL_POLYGON)  # legs borders
    glColor(0, 0, 0)
    glVertex2d(0.21,-0.4)
    glVertex2d(0.03,-0.4)
    glVertex2d(0.03,-0.71)
    glVertex2d(0.21,-0.71)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)  # legs borders
    glColor(0, 0, 0)
    glVertex2d(-0.21, -0.4)
    glVertex2d(-0.03, -0.4)
    glVertex2d(-0.03, -0.71)
    glVertex2d(-0.21, -0.71)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)  # legs
    glColor(0.78, 0.78, 0.78)
    glVertex2d(0.2,-0.41)
    glVertex2d(0.04,-0.41)
    glVertex2d(0.04,-0.7)
    glVertex2d(0.2,-0.7)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)  # legs
    glColor(0.78, 0.78, 0.78)
    glVertex2d(-0.2, -0.41)
    glVertex2d(-0.04, -0.41)
    glVertex2d(-0.04, -0.7)
    glVertex2d(-0.2, -0.7)
    glEnd()
    #glFlush()

    glBegin(GL_POLYGON) # foot borders
    glColor(0, 0, 0)
    for angle in np.arange(0, 2 * pi, 0.01):
        x = 0.16 * sin(angle) + 0.19
        y = 0.16 * cos(angle) - 0.71
        glVertex2d(x, y)
    glEnd()
    #glFlush()

    glBegin(GL_POLYGON) # foot borders
    glColor(0, 0, 0)
    for angle in np.arange(0, 2 * pi, 0.01):
        x = 0.16 * sin(angle) - 0.19
        y = 0.16 * cos(angle) - 0.71
        glVertex2d(x, y)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON) # foot
    glColor(0.78, 0.78, 0.78)
    for angle in np.arange(0, 2 * pi, 0.01):
        x = 0.15* sin(angle) + 0.19
        y = 0.15* cos(angle) - 0.71
        glVertex2d(x, y)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)
    glColor(0.78, 0.78, 0.78)
    for angle in np.arange(0, 2 * pi, 0.01):
        x = 0.15* sin(angle) - 0.19
        y = 0.15 * cos(angle) - 0.71
        glVertex2d(x, y)
    glEnd()
    #glFlush()
    glBegin(GL_POLYGON)  # foot cutting
    glColor(1,1, 1)
    glVertex2d(0.5, -0.71)
    glVertex2d(-0.5, -0.71)
    glVertex2d(-0.5, -0.9)
    glVertex2d(0.5, -0.9)
    glEnd()
    #glFlush()


#glutInit()
#glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
#glutCreateWindow(b"Mr.Robot")
#glutDisplayFunc(Mr_Robot)
#glutMainLoop()