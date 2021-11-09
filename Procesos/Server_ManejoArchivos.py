import socket

host = '127.0.0.1'
port = 5656
buffer_size = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
    
    socket_tcp.bind((host, port))
    socket_tcp.listen(1)
    print('Esperando conexion')

    conn, addr = socket_tcp.accept()
    with conn:
        print('Conexion')
        while True:
            data = conn.recv(buffer_size)
            
            if not data:
                break
            else:
                print('Recibido: {}'.format(data.decode('utf-8')))
                k = 'Nombre:' + data.decode('utf-8')

                """f = open ('Persona.txt','w')
                f.write(k)
                f.close()

                f = open ('Persona.txt','r')
                msn = f.read()
                print(msn + ' Leido')
                f.close"""

            conn.send(data)