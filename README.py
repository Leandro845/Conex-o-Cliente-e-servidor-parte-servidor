# Conex-o-Cliente-e-servidor-parte-servidor
Parte servidor
#Utilizando TCP/IP

import socket

ip = '0.0.0.0' #Server ip
port = 8888 #Server port

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create the socket
sock.bind((ip, port)) #Slect port and address
sock.getpeername() #Return server ip
sock.listen() #The server starts listening

data, address = sock.accept() #The server accepts the connections
print(f'host: {address}')

while True:
    d = data.recv(9000) #Receive the data
    d.decode() #Decode de data

    print(d)


