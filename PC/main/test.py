from manipulator_3D import *
from python_arduino_bluetooth import *
from I2C import *

from copy import deepcopy

from time import time

def map(x,in_min,in_max,out_min,out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


if __name__ == "__main__":
    
    controller = arduino_bluetooth("00:18:e4:40:00:06")
    controller.start()
    telemetria = simulation_manipulator()
    telemetria.start()
    arduino = arduino_i2c(0x04)
    
    mas = deepcopy(telemetria.angle_mas)
    
    telemetria.angle_mas[1] += 45
    telemetria.angle_mas[3] += 45
    
    t = time()

    while telemetria.enable:
        
        if (time()-t>=0.1): 
            controller.write("")
            t = time()
        input = controller.read_avatar()
        
        if (input!=0):
            # elbow 
            telemetria.angle_mas[2] = map(input[0],850,450,0,90)
            # joystick
            if (abs(input[1]-550)>300): 
                if (input[1]<550): telemetria.angle_mas[0] += 3
                else: telemetria.angle_mas[0] -= 3
            # akselerometr
            telemetria.angle_mas[1] = map(input[6],0,90,0,90)
            telemetria.angle_mas[4] = map(input[4],0,90,0,90)
            telemetria.angle_mas[3] = -map(input[5],0,90,0,90)
            print(input)

            if (mas!=telemetria.angle_mas):
                for i in range(len(mas)):
                    if (mas[i]!=telemetria.angle_mas[i]):
                        arduino.write(i,telemetria.angle_mas[i]+90)
                mas = deepcopy(telemetria.angle_mas)

        '''
        controller.update()
        try:
            
            telemetria.angle_mas[2] = (-controller.joystick[4]+0.5)*150
            telemetria.angle_mas[1] = (controller.joystick[7]+0.3)*100
            # controller.joystick[5]
            telemetria.angle_mas[3] = (-controller.joystick[6])*100
            telemetria.angle_mas[0] += controller.joystick[0]
            
            #print(controller.joystick[6])
            # угол обзора
            #a = 0
            #if (controller.arrow[0][0]!=0): a = 1
            #glRotatef(a, 0, controller.arrow[0][0], 0)
            if (mas!=telemetria.angle_mas):
                for i in range(len(mas)):
                    if (mas[i]!=telemetria.angle_mas[i]):
                        arduino.write(i,telemetria.angle_mas[i])
                mas = deepcopy(telemetria.angle_mas)
        except IndexError: pass
        '''
        
        pygame.time.wait(10) # sleep(0.1)
        
        #print(controller.update())