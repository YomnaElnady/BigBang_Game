#Bing Bang is a simple game using Python and OpenGl Only..
# to choose certain scene in the menu use up and down arrows then press "u"
#Use Arrows to move the character and space to shoot on the ball

from time import sleep
from random import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import numpy as np
import pygame


##################### Robot/character Drawing ####################


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


##################### End Robot ##################


##################### sound staff ##########################

pygame.mixer.init()
pygame.mixer.music.load("Taeyeon - U R.mp3")
pygame.mixer.music.play(0)
win_sound=pygame.mixer.Sound("tada.wav")
fire_sound=pygame.mixer.Sound("laser.wav")
losing_sound=pygame.mixer.Sound("Lost-life-sound-effect.wav")
click_sound=pygame.mixer.Sound("click2.wav")


#################### END of sound staff ####################

#################### Ball class ####################
class ball:
    def __init__(self, radi, xi, yi, hVel, vVel):
        self.radius = radi
        self.colorR = uniform(0.3, .9)
        self.colorG = uniform(0.3, .9)
        self.colorB = uniform(0.3, .9)
        self.x = xi
        self.y = yi
        self.hVelocity = hVel
        self.vVelocity = vVel

    def isSplitted(self, x_weapon, y_weapon, l): # Check if the ball is has a collision with the weapon or not
        if round(self.y, 1) > y_weapon and round(self.y, 1) <= round(y_weapon + 15 * l, 1) and (round(self.x, 1) <= x_weapon + self.radius+1) and (round(self.x, 1) >= x_weapon - self.radius-1):
            return 1
        return 0

    def move(self): # free movement of the ball
        self.x = self.x + self.hVelocity * dtime
        self.vVelocity = self.vVelocity - 9.8 * dtime
        self.y = self.y + self.vVelocity * dtime

    def collisionWithWall(self): # chech the collision of the ball with rha wall

        if self.y >= axrng - self.radius :
            self.vVelocity = - self.vVelocity
            self.y=self.y-1
        if self.y <= -axrng + self.radius:
            self.vVelocity = - self.vVelocity
            self.y = self.y + 1
        if self.x >= axrng - self.radius :
            self.hVelocity = - self.hVelocity
            self.x=self.x-1
        if self.x <= -axrng + self.radius:
            self.hVelocity = - self.hVelocity
            self.x=self.x+1

    def disappear(self): # set up the old ball to create the new one
        self.x = 1000
        self.y = 1000

    def split(self):
        self.radius /= 2
        return self.radius

#################### END of Ball class ####################

def init(): # set up the environment of the scene
    global axrng

    glClearColor(1.0, 1.0, 1.0, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-axrng, axrng, -axrng, axrng, 20, -20)
    glMatrixMode(GL_MODELVIEW)


def lose():
    global k, p, l,t, collsionBall, playAgain, numOfSplitings, initialHVelocity, initialvVelocity,images, initialRadius, mainflag
    global y_weapon, x_weapon, x_char, y_char, anim, anim_squ, weapon, parameters, listt, timer
    global main_flag, LightSpec, LightDiff, LightPos, LightAmb, dtime, axrng, width, height

    main_flag = 0
    axrng = 100
    images = ["Final.jpg", "back2.jpg", "00.jpg", "gameover.jpg", "arrow1.jpg", 'arrow2.jpg', 'arrow3.jpg', "cong.jpg"]
    timer = axrng
    collsionBall = 0
    t = 1  ## pointer in menu
    glDisable(GL_LIGHTING)
    anim = 0  ## beginning and stopping the game
    sleep(2)
    layer(0)
    playAgain = 0
    timer = axrng
    LightPos = [0, 0, 0, 1]  # Positional light source #sun
    LightAmb = [0.5, 0.5, 0.5, 1]  # RGBA of Ambient Light
    LightDiff = [1, 1, 1, 1]  # RGBA of Diffuse Light
    LightSpec = [1, 1, 1, 1]  # RGBA of Specular Light
    dtime = 0.05
    width = 700
    height = 700
    x_char = 0
    y_char = -axrng + 7
    y_weapon = y_char
    x_weapon = x_char
    l = 0  ## vertical space in the line strips
    anim_squ = 1  ## char movement
    weapon = 0
    k = 0  ## initial splitted ball name
    p = 0  ## initial splitted ball name
    initialRadius = randrange(10, 21)
    numOfSplitings = 3
    initialHVelocity = 5
    initialvVelocity = 5
    initialXPos = randrange(-axrng + initialRadius, axrng - initialRadius + 1)
    initialYPos = randrange(50, axrng - initialRadius + 1)
    Ball = ball(initialRadius, initialXPos, initialYPos, initialHVelocity, initialHVelocity)
    listt = list()
    listt = [Ball]  ## empty list for the balls with the first ball in it
    parameters = {} # intiate again after lose

