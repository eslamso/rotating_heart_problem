from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import cos, sin, pi
global theta,rangle
rangle=0
theta=0.45
def draw_heart():
    global theta
    glColor(1,0,0,0)
    glBegin(GL_LINE_STRIP)
    for i in range(0, 1000, 1):  # 10, 20, 30, 40  => 50, 60, 70, 80
        x=0.5*(sin(theta*(pi)/180*i))**3
        y= 0.40625*cos(theta*(pi)/180*i)-0.15625*cos(2*theta*(pi)/180*i)-0.0625*cos(3*theta*(pi)/180*i)-0.03125*cos(4*theta*(pi)/180*i)
        glVertex2d(x,y)

    glEnd()



def InitGL(Width, Height):

    glClearColor(1.0, 1.0, 1.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # not necessary
    # gluPerspective(120.0, Width / Height, 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()  # not necessary
    #gluLookAt(0.2, 0.1, 0.1, 0, 0, 0, 0, 1, 0)
    # glEnable(GL_DEPTH_TEST)



def Draw():
    global rangle
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glColor(0,0,0,0)
    ######################
    ##drawpoint
    ###################
    glBegin(GL_POINTS)
    glVertex(0.25,0.2,0)
    glEnd()
    glTranslate(0.25, 0.2, 0)
    glRotate(rangle,0.25,0,1)
    glTranslate(-0.25, -0.2, 0)

    # glRotate(rangle,0,0,1)
    draw_heart()
    rangle=rangle+0.2
    glutSwapBuffers()

def main():
    glutInit()
    glutInitWindowSize(600, 600)  # Width,Height. The line gets scaled to the window.
    glutInitWindowPosition(10, 30)  # Controls where the window starts - top-left corner of screen.
    glutInitDisplayMode(GLUT_RGB|GLUT_DOUBLE)
    glutCreateWindow(b'practical')
    glutDisplayFunc(Draw)  # Drawing.
    glutIdleFunc(Draw)  #animation
    InitGL(5, 5)  # Starting position of window on computer screen (top-left corner).
    glutMainLoop()
main()

