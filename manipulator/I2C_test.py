import smbus

class arduino_i2c():
    
    def __init__(self,i2c): 
        self.bus = smbus.SMBus(1)
        self.SLAVE_ADDRESS = i2c 

    def write(self,servo,angle):
        try:
            self.bus.write_byte(self.SLAVE_ADDRESS, servo)
            self.bus.write_byte(self.SLAVE_ADDRESS, angle)
        except OSError: print("ERROR: I2C connect")

if __name__ == "__main__":
    arduino = arduino_i2c(0x04)
    arduino.write(1,80)
    
    