########################## Texture ###########################

def texture_setup():
    global texture
    texture = glGenTextures(8)

    for i in range(8):
        img = pygame.image.load(images[i])
        img_raw = pygame.image.tostring(img, "RGBA", 1)

        width = img.get_width()
        height = img.get_height()

        glBindTexture(GL_TEXTURE_2D, texture[i])  # Set this image in images array
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_raw)

        glEnable(GL_TEXTURE_2D)

    glFlush()

########################## End Texture ###########################

def game_over(): # load the game over scene

    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    glBindTexture(GL_TEXTURE_2D, texture[3])

    glBegin(GL_QUADS)

    glTexCoord(0, 0)
    glVertex(-axrng, -axrng, -1)

    glTexCoord(1, 0)
    glVertex(axrng, -axrng, -1)

    glTexCoord(1, 1)
    glVertex(axrng, axrng, -1)

    glTexCoord(0, 1)
    glVertex(-axrng, axrng, -1)
    glEnd()
    glFlush()
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(losing_sound)
    sleep(2)
    display(menu1)


def level_1_BackGround():# load background of level 1
    glClear(GL_COLOR_BUFFER_BIT)

    glBindTexture(GL_TEXTURE_2D, texture[1])
    glBegin(GL_QUADS)

    glTexCoord(0, 0)
    glVertex(-axrng, -axrng, 0)

    glTexCoord(1, 0)
    glVertex(axrng, -axrng, 0)

    glTexCoord(1, 1)
    glVertex(axrng, axrng, 0)

    glTexCoord(0, 1)
    glVertex(-axrng, axrng, 0)

    glEnd()


def background(): # load background of the game

    pygame.mixer.music.play(0)


    global main_flag
    main_flag=0

    glBindTexture(GL_TEXTURE_2D, texture[0])
    glBegin(GL_QUADS)

    glTexCoord(0, 0)
    glVertex(-axrng, -axrng, 0)

    glTexCoord(1, 0)
    glVertex(axrng, -axrng, 0)

    glTexCoord(1, 1)
    glVertex(axrng, axrng, 0)

    glTexCoord(0, 1)
    glVertex(-axrng, axrng, 0)

    glEnd()

    glLoadIdentity()

    glFlush()


