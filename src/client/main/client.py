import socket               # Import socket module

#from random import randint

class my_client():

    def __init__(self):
        self.s = socket.socket()         # Create a socket object
        #self.host = "192.168.43.225" 
        self.host = socket.gethostname() #"192.168.43.225" #socket.gethostname() # Get local machine name
        #self.host = "raspberrypi" #"LAPTOP-V2VL8AV1"
        self.port = 12345                # Reserve a port for your service.

    def send(self, message=[[90,90,90,90,90,90,90,90,90,90],[0,0,0,0,0,0,0,0,0,0]]):
        try:
            m = ' '.join(str(i) for i in message[0]) + " " + ' '.join(str(i) for i in message[1])
            m = bytes(m, encoding='utf-8')
            self.s.send(m)
            #self.s.send(b'45 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90')
            self.s.recv(1024)
            #print(self.s.recv(1024))
        except ConnectionRefusedError or ConnectionResetError or OSError: 
            print("error connect")

    def connect(self):
        self.s.connect((self.host, self.port))

    def disconnect(self):
        self.s.close

if __name__ == "__main__":

    client = my_client()
    client.connect()
    #for i in range (100): client.send([[90,90,90,90,randint(0, 180),90,90,90,90,90],[0,0,0,0,0,0,0,0,0,0]])
    client.send([[90,90,90,90,90,90,90,90,90,90],[0,0,0,0,0,0,0,0,0,0]])
    client.disconnect()