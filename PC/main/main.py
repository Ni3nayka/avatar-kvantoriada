from manipulator_3D import *
from joystick import *
from I2C import *

from copy import deepcopy

if __name__ == "__main__":
    
    controller = my_universal_joystick()
    telemetria = simulation_manipulator()
    telemetria.start()
    arduino = arduino_i2c(0x04)
    
    mas = deepcopy(telemetria.angle_mas)
    
    while telemetria.enable:
        
        controller.update()
        
        try:
            # управление манипулятором
            if (controller.button[1]): telemetria.angle_mas[0] += 1
            elif (controller.button[3]): telemetria.angle_mas[0] -= 1
            #angle_mas[1] += controller.arrow[0][1]
            telemetria.angle_mas[1] += controller.joystick[2]
            telemetria.angle_mas[2] += controller.joystick[3]
            telemetria.angle_mas[3] += controller.joystick[0]
            telemetria.angle_mas[5] += controller.joystick[1]
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
        
        pygame.time.wait(10) # sleep(0.1)
        
        #print(controller.update())