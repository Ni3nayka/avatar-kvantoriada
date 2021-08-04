import pygame #############seoighes;oreshr;ogiher
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def Cube(vertices, edges):
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    vertices = (
        (1.0, -1.0, -1.0),
        (1.0, 1.0, -1.0),
        (-1.0, 1.0, -1.0),
        (-1.0, -1.0, -1.0),
        (1.0, - 1.0, 1.0),
        (1.0, 1.0, 1.0),
        (-1.0, -1.0, 1.0),
        (-1.0, 1.0, 1.0),
        (-3.0, -3.0, 3.0) ##
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
        (1, 4), ##
        (5, 7),
        ##
        (1,8),
        (7,8),
        (5,8)
    )

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, -1.0, -10)
    glRotatef(20, 10, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #glRotatef(1, 0, 1, 0)
        glRotatef(-1, 100, 100, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube(vertices, edges)
        pygame.display.flip()
        pygame.time.wait(10)

main()