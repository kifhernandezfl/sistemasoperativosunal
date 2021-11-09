import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('www.buda.com', 80))
cmd = 'GET https://api.buda.com/#librerias-open-source HTTP/1.0\r\n\r\n'.encode('utf-8')
server.send(cmd)

while True:
    datos = server.recv(512)
    if len(datos) < 1:
        break
    txt = datos.decode('utf-8')
    f = open ('Punto 2.txt','w')
    f.write(txt)
    f.close()

server.close()

#SHA1: 70BB76A1416BFFAA2FF6CA287AD9B3242117ECAB