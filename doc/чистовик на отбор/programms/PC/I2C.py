weufjhkjbvhjvbdfzskhgfbzskbvzsk = True # flag (because i can testing on usualy PC)

try: import smbus
except ModuleNotFoundError:
    weufjhkjbvhjvbdfzskhgfbzskbvzsk = False
    print("WARNING: no I2C")

class arduino_i2c():
    
    def __init__(self,i2c): 
        if (weufjhkjbvhjvbdfzskhgfbzskbvzsk):
            self.bus = smbus.SMBus(1)
        self.SLAVE_ADDRESS = i2c 

    def write(self,servo,angle):
        if (weufjhkjbvhjvbdfzskhgfbzskbvzsk):
            try:
                self.bus.write_byte(self.SLAVE_ADDRESS, servo)
                self.bus.write_byte(self.SLAVE_ADDRESS, angle)
            except OSError: print("ERROR: I2C connect")

if __name__ == "__main__":
    arduino = arduino_i2c(0x04)
    arduino.write(1,80)
    
    