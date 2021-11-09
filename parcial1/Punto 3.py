import socket

host = '127.0.0.1'
port = 5656
buffer_size = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
    
    socket_tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_tcp.bind((host, port))
    socket_tcp.listen(1)
    print('Esperando conexion')

    conn, addr = socket_tcp.accept()
    with conn:
        print('Conexion')

        while True:
            data = conn.recv(buffer_size).decode('utf-8')
            pag = 'punto3.html'

            try:
              file = open(pag,'rb')
              data = file.read()
              file.close()
              header = 'HTTP/1.1 200 OK\n'
              mimetype = 'text/html'
            
              header += 'Content-Type: ' + str(mimetype) + '\n\n'
            
            except Exception as e:
              header = 'HTTP/1.1 404 Not found\n'
              data = '<html><body>Error 404 Not found</body></html>'.encode('utf-8')

            final_response = header.encode('utf-8')
            final_response += data

            conn.send(final_response)
            conn.close()

#SHA1: 143FF4F84468F4455ECC2A065651D5BBE88CA043