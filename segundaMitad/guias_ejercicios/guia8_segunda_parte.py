from queue import LifoQueue as Pila
from queue import Queue as Cola 
#diccionarios y archivos##:
#Operaciones:
#Inicializar: diccionari_autos = {} (esto seria un diccionario vacio, pero ahora sabemos que diccionari_autos es un diccionario)
#Insercion o actualizacion: d["clave"] = valor (si la clave no exista, entonces la crea y le asigna el valor, pero si la clave ya existe entonces le pisa el valor, es decir lo actualiza)
#Consulta/acceso a un valor de una clave: valor = d["clave"] 
#pertenencia con in, podemos hacer igual que con listas; elemento in d, donde d es un dict. (if "perro" in d:print("Está presente"))
#d.clear vacia el diccionario
#del d["clave"] borra la clave, y por ende el valor que almacenaba
#len(dict) devuelve la cantidad de claves que tiene, no la cantidad de valores, es impórtante esta observacion sutil pero confunza
# dict.items() me da acceso iterable al diccionario

#EJERCICIO 16
#DICCIONARIOS;


def calcular_promedio_por_estudiante(notas: list[tuple[str, int]])-> dict:
    notas_obtenidas = {}
    for alumno, calificacion in notas:
        if alumno in notas_obtenidas: #si mi clave ya esta en el diccionario entonces:
            notas_obtenidas[alumno].append(calificacion) #agregamos a mi lista la calificacion, porque la clave es alumno y el valor es una lista
        else:
            #creamos la lista con el alumno como clave
            notas_obtenidas[alumno] = [calificacion] 


    #calcula el promedio
    for alumno, calificacion in notas_obtenidas.items():#items() hace que mi diccionario sea iterable
        sumatoria_de_calificaciones = 0
        for lista_notas in calificacion:
            sumatoria_de_calificaciones += lista_notas  
        divisor = len(notas_obtenidas[alumno])
        notas_obtenidas[alumno] = sumatoria_de_calificaciones/ divisor

    return notas_obtenidas

notas_randomss = [("sole", 9),("lucas", 10),("sole", 8)]
res = calcular_promedio_por_estudiante(notas_randomss)
print(res)


#EJERCICIO 17

pila_diego = Pila()
pila_diego.put(301060)
pila_diego.put("anime1v")
pila_diego.put("futbol libre")

pila_mateo = Pila()
pila_mateo.put(331060)
pila_mateo.put("animeflv")
pila_mateo.put("al angulo libre")


pila_mansilla = Pila()
pila_mansilla.put("claude")
pila_mansilla.put("gpt")
pila_mansilla.put("stack overflow")

historiales_argumento_dict = {"Diego": pila_diego, "mateo": pila_mateo, "mansilla": pila_mansilla}


def visitar_sitio_web(historiales: dict[str, Pila[str]], usuario:str, sitio:str):#es un procedimiento, no devuelve nada
        if usuario in historiales.keys(): #si usuario es una clave existente entonces... 
            historiales[usuario].put(sitio)

        else: #si usuario no pertenece a usuarios dentro de historiales, entonces creamos una pila que contiene un solo elemento, y ese elemento es una pila
            historiales[usuario] = Pila()
            historiales[usuario].put(sitio)


visitar_sitio_web(historiales_argumento_dict, "mateo", "w3school")#como mateo ya esta deberia agregarme en la pila mateo el elemento w3school
print(pila_mateo.queue)
# print(historiales_argumento_dict["pedro"])

def navegar_atras(historiales: dict[str, Pila], user:str)-> str:
    sitio_en_historial = historiales[user].get()
    return sitio_en_historial

res = navegar_atras(historiales_argumento_dict, "mateo") #esto me deberia devolver w3school
print(res)
print(pila_mateo.queue)

#perfecto

###18.a###
def agregar_producto(inventario: dict[str, dict[str, float | int]], nombre: str, precio: float, cantidad:int):
    inventario[nombre] = {"precio": precio, "cantidad": cantidad} 
    #estoy agregando en el diccionario la clave "nombre que entra como parametro", y le asigo otro diccionario con la clave "precio" el valor de precio que entra como argumento y lo mismo para cantidad, todo dentro de un nuevo diccionario

def actualizar_stock(inventario: dict[str, dict[str, float | int]], nombre: str, cantidad_valor: float):
    inventario[nombre]["cantidad"] = cantidad_valor  #con inventario[nombre] estoy accediendo a la primer clave que tiene como valor un diccionario y con [cantidad estoy accediendo a la clave del 2do diccionario, y recien en ese momento actualizo la cantidad]

def actualizar_precio(inventario: dict[str, dict[str, float | int]], nombre: str, precio_valor: float):
    inventario[nombre]["precio"] = precio_valor #actualizamos la clave "precio" con el argumento precio