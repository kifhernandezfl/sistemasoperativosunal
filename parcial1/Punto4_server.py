import socket
import struct

host = '127.0.0.1'
port = 5656
buffer_size = 1024

def size_file(server: socket.socket):
    
    fmt = "<Q"
    expected_bytes = struct.calcsize(fmt)
    received_bytes = 0
    stream = bytes()

    while received_bytes < expected_bytes:
        part = server.recv(expected_bytes - received_bytes)
        stream += part
        received_bytes += len(part)
    filesize = struct.unpack(fmt, stream)[0]
    
    return filesize


def receive_file(server: socket.socket, name):
    
    filesize = size_file(server)
    
    with open(name, "wb") as f:
        received_bytes = 0
        
        while received_bytes < filesize:
            part = server.recv(1024)
            if part:
                f.write(part)
                received_bytes += len(part)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
    
    socket_tcp.bind((host, port))
    socket_tcp.listen(1)
    print('Esperando conexion')

    conn, addr = socket_tcp.accept()
    
    with conn:
        print('Conexion')
        receive_file(conn, "Punto4_1.txt")
        print("Archivo recibido.")
 
    conn.close()

#SHA1: D1795444C99420BAEA28729A81B4D34C79DF2CAA