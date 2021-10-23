import socket               # Import socket module
from copy import deepcopy

# SETUP

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
print("start server:")
print("host:",host)
print("port:",port)

servo_array = [90,90,90,90,90,90]
servo_array_last = deepcopy(servo_array)

# LOOP

while True and 1:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   while True:
      print (c.recv(1024))
      c.send(b'Thank you for connecting')
      if servo_array!=servo_array_last:
         print(servo_array)
         servo_array_last = deepcopy(servo_array)
      break
   c.close()                # Close the connection
