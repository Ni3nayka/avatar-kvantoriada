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
    
    telemetria.angle_mas[1] += 45
    telemetria.angle_mas[3] += 45
    
    while telemetria.enable:
        
        controller.update()
        
        try:
            telemetria.angle_mas[2] = (-controller.joystick[4]+0.5)*150
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