import socket

host = socket.gethostname()
port = 5656
buffer_size = 1024
print('Nombre:')
m = input()
print('Apellido:')
n = input()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:

    socket_tcp.connect((host, port))
    socket_tcp.send(m.encode('utf-8'))
    socket_tcp.send(n.encode('utf-8'))
    data = socket_tcp.recv(buffer_size)

