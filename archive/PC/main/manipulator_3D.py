from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # чтобы заводских надписей не было
import pygame 
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from math import radians, cos, sin

from threading import Thread

class simulation_manipulator(Thread):
    
    def __init__(self, size_mas=[1,3,3,1,2], angle_mas=[0,0,0,0,0,0]): 
        Thread.__init__(self)
        self.size_mas = size_mas
        self.angle_mas = angle_mas
        #self.view = [0]
        self.enable = True
    
    def run(self): 
        def Cube(vertices, edges):
            glBegin(GL_LINES)
            for edge in edges:
                for vertex in edge:
                    glVertex3fv(vertices[vertex])
            glEnd()
        
        def test_angle(angle_mas):
            for i in range(len(angle_mas)):
                if (angle_mas[i]>90): angle_mas[i]=90
                elif (angle_mas[i]<-90): angle_mas[i]=-90
        
        def vertices_update(size_mas, angle_mas):
            mas = [(0, size_mas[0], 0)]
            mas.append( (mas[0][0]+size_mas[1]*sin(radians(angle_mas[1]))*cos(radians(angle_mas[0])), mas[0][1]+size_mas[1]*cos(radians(angle_mas[1])), mas[0][2]+size_mas[1]*sin(radians(angle_mas[1]))*sin(radians(angle_mas[0]))) )
            mas.append( (mas[1][0]+size_mas[2]*sin(radians(angle_mas[1]+angle_mas[2]))*cos(radians(angle_mas[0])), mas[1][1]+size_mas[2]*cos(radians(angle_mas[1]+angle_mas[2])), mas[1][2]+size_mas[2]*sin(radians(angle_mas[1]+angle_mas[2]))*sin(radians(angle_mas[0])) ))
            mas.append( (mas[2][0]+size_mas[3]*sin(radians(angle_mas[1]+angle_mas[2]+angle_mas[3]))*cos(radians(angle_mas[0])), mas[2][1]+size_mas[3]*cos(radians(angle_mas[1]+angle_mas[2]+angle_mas[3])), mas[2][2]+size_mas[3]*sin(radians(angle_mas[1]+angle_mas[2]+angle_mas[3]))*sin(radians(angle_mas[0])) ))
            vertices = (
                # основа
                (1, 0, 1),
                (-1, 0, 1),
                (-1, 0, -1),
                (1, 0, -1),
                # насечка
                (1, 0, 0),
                (1.5, 0, 0),
                # манипулятор
                (0, 0, 0),
                mas[0], 
                mas[1], 
                mas[2], 
                mas[3], 
                #mas[4], 
                #mas[5], 
                #mas[6], 
            )
            return vertices
        
        size_mas = self.size_mas
        angle_mas = self.angle_mas
        
        #size_mas = [1,3,3,1,2] # *5 = real
        #angle_mas = [0,0,0,0,0,0]
        
        vertices = vertices_update(size_mas, angle_mas)
        edges = (
            # основа
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 0),
            # насечка
            (5, 4),
            # манипулятор
            (6,7),
            (7,8),
            (8,9),
            (9,10),
            #(8,9),
            #(8,10),
        )

        pygame.init()
        #display = (800, 600)
        display = (200, 200)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

        gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

        glTranslatef(0.0, -5, -20) # x y z перемещение
        glRotatef(20, 0, 10, 0) # step x y z вращение
        #glTranslatef(0.0, -1.0, -10) # делаем чутка подальше

        X = 0
        Y = 0
        
        while self.enable:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #pygame.quit()
                    #quit()
                    self.enable = False
                    
            if (self.enable):
                
                size_mas = self.size_mas
                angle_mas = self.angle_mas
                test_angle(angle_mas)
                
                vertices = vertices_update(size_mas, angle_mas)
                
                glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
                Cube(vertices, edges)
                pygame.display.flip()
                pygame.time.wait(10)

#def main_simulation_manipulator():
    
    

if __name__ == "__main__":
    
    telemetria = simulation_manipulator()
    telemetria.start()
    
    flag = 0
    
    while telemetria.enable:
        
        if flag==0:
            for i in range(4): telemetria.angle_mas[i] += 1
            if telemetria.angle_mas[0]>=90: flag = 1
        else:
            for i in range(4): telemetria.angle_mas[i] -= 1
            if telemetria.angle_mas[0]<=-90: flag = 0
            # угол обзора
            #a = 0
            #if (controller.arrow[0][0]!=0): a = 1
            #glRotatef(a, 0, controller.arrow[0][0], 0)
        
        pygame.time.wait(10) # sleep(0.1)
        
        #print(controller.update())
        
        