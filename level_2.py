# Level 2 of Big Bang Game
# Press "P" to start , Arrows to move , Space for shoots , "S' to stop , "q" to quit

import time
from random import uniform ,randrange
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame
from Mr_Robot import*


dtime = 0.05
axrng = 100
y1= y2 = axrng/2
width = 700
height = 700

x_char = -50
y_char = -axrng + 7
y_weapon = y_char
x_weapon = x_char
l = 0  ## vertical space in the line strips

anim = 0    ## beginning and stopping the game
anim_squ = 1  ## char movement
weapon = 0  ## for shooting

initialRadius = 10

##########

k = 0  ## initial splitted ball name
p = 0  ## initial splitted ball name


def texturesWall():
    global texture
    texture = glGenTextures(2)
    img1 = pygame.image.load("wall3.jpeg")
    img_raw1 = pygame.image.tostring(img1, "RGBA", 1)

    img2 = pygame.image.load("wall3.jpeg")
    img_raw2 = pygame.image.tostring(img2, "RGBA", 1)

    width = img1.get_width()
    height = img1.get_height()
    width2 = img2.get_width()
    height2 = img2.get_height()

    glBindTexture(GL_TEXTURE_2D, texture[0])

    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_raw1)


    glBindTexture(GL_TEXTURE_2D, texture[1])

    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    glTexImage2D(GL_TEXTURE_2D, 0, 3, width2, height2, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_raw2)


