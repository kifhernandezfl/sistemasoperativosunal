import socket
import struct
import os

host = '127.0.0.1'
port = 5656
buffer_size = 1024

def enviar(server: socket.socket, name):

    filesize = os.path.getsize(name)

    server.send(struct.pack("<Q", filesize))
    
    with open(name, "rb") as f:
        while read_bytes := f.read(1024):
            server.send(read_bytes)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:

    socket_tcp.connect((host, port))
    enviar(socket_tcp, "Punto4.txt")