def credit(): # load credit scene

    glClearColor(0, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    glBindTexture(GL_TEXTURE_2D, texture[2])
    glBegin(GL_QUADS)

    glTexCoord(0, 0)
    glVertex(-axrng, -axrng, 0)

    glTexCoord(1, 0)
    glVertex(axrng, -axrng, 0)

    glTexCoord(1, 1)
    glVertex(axrng, axrng, 0)

    glTexCoord(0, 1)
    glVertex(-axrng, axrng, 0)

    glEnd()
    glFlush()


def menu1():
    pygame.mixer.music.load("Taeyeon - U R.mp3")
    pygame.mixer.music.play(0)
    glClear(GL_COLOR_BUFFER_BIT)
    glBindTexture(GL_TEXTURE_2D, texture[4])
    glBegin(GL_QUADS)

    glTexCoord(0, 0)
    glVertex(-axrng, -axrng, 0)

    glTexCoord(1, 0)
    glVertex(axrng, -axrng, 0)

    glTexCoord(1, 1)
    glVertex(axrng, axrng, 0)

    glTexCoord(0, 1)
    glVertex(-axrng, axrng, 0)

    glEnd()

    glLoadIdentity()

    glFlush()
    layer(0)


def menu2():

    glClear(GL_COLOR_BUFFER_BIT)

    glBindTexture(GL_TEXTURE_2D, texture[5])
    glBegin(GL_QUADS)

    glTexCoord(0, 0)
    glVertex(-axrng, -axrng, 0)

    glTexCoord(1, 0)
    glVertex(axrng, -axrng, 0)

    glTexCoord(1, 1)
    glVertex(axrng, axrng, 0)

    glTexCoord(0, 1)
    glVertex(-axrng, axrng, 0)

    glEnd()

    glLoadIdentity()

    glFlush()


def menu3():

    glClear(GL_COLOR_BUFFER_BIT)

    glBindTexture(GL_TEXTURE_2D, texture[6])
    glBegin(GL_QUADS)

    glTexCoord(0, 0)
    glVertex(-axrng, -axrng, 0)

    glTexCoord(1, 0)
    glVertex(axrng, -axrng, 0)

    glTexCoord(1, 1)
    glVertex(axrng, axrng, 0)

    glTexCoord(0, 1)
    glVertex(-axrng, axrng, 0)

    glEnd()

    glLoadIdentity()

    glFlush()


def congrat():# load congratulation scene
    glClear(GL_COLOR_BUFFER_BIT)

    glBindTexture(GL_TEXTURE_2D, texture[7])
    glBegin(GL_QUADS)

    glTexCoord(0, 0)
    glVertex(-axrng, -axrng, 0)

    glTexCoord(1, 0)
    glVertex(axrng, -axrng, 0)

    glTexCoord(1, 1)
    glVertex(axrng, axrng, 0)

    glTexCoord(0, 1)
    glVertex(-axrng, axrng, 0)

    glEnd()

    glLoadIdentity()

    glFlush()
    sleep(2)
    display(menu1)


def Level_1(): # the core of the game
    glDisable(GL_LIGHTING)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    global MatShnF, MatShnc

    level_1_BackGround()

    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glPushMatrix()

    makeChar()

    glLightfv(GL_LIGHT0, GL_POSITION, LightPos)
    glLightfv(GL_LIGHT0, GL_AMBIENT, LightAmb)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, LightDiff)
    glLightfv(GL_LIGHT0, GL_SPECULAR, LightSpec)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    MatShnc = [128]

    glDisable(GL_TEXTURE_2D)

    Animation()

    glEnable(GL_TEXTURE_2D)

    glPopMatrix()
    glPopAttrib()
    glFlush()


def makeChar(): #Draw character

    glDisable(GL_TEXTURE_2D)

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glLoadIdentity()

    glTranslate(x_char, y_char, -1)  ###initial Place of char is (0, -9)
    Mr_Robot()

    glPopAttrib()
    glPopMatrix()

    glEnable(GL_TEXTURE_2D)


def count(): # prepare timer
    global k, p, l,collsionBall,playAgain ,numOfSplitings,initialHVelocity,initialvVelocity
    global y_weapon, x_weapon, x_char, y_char, anim, anim_squ, weapon,parameters,listt,timer
    global main_flag,LightSpec,LightDiff,LightPos,LightAmb,dtime ,axrng ,width,height


    glColor(0.5, 0.8, .9)
    if anim != 0 and timer >= -axrng:
        glLoadIdentity()
        #glTranslate(0,0,-1)
        glBegin(GL_POLYGON)
        glVertex3d(timer, axrng,-1)
        glVertex3d(-axrng, axrng,-1)
        glVertex3d(-axrng,95,-1)
        glVertex3d(timer,95,-1)
        timer -= .1
        glEnd()
    elif timer <-axrng:
        lose()
        display(game_over)


