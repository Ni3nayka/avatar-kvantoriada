import pygame 
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from joystick import *

def Cube(vertices, edges):
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    
    controller = my_universal_joystick()
    
    vertices = (
        (1.0, -1.0, -1.0),
        (1.0, 1.0, -1.0),
        (-1.0, 1.0, -1.0),
        (-1.0, -1.0, -1.0),
        (1.0, - 1.0, 1.0),
        (1.0, 1.0, 1.0),
        (-1.0, -1.0, 1.0),
        (-1.0, 1.0, 1.0),
        #(-3.0, -3.0, 3.0) ##
    )

    edges = (
        (0, 1),
        (0, 3),
        (0, 4),
        (2, 1),
        (2, 3),
        (2, 7),
        (6, 3),
        (6, 4),
        (6, 7),
        (5, 1),
        (5, 4),
        #(1, 4), ##
        (5, 7)
        ##
        #(1,8),
        #(7,8),
        #(5,8)
    )

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, -1.0, -10)
    glRotatef(20, 10, 0, 0) # делаем чутка пониже

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        controller.update()
        
        a = 0
        if (controller.joystick[0]!=0 or controller.joystick[1]!=0): a = 1 
        glRotatef(a, controller.joystick[1], controller.joystick[0], 0)
        
        #print(vertices[0][0],controller.joystick[2])
        #vertices[0][0]+=controller.joystick[2]
        vertices = (
            (vertices[0][0]+controller.joystick[2]*0.1, -1.0, -1.0),
            (1.0, 1.0, -1.0),
            (-1.0, 1.0, -1.0),
            (-1.0, -1.0, -1.0),
            (1.0, - 1.0, 1.0),
            (1.0, 1.0, 1.0),
            (-1.0, -1.0, 1.0),
            (-1.0, 1.0, 1.0),
            (-3.0, -3.0, 3.0) ##
        )
        #glRotatef(1, 0, 1, 0) # speed x y z
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube(vertices, edges)
        pygame.display.flip()
        pygame.time.wait(10)

main()