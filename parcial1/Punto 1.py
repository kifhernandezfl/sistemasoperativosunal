import pandas as pd

funciones = {'Nombre':['open()', 'close()', 'getpid()', 'rename()', 'remove()'],'Descripcion':["Abre un archivo", "Cierra un archivo", "Devuelve el identificador de proceso del proceso actual", "Cambia el nombre de un archivo", "Elimina un archivo"]}

print(funciones)

func = pd.DataFrame(funciones, columns = ['Nombre', 'Descripcion'])
func.to_excel('Punto 1.xlsx')

func_txt = func.to_string(header=False, index=False)

f = open ('Punto 1.txt','w')
f.write(func_txt)
f.close()

#SHA1
#251CCDDBCD38270E13EECAAE6961DA5632828065