def lightAnimation(): # using lightning
    MatAmbc = [5, 0, 5, 1]
    MatDifc = [1, 0, 1, 1]
    MatSpecc = [1, 0, 1, 1]

    glMaterialfv(GL_FRONT, GL_AMBIENT, MatAmbc)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, MatDifc)
    glMaterialfv(GL_FRONT, GL_SPECULAR, MatSpecc)
    glMaterialfv(GL_FRONT, GL_SHININESS, MatShnc)

    MatAmbF = [5, 0, 5, 1]
    MatDifF = [1, 0, 1, 1]
    MatSpecF = [1, 0, 1, 1]

    glMaterialfv(GL_FRONT, GL_AMBIENT, MatAmbF)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, MatDifF)
    glMaterialfv(GL_FRONT, GL_SPECULAR, MatSpecF)
    glMaterialfv(GL_FRONT, GL_SHININESS, MatShnc)


def BallMaterial(ball):

    MatAmbF = [ball.colorR, ball.colorG, ball.colorB, 1]
    MatDifF = [ball.colorR, ball.colorG, ball.colorB, 1]
    MatSpecF = [ball.colorR, ball.colorG, ball.colorB, 1]
    MatShnF = [128]

    glMaterialfv(GL_FRONT, GL_AMBIENT, MatAmbF)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, MatDifF)
    glMaterialfv(GL_FRONT, GL_SPECULAR, MatSpecF)
    glMaterialfv(GL_FRONT, GL_SHININESS, MatShnF)


def draw(ball):

    BallMaterial(ball)
    glLoadIdentity()
    glColor(ball.colorR, ball.colorG, ball.colorB)
    glTranslate(ball.x, ball.y, -1)
    glutSolidSphere(ball.radius, 50, 50)


def generate(Ball, k, p):
    global parameters

    ############
    ## make two objects

    parameters['Ball' + str(k)] = ball(Ball.radius / 2, Ball.x + 2 * Ball.radius, Ball.y, -uniform(Ball.hVelocity-5,Ball.hVelocity+5),
                                       Ball.vVelocity)
    parameters['Ball' + str(p)] = ball(Ball.radius / 2, Ball.x - 2 * Ball.radius, Ball.y,uniform(Ball.hVelocity-5,Ball.hVelocity+5),
                                       Ball.vVelocity)
    ## end ##
    ## append to listt
    listt.append(parameters['Ball' + str(k)])
    listt.append(parameters['Ball' + str(p)])
    ## end ##


def collisionWithChar(ball):#check the collision of the ball with char
    global x_char, y_char

    if round(ball.y, 1) - ball.radius <= y_char + 3 and round(ball.x, 1) + ball.radius >= x_char - 3 and round(ball.x,1) - ball.radius <= x_char + 3:
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(losing_sound)
        lose()
        display(game_over)
        return 0
    return 1