class ball:
    def __init__(self, radi, xi, yi, hVel, vVel):
        self.radius = radi
        self.colorR = uniform(0.5, .9)
        self.colorG = uniform(0.5, .9)
        self.colorB = uniform(0.5, .9)
        self.x = xi
        self.y = yi
        self.hVelocity = hVel
        self.vVelocity = vVel

    def isSplitted(self, x_weapon, y_weapon, l):
        if round(self.y, 1) > y_weapon and round(self.y, 1) < round(y_weapon + 15 * l, 1) and (
                round(self.x, 1) <= x_weapon + self.radius) and (
                round(self.x, 1) >= x_weapon - self.radius):
            return 1
        return 0

    def move(self):
        self.x = self.x + self.hVelocity * dtime
        self.vVelocity = self.vVelocity - 9.8 * dtime
        self.y = self.y + self.vVelocity * dtime

    def collisionWithWall(self,lista):
        if lista == listt_1:

            if self.y >= axrng - self.radius or self.y <= -axrng + self.radius:
                self.vVelocity = - self.vVelocity
                if self.y > 0:
                    self.y -= 1
                else:
                    self.y += 1

            if self.x >= ((axrng//2)-60) - self.radius or self.x <= -axrng + self.radius:
                if self.x >(-axrng+((axrng//2)-60))//2:
                    self.x-= 1
                else:
                    self.x+= 1
                self.hVelocity = - self.hVelocity
        else:
            if self.y >= axrng - self.radius or self.y <= -axrng + self.radius:
                self.vVelocity = - self.vVelocity
                if self.y > 0:
                    self.y -= 1
                else:
                    self.y += 1

            if self.x >= axrng - self.radius or self.x <= -axrng + self.radius:
                self.hVelocity = - self.hVelocity
                if self.x > 0:
                    self.x -= 1
                else:
                    self.x += 1



    def disappear(self):
        self.x = 1000
        self.y = 1000

    """def isDissapear(self):

        if self.radius == 0:
            return True
        return False
    """

    def split(self):
        self.radius /= 2
        return self.radius

initialHVelocity = 5
initialvVelocity = 5
initialXPos = -50
initialYPos = 25
Ball_1 = ball(initialRadius, initialXPos, initialYPos, initialHVelocity, initialHVelocity)

listt_1 = [Ball_1]  ## empty list for the balls with the first ball in it

initialXPos2 = 50
initialYPos2 = 25
Ball_2 = ball(initialRadius, initialXPos2, initialYPos2, initialHVelocity, initialHVelocity)

listt_2 = [Ball_2]
parameters ={}  ## dict for naming the balls




def display(x):
    glutDisplayFunc(x)
    glutIdleFunc(x)

def drawQuad():
    global texture
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    glBindTexture(GL_TEXTURE_2D, texture[0])
    glBegin(GL_QUADS)
    glColor3f(1,1,1)
    glTexCoord(0, 0)
    glVertex3d((axrng / 2) - 10, y1-60, -1)

    glTexCoord(1, 0)
    glVertex3d((axrng / 2) + 10, y1-60, -1)

    glTexCoord(1, 1)
    glVertex3d((axrng / 2) + 10, axrng, -1)

    glTexCoord(0, 1)
    glVertex3d((axrng / 2) - 10, axrng, -1)

    glEnd()

    glBindTexture(GL_TEXTURE_2D, texture[1])
    glBegin(GL_QUADS)
    glColor3f(1,1,1)
    glTexCoord(0, 0)
    glVertex3d((axrng / 2) - 10, -axrng, -1)

    glTexCoord(1, 0)
    glVertex3d((axrng / 2) + 10, -axrng, -1)

    glTexCoord(1, 1)
    glVertex3d((axrng / 2) + 10, y2-60, -1)

    glTexCoord(0, 1)
    glVertex3d((axrng / 2) - 10, y2-60, -1)
    glEnd()



def level2():

    glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT)
    global k,p,parameters,listt_1,listt_2,y2,y1
    glLoadIdentity()
    glColor(0.2, 0.2, 0.2)
    glTranslate(-50,0,0)
    drawQuad()
    glLoadIdentity()
    glTranslate(x_char, y_char, -1)  ###initial Place of char is (0, -9)
    Mr_Robot()
    glDisable(GL_TEXTURE_2D)

    if(listt_1 != []):
         Animation(listt_1)

    else:
         k=p=0
         y1+=2
         y2-=2
         glDisable(GL_TEXTURE_2D)
         Animation(listt_2)
         glEnable(GL_TEXTURE_2D)

    glEnable(GL_TEXTURE_2D)

    glFlush()


def init():
    global axrng
    glClearColor(1, 1, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-axrng, axrng, -axrng, axrng, 20, -50)
    glMatrixMode(GL_MODELVIEW)



def draw(ball):
    glLoadIdentity()
    glColor(ball.colorR, ball.colorG, ball.colorB)
    glTranslate(ball.x, ball.y, -1)
    glutSolidSphere(ball.radius, 50, 50)


def collisionWithChar(ball):
    global x_char, y_char

    if round(ball.y, 1) - ball.radius <= y_char + 5 and round(ball.x, 1) + ball.radius >= x_char - 5 and round(ball.x,1) - ball.radius <= x_char + 5:
        return 0
    return 1


def Animation(listt):
    global k, p, l
    global y_weapon, x_weapon, x_char, ychar, anim, anim_squ, weapon,y1,y2

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glLoadIdentity()


    if anim == 1:
        if weapon == 1:
            glColor3f(0.3, 0.4, 0.5)
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
            y_weapon = y_char+5

        if listt == listt_1:
            if anim_squ == 1:
               if x_char + 5 >= (axrng/2 - 60):
                  x_char = x_char
                  anim_squ = 0
               else:
                  x_char = x_char + 1
                  anim_squ = 0

            elif anim_squ == 2:
               if x_char - 5 <= -axrng :
                  x_char = x_char
                  anim_squ = 0
               else:
                  x_char = x_char - 1
                  anim_squ = 0
        elif listt == listt_2 :
            if anim_squ == 1:
               if x_char + 5 >= axrng:
                  x_char = x_char
                  anim_squ = 0
               else:
                  x_char = x_char + 1
                  anim_squ = 0

            elif anim_squ == 2:
               if x_char - 5 <= -axrng :
                  x_char = x_char
                  anim_squ = 0
               else:
                  x_char = x_char - 1
                  anim_squ = 0


        for i in listt:

            if i.isSplitted(x_weapon, y_weapon, l) == 1:
                weapon = 0
                listt.remove(i)
                if i.radius > 2:
                    p = k + 1
                    generate(i, p, k,listt)
                    k += 1
                i.disappear()

                ##draw, move, check collisision with wall

                draw(parameters['Ball' + str(k)])
                draw(parameters['Ball' + str(p)])
                parameters['Ball' + str(k)].move()
                parameters['Ball' + str(p)].move()
                parameters['Ball' + str(k)].collisionWithWall(listt)
                parameters['Ball' + str(p)].collisionWithWall(listt)

            else:
                draw(i)
                i.move()
                i.collisionWithWall(listt)

            if collisionWithChar(i) == 0: #and i.radius >= 3  :
                anim = 0
                break
    else:
        for i in listt:
            draw(i)

    glPopAttrib()
    glPopMatrix()

def generate(Ball, k, p,listt):
    global parameters

    ############
    ## make two objects

    parameters['Ball' + str(k)] = ball(Ball.radius / 2, Ball.x + 2 * Ball.radius, Ball.y, -Ball.hVelocity,
                                       Ball.vVelocity)
    parameters['Ball' + str(p)] = ball(Ball.radius / 2, Ball.x - 2 * Ball.radius, Ball.y, Ball.hVelocity,
                                       Ball.vVelocity)
    ## end ##
    ############


    ############
    ## append to listt
    listt.append(parameters['Ball' + str(k)])
    listt.append(parameters['Ball' + str(p)])
    ## end ##
    ############

def keyboard(key, xx, yy):
    # Allows us to quit by pressing 'q'
    # We can animate by "a" and stop by "s"

    global anim, weapon, anim_squ
    global x1, x2, y_weapon, x_weapon

    if key == b" ":
        weapon = 1
        y_weapon = y_char
        x_weapon = x_char

    if key == b"p":
        anim = 1

    if key == b"s":
        anim = 0

    if key == GLUT_KEY_RIGHT:
        anim_squ = 1

    if key == GLUT_KEY_LEFT:
        anim_squ = 2

    if key == b"q":
        sys.exit()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    # glutInitWindowPosition(0, 0)
    glutInitWindowSize(700, 700)
    glutCreateWindow(b"Big Bang")
    #glutFullScreen()
    display(level2)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(keyboard)
    #glutMouseFunc(myMouseFunc)
    #lose()
    init()
    texturesWall()
    glutMainLoop()


main()
