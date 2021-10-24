from I2C import arduino_i2c
from server import my_server
from copy import deepcopy
from time import sleep
from camera import my_camera

if __name__ == "__main__":
    server = my_server() 
    server.start()
    
    arduino = arduino_i2c(0x04)
    
    camera = my_camera(600)
    camera.start()
    
    mas = [90,90,90,90,45,0,0,0,0,0]
    
    while True:
        for i in range (5):
            if (mas[i]!=server.array[0][i]):
                mas[i] = server.array[0][i]
                arduino.write(i,server.array[0][i])
        #sleep(0.5)
        
    camera.enable = False
    
    
    