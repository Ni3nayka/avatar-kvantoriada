import socket               # Import socket module


class my_client():

    def __init__(self):
        self.s = socket.socket()         # Create a socket object
        self.host = "192.168.43.225" #socket.gethostname() #"192.168.43.225" #socket.gethostname() # Get local machine name
        #self.host = "raspberrypi" #"LAPTOP-V2VL8AV1"
        self.port = 12345                # Reserve a port for your service.

    def send(self, message=[[90,90,90,90,90,90,90,90,90,90],[0,0,0,0,0,0,0,0,0,0]]):
        try:
            self.s.send(b'45 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90')
            print(self.s.recv(1024)) # print(s.recv(1024))
        except ConnectionRefusedError or ConnectionResetError or OSError: 
            print("error connect")

    def connect(self):
        self.s.connect((self.host, self.port))

    def disconnect(self):
        self.s.close

if __name__ == "__main__":

    client = my_client()
    client.connect()
    client.send([[90,90,90,90,90,90,90,90,90,90],[0,0,0,0,0,0,0,0,0,0]])
    client.disconnect()