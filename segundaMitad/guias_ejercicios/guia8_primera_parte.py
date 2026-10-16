import random 
from queue import LifoQueue as Pila #importa lifoqueue y le asigna el alias pila

# p = Pila () # crea una pila
# p . put (1) # apila un 1
# elemento = p . get () # desapila
# p . empty () # devuelve true si y solo si la pila esta vacia


def generar_numeros_al_azar(cantidad: int, desde:int, hasta:int)-> Pila[int]:
    p = Pila()
    contador = 1

    while contador <= cantidad:
        numero_aleatorio = random.randint(desde, hasta)
        p.put(numero_aleatorio)
        contador += 1
    return p

mi_pila = generar_numeros_al_azar(5, 0, 11)
#para poder visualizar la pila, importante que luego de usar get, se me desapilo toda la vaina, ademas, las pilas no tiene el atribute len ni copy
while not mi_pila.empty():
    print(mi_pila.get())

