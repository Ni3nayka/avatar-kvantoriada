'''
This program writing Bakay Egor, Moscow, Russia, 2020
This script is part of the project "PROMETHEUS"
https://www.youtube.com/playlist?list=PL24VxeCr7LD3qzQenzNS4zYKe5VYeBOxw

Info:
https://vk.com/@initblog-peredacha-dannyh-mezhdu-raspberry-pi-i-arduino-po-bluetooth
'''

print("$ import <python_arduino_bluetooth>")

from threading import Thread
from bluetooth import *

def python_arduino_bluetooth_version(S=0):
    version = "1.0"
    if (S==0):
        return version
    if (str(S)==version):
        return 1
    else:
        print("<python_arduino_bluetooth> have more version!!!")
        return 0

class arduino_bluetooth(Thread):
    
    def __init__(self,com): 
        Thread.__init__(self)
        self.ser = BluetoothSocket(RFCOMM)
        self.mas = []
        self.cache = []
        self.enable = 1
        try:
            self.ser.connect((com,1)) # port = 1
        except BluetoothError:
            self.enable = 0
            print("ERROR <python_arduino_bluetooth>: no bluetooth device:", com)

    def port(self):
        return self.enable
    
    #def now_read(self):
    #    return S

    def write(self,S):
        if (not self.enable): return 0
        self.ser.send(S)
        self.ser.send('\n')
    
    def run(self): # Запуск потока ################################################
        if (not self.enable): return 0
        while (1):
            a = self.ser.recv(1)
            if (a!=0):
                if (a==b'\n'):
                    self.mas.append(''.join(self.cache))
                    self.cache.clear()
                else:
                    a = str(a)
                    a = list(a)  # str => mas
                    a = str(a[2])
                    self.cache.append(a)
        sock.close()
            
    def available(self):
        if (not self.enable): return 0
        if (len(self.mas)>0):
            return 1
        else:
            return 0
        
    def read(self):
        if (not self.enable): return 0
        if (len(self.mas)>0):
            S = self.mas[0]
            del self.mas[0]
            return S
        else:
            return 0
        
    def wait_read(self):
        if (not self.enable): return 0
        while (len(self.mas)==0): pass
        S = self.mas[0]
        del self.mas[0]
        return S


if __name__ == "__main__":
    #main()
    arduino = arduino_bluetooth("00:19:09:01:12:61")
    arduino.start()
    arduino.write("test - 1")
    arduino.write("test - 2")
    while (1):
        if (arduino.available()):
            print(arduino.read())
