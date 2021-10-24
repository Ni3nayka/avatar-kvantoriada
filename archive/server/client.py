import socket               # Import socket module

s = socket.socket()         # Create a socket object
#host = "192.168.1.62" #socket.gethostname() # Get local machine name
host = "LAPTOP-V2VL8AV1"
port = 12345                # Reserve a port for your service.

try:
    s.connect((host, port))     
    for i in range(10):
        s.send(b'1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20')
        print(s.recv(1024))
    s.close                     # Close the socket when done    
except ConnectionRefusedError or ConnectionResetError: print("connect error") 