def Animation(): # start animation
    global k, p, l,collsionBall,playAgain ,numOfSplitings,initialHVelocity,initialvVelocity ,whatever_sound,initialRadius
    global y_weapon, x_weapon, x_char, y_char, anim, anim_squ, weapon, split1,parameters,listt
    global main_flag,LightSpec,LightDiff,LightPos,LightAmb,dtime ,axrng ,width,height,timer

    lightAnimation()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glLoadIdentity()

    if anim == 1:
        glPushMatrix()
        glPushAttrib(GL_ALL_ATTRIB_BITS)
        glDisable(GL_LIGHTING)
        count()
        glEnable(GL_LIGHTING)
        glPopAttrib()
        glPopMatrix()


        if weapon == 1:
            glColor3f(1, 1, 1)
            glLineWidth(3)
            if y_weapon + 15 * l <= axrng:
                glLoadIdentity()
                glBegin(GL_LINE_STRIP)
                glVertex3d(x_weapon, y_weapon, -1)

                for i in range(20):
                    glVertex3d(x_weapon + .15, y_weapon + i, -1)
                    glVertex3d(x_weapon - .15, y_weapon + (i+.5) * l, -1)

                glVertex3d(x_weapon, y_weapon, -1)
                glVertex3d(x_weapon + 1, y_weapon + l, -1)
                glVertex3d(x_weapon - 1, y_weapon + 1.5 * l, -1)
                glVertex3d(x_weapon + 1, y_weapon + 2 * l, -1)
                glVertex3d(x_weapon - 1, y_weapon + 2.5 * l, -1)
                glVertex3d(x_weapon + 1, y_weapon + 3 * l, -1)
                glVertex3d(x_weapon - 1, y_weapon + 3.5 * l, -1)
                glVertex3d(x_weapon + 1, y_weapon + 4 * l, -1)
                glVertex3d(x_weapon - 1, y_weapon + 4.5 * l, -1)
                glVertex3d(x_weapon + 1, y_weapon + 5 * l, -1)
                glVertex3d(x_weapon - 1, y_weapon + 5.5 * l, -1)
                glVertex3d(x_weapon + 1, y_weapon + 6 * l, -1)
                glVertex3d(x_weapon - 1, y_weapon + 6.5 * l, -1)
                glVertex3d(x_weapon + 1, y_weapon + 7 * l, -1)
                glVertex3d(x_weapon - 1, y_weapon + 7.5 * l, -1)
                glVertex3d(x_weapon + 1, y_weapon + 8 * l, -1)
                glVertex3d(x_weapon - 1, y_weapon + 8.5 * l, -1)
                glVertex3d(x_weapon + 1, y_weapon + 9 * l, -1)
                glVertex3d(x_weapon - 1, y_weapon + 9.5 * l, -1)
                glVertex3d(x_weapon + 1, y_weapon + 10 * l, -1)
                glVertex3d(x_weapon - 1, y_weapon + 10.5 * l, -1)
                glVertex3d(x_weapon + 1, y_weapon + 11 * l, -1)
                glVertex3d(x_weapon - 1, y_weapon + 11.5 * l, -1)
                glVertex3d(x_weapon + 1, y_weapon + 12 * l, -1)
                glVertex3d(x_weapon - 1, y_weapon + 12.5 * l, -1)
                glVertex3d(x_weapon + 1, y_weapon + 13 * l, -1)
                glVertex3d(x_weapon - 1, y_weapon + 13.5 * l, -1)
                glVertex3d(x_weapon + 1, y_weapon + 14 * l, -1)
                glVertex3d(x_weapon - 1, y_weapon + 14.5 * l, -1)
                glVertex3d(x_weapon + 1, y_weapon + 15 * l, -1)
                glEnd()
            else:
                x_weapon = x_char
                y_weapon = y_char+5
                l = 0
            l += .3

            if y_weapon + 15 * l > axrng:
                weapon = 0

        else:
            l = 0
            x_weapon = x_char
            y_weapon = y_char

        if anim_squ == 1:
            if x_char + 5 >= axrng:
                x_char = x_char
                anim_squ = 0
            else:
                x_char = x_char + 1
                anim_squ = 0

        elif anim_squ == 2:
            if x_char - 5 <= -axrng:
                x_char = x_char
                anim_squ = 0
            else:
                x_char = x_char - 1
                anim_squ = 0

        if listt !=[]:
            for i in listt:

                if i.isSplitted(x_weapon, y_weapon, l) == 1:
                    weapon = 0
                    listt.remove(i)
                    if i.radius > initialRadius / (2 ** numOfSplitings):
                        p = k + 1
                        k +=2
                        generate(i, p, k)
                    i.disappear()

                    ##draw, move, check collisision with wall

                    draw(parameters['Ball' + str(k)])
                    draw(parameters['Ball' + str(p)])
                    parameters['Ball' + str(k)].move()
                    parameters['Ball' + str(p)].move()
                    parameters['Ball' + str(k)].collisionWithWall()
                    parameters['Ball' + str(p)].collisionWithWall()
                    #
                else:
                    draw(i)
                    i.move()
                    i.collisionWithWall()

                if collisionWithChar(i) == 0 :   ##and i.radius >= initialRadius / (2 ** numOfSplitings):
                    anim = 0
                    lose()
                    display(game_over)
                    break

        else:
              display(congrat)

              glDisable(GL_LIGHTING)
              timer=axrng
              LightPos = [0, 0, 0, 1]  # Positional light source #sun
              LightAmb = [0.5, 0.5, 0.5, 1.0]  # RGBA of Ambient Light
              LightDiff = [1, 1, 1, 1.0]  # RGBA of Diffuse Light
              LightSpec = [1, 1, 1, 1.0]  # RGBA of Specular Light
              dtime = 0.05
              axrng = 100
              width = 700
              height = 700

              x_char = 0
              y_char = -axrng + 7
              y_weapon = y_char
              x_weapon = x_char
              l = 0  ## vertical space in the line strips

              anim = 0  ## beginning and stopping the game
              anim_squ = 1  ## char movement
              weapon = 0

              k = 0  ## initial splitted ball name
              p = 0  ## initial splitted ball name

              timer = axrng

              initialXPos = randrange(-axrng + initialRadius, axrng - initialRadius + 1)
              initialYPos = randrange(50, axrng - initialRadius + 1)
              Ball = ball(initialRadius, initialXPos, initialYPos, initialHVelocity, initialHVelocity)
              listt=list()
              listt = [Ball]  ## empty list for the balls with the first ball in it
              parameters = {}
              layer(0)
              main_flag=0


    glPopAttrib()
    glPopMatrix()


