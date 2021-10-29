from I2C import arduino_i2c
from server import my_server
from copy import deepcopy
from time import sleep
from camera import my_camera
from python_arduino_USB_plus import arduino_usb

if __name__ == "__main__":
    server = my_server() 
    server.start()
    
    arduino = arduino_i2c(0x04)

    platforma = arduino_usb('/dev/ttyUSB0')
    platforma.start()
    
    camera = my_camera(600)
    camera.start()
    
    servo = [90,90,90,90,45]
    devise = [0,0,0]
    
    while False:
        for i in range (5):
            if (servo[i]!=server.array[0][i]):
                servo[i] = server.array[0][i]
                arduino.write(i,server.array[0][i])
        for i in range (3):
            if (device[i]!=server.array[1][i]):
                device[i] = server.array[1][i]
                platforma.write(10+i,server.array[1][i])
        #sleep(0.5)
        
    camera.enable = False
    
    
    
