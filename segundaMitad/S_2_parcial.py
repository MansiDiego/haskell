from queue import Queue 

#primer cuatri de 2025, tema2:

#Ejercicio 1(2 puntos):
#requier = TRUE
#res es igual a la cantidad de parejas que suman el valor n pasado por argumento
#por ejemplo : cantidad_parejas_que_suman([1,3,2,5,4,8], 5) debe devolver 2
def cantidad_de_parejas_que_suman(s: list[int], n: int )-> int:
    cantidad_de_parejas : int = 0
    longitud : int  = len(s) - 1 

    for i in range(0, longitud, 1): #(inicio, final, paso)
        inicio : int = i + 1 #esto me sirve para que el siguiente for arranque desde aca

        for indice in range(inicio, len(s) , 1): #lo mismo(inicio, final, paso) recordar que los argumentos son enteros
            if s[i] + s[indice] == n:
                cantidad_de_parejas += 1
        
    return cantidad_de_parejas

resultado_obtenido = cantidad_de_parejas_que_suman([1,3,2,5,4,8], 5)
print(resultado_obtenido) #deberia devolverme 2, pefeeto caballedo!!


##Ejercicio 2  (valor: 2.5)##
#clientes es inout

#req1: son clientes distintos
#req2: la tercera componente de clientes son todos numeros positivos
#req3: existe almenos un elemento(que seria un tripla de str str int), que contiene en c1(segunda componente) /= efectivo y c2 <= 15

#debe devolver el primer nombre que cumpla lo siguiente, que c1 sea distinto de efectivo y c2 sea menor a 15.
# ademas esa tripla debe ser eliminada de la cola
def pasar_por_auto_servicio(clientes: Queue[tuple[str, str, int]]) -> str:
    copia_clientes = Queue()
    cola_bien_formada = Queue()

    while not clientes.empty():
        tripla = clientes.get()
        nombre, modo, cantidad =  tripla
        if modo !="efectivo" and cantidad <= 15:
            nombre_buscado = nombre
            break
        copia_clientes.put(tripla)

    while not copia_clientes.empty():
        triplas = copia_clientes.get()
        cola_bien_formada.put(triplas)

    while not clientes.empty():
        triplass = clientes.get()
        cola_bien_formada.put(triplass)

    while not cola_bien_formada.empty():
        tuplass = cola_bien_formada.get()
        clientes.put(tuplass)

 
    return nombre_buscado #ahora el problema es que modifique la cola y no la deje tal cual

cola_prueba = Queue()
cola_prueba.put(("mauri", "tarjeta", 19))
cola_prueba.put(("jose","efectivo", 18))
cola_prueba.put(("mateo", "tarjeta", 13))


# resultado = pasar_por_auto_servicio(cola_prueba)
# print(resultado)
# print(cola_prueba.queue)


##Ejercicio 3 (valor = 2.5)##
#todas las filas de a tienen la misma longitud
#coll >=0 y coll<len(primer fila)
#col2 >=0 y col2<len(primer fila)
#coll y col2 son distintos

def ejercicio3(m: list[list[int]], col1: int, col2:int):#es un procedimiento
    ultima_fila : int = len(m) - 1 #es un indice
    primer_elemento : int  = extrae_el_elemento_de_fila_en_columna_indice(m[ultima_fila], col1)
    segundo_elemento : int = extrae_el_elemento_de_fila_en_columna_indice(m[ultima_fila], col2)
    for filas in m:
        filas[col1] = segundo_elemento
        filas[col2] = primer_elemento

#Importante el indice no debe estar fuera de rango
def extrae_el_elemento_de_fila_en_columna_indice(fila:list[int], indice:int)-> int:
    longitud = len(fila)

    for i in range(longitud):
        if i== indice:
            return fila[indice]

matriz_prueba = [[1,2,3],[40,50,60], [-7,-8,-9]]
ejercicio3(matriz_prueba, 1, 2)
print(matriz_prueba)