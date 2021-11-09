import hashlib
 
def sha1(fichero):
    fp = open(fichero, "rb")
    buffer = fp.read()
    # sha1
    hashObj = hashlib.sha1()
    hashObj.update(buffer)
    lastHash = hashObj.hexdigest().upper()
    sha1 = lastHash
    fp.close()
    return fichero,sha1

ficheroElegido = input("Introduzca la ruta y nombre de fichero: ")

fichero, ultimoHash = sha1(ficheroElegido)
print("Fichero: " + fichero)
print("SHA1: " + ultimoHash)