def keyboard(key, xx, yy):
    global t,playAgain

    global anim, weapon, anim_squ
    global x1, x2, y_weapon, x_weapon


    if key == b" ":
        pygame.mixer.Sound.play(fire_sound)
        weapon = 1
        y_weapon = y_char
        x_weapon = x_char


    if key == GLUT_KEY_DOWN:
        t = (t + 1) % 3
        pygame.mixer.Sound.play(click_sound)

    if key == GLUT_KEY_UP:
        t = (t - 1) % 3
        pygame.mixer.Sound.play(click_sound)

    if anim==0 and playAgain == 0:
        if t == 1:
            display(menu1)
        elif t ==2:
            display(menu2)
        elif t ==0:
            display(menu3)


    if key == b"u":
        if t == 1:
            anim=1
            display(Level_1)
        elif t == 2:
            display(credit)
        elif t == 0:
            sys.exit()

    if key == b"s":
        # STOP the ball!
        anim = 0

    if key == GLUT_KEY_RIGHT :
        anim_squ = 1

    if key == GLUT_KEY_LEFT :
        anim_squ = 2

    if key == b"q":
        sys.exit()


def myMouseFunc(button,state,x,y):
    mouse_x=(2*x/1500)-1
    mouse_y=-((2*y/800)-1)

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and -0.8>mouse_x>-1.5 and 1>mouse_y>0.8 :
        glDisable(GL_LIGHTING)
        if t == 1:
            display(menu1)
        elif t == 2:
            display(menu2)
        elif t == 0:
            sys.exit()
        layer(0)


def layer(c):

    global main_flag,anim

    if c==1:
        main_flag=1
        anim = 1

    elif c==0:
        main_flag==0
        anim=0


def display(x):
    glutDisplayFunc(x)
    glutIdleFunc(x)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    # glutInitWindowPosition(0, 0)
    glutInitWindowSize(700, 700)
    glutCreateWindow(b"Big Bang")
    #glutFullScreen()
    display(menu1)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(keyboard)
    glutMouseFunc(myMouseFunc)
    lose()
    init()
    texture_setup()
    glutMainLoop()


main()
