from I2C import arduino_i2c
from server import my_server
from copy import deepcopy
from time import sleep

if __name__ == "__main__":
    server = my_server() 
    server.start()
    
    arduino = arduino_i2c(0x04)
    
    while True:
        for i in range (5): arduino.write(i,server.array[0][i])
        sleep(0.5)
    
    
    