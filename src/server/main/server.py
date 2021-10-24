import socket               # Import socket module
from copy import deepcopy
from threading import Thread

class my_server(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        self.s = socket.socket()            # Create a socket object
        self.host = "192.168.43.231" #socket.gethostname()    # Get local machine name
        self.port = 12345                   # Reserve a port for your service.
        self.s.bind((self.host, self.port)) # Bind to the port
        self.s.listen(5)                    # Now wait for client connection.

        if True:
            print("SERVER start:")
            print("host:",self.host)
            print("port:",self.port)

        self.array = [[90,90,90,90,90,90,90,90,90,90],[0,0,0,0,0,0,0,0,0,0]]

    def run(self):
        while True and 1:
            c, addr = self.s.accept()     # Establish connection with client.
            #print ('Got connection from', addr)
            try:
                while True:
                    a = c.recv(1024)
                    c.send(b'Thank you for connecting')
                    if a!=b'':
                        a = a.decode('UTF-8')
                        a=list(map(int,list(a.split())))
                        a = [a[0:10],a[10:20]]
                        #print(a)
                        if self.array!=a:
                            self.array = deepcopy(a)
                            print(self.array)
                #break
            except ConnectionAbortedError and BrokenPipeError: c.close()  # Close the connection 
            #print ('stop connection from', addr)       

if __name__ == "__main__":
    server = my_server() # SETUP
    server.start()       # LOOP


