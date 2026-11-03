##MODOSSS##

#modos: 'r', 'w', 'a', 'rb', la estructura siempre es: archivo = open('nombre del archivo', 'modo' ) para abrir el archivo 
#nota: with open() as alias: realiza el close() de forma automatica al salir del bloque



##METODOS DE LECTURA:

##1##
#alias.read()
#Lee todo el contenido del archivo y lo devuelve como un unico str
#por ej:
#with open("texto.text", "r") as aliasqsy:
    #contenido : str = aliasqsy.read() #use el metodo read

##2##
#alias.readline()
#Lee una sola línea desde la posición actual del cursor (incluyendo el salto de línea \n al final). Al llegar al final del archivo devuelve un string vacío ("").
# with open("texto.txt", "r") as f:
#     linea1: str = f.readline()

##3##
#alias.readlines()
#Lee todas las líneas restantes y las devuelve dentro de una lista de strings (list[str]), donde cada elemento conserva su \n.
# with open("texto.txt", "r") as f:
#     lineas: list[str] = f.readlines()





###METODOS DE ESCRITURA###

##1##
#alias.write(cadena)
#Escribe la cadena de texto pasada por argumento. No agrega saltos de línea automáticos; si se necesita cambiar de línea, hay que concatenar explícitamente \n
# with open("salida.txt", "w") as f:
#     f.write("Primera línea\n")


##2##
#alias.writelines(lista_cadenas)
#Escribe una secuencia o lista de strings directamente en el archivo.
# lineas = ["uno\n", "dos\n", "tres\n"]
# with open("salida.txt", "w") as f:
#     f.writelines(lineas)




##MODULOSSSSS##
#Requiere importar la librería con import os.path o import os.

#os.path.exists(path)
#Devuelve True si la ruta o archivo existe en el sistema de archivos, y False en caso contrario.
# import os.path

# if os.path.exists("notas.csv"):
#     print("El archivo existe")


#os.path.join(ruta1, ruta2, ...)
#Concatena componentes de una ruta de forma segura según el separador del sistema operativo actual (/ en Linux/macOS, \ en Windows).
# import os.path
# ruta_completa = os.path.join("carpeta", "datos.txt")




#Ejemplos;

file = open('data1.txt', 'r')#abrimos el documento con el modo 'r' que sea de lecutra(read)
#print(file)
lineas = file.readlines()#el metodo "readlines lee todas las lineas"
print(lineas)#estoy leyendo lo que hay en el archivo data1.txt

siguientes7 = file.read(7)#el metodo read sirve para indicarle cuantos caracteres se quiere leer, (obs:el salto de linea cuaenta como un caracter)

file.close()

with open('data2.txt', 'w') as archivo: #w indica que el modo es de escritura(writing)
    archivo.write('mateo\nhice un salto de linea \ndiego')
