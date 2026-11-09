#PRIMER CUATRIMESTRE DE 2024!
from queue import Queue as Cola
#valor 1 punto
#fila_clientes es tipo in
def reordenar_cola_priorizando_vips(fila_clientes:Cola[str, str])-> Cola[str]:
    fila_clientes_respaldo : Cola[str, str] = Cola()
    res : Cola[str] = Cola()    

    while not fila_clientes.empty():
        nombre, tipo = fila_clientes.get()
        fila_clientes_respaldo.put((nombre, tipo))
        
        if tipo == "vip":
            res.put(nombre)

    while not fila_clientes_respaldo.empty():
        nombre, tipo = fila_clientes_respaldo.get()
        fila_clientes.put((nombre, tipo))

        if tipo == "comun":
            res.put(nombre)

    return res

# banco_prueba = Cola()
# banco_prueba.put(("mateo", "vip"))
# banco_prueba.put(("enner", "vip"))
# banco_prueba.put(("leo", "vip"))
# banco_prueba.put(("rodo", "comun"))
# res = reordenar_cola_priorizando_vips(banco_prueba)
# print(banco_prueba.queue)


##
# requiere: {Las claves de estrategias tienen longitud mayor a 0}
# requiere: {Los valores de estrategias sólo pueden ser los strings "me desvío siempre" ó "me la banco y no me desvío"
# asegura: {para cada jugador p perteneciente a claves(estrategias), res[p] es igual a la cantidad de puntos que obtuvo al
# finalizar el torneo, dado que jugó una vez contra cada otro jugador}


def torneo_de_gallinas(estrategias: dict[str, str])-> dict[str, int]:
    resultado_torneo : dict[str, int] = {}

    for nombre, habilidad in estrategias.items():
        for nombre2, habilidad2 in estrategias.items():
            
            if nombre != nombre2:
                #(1 si se chocan)
                if habilidad =="me la banco y no me desvío" and habilidad2 =="me la banco y no me desvío":
                    #a ambos jugadores le voy a sacar puntos, les voy a sacar -5 puntos
                    if nombre not in resultado_torneo.keys():
                        resultado_torneo[nombre] = -5


                    elif nombre in resultado_torneo.keys():
                        puntaje = resultado_torneo[nombre]
                        resultado_torneo[nombre] = puntaje - 5

                #(2)
                if habilidad =="me desvío siempre" and habilidad2 == "me desvío siempre":
                    if nombre not in resultado_torneo.keys():
                        resultado_torneo[nombre] = -10


                    elif nombre in resultado_torneo.keys():
                        puntaje = resultado_torneo[nombre]
                        resultado_torneo[nombre] = puntaje - 10

                #(3)
                if habilidad =="me desvío siempre" and habilidad2 == "me la banco y no me desvío":
                    if nombre not in resultado_torneo.keys():
                        resultado_torneo[nombre] = -15

                    elif nombre in resultado_torneo.keys():
                        puntaje = resultado_torneo[nombre]
                        resultado_torneo[nombre] = puntaje - 15

                #(3')
                if habilidad =="me la banco y no me desvío" and habilidad2 == "me desvío siempre":
                    if nombre not in resultado_torneo.keys():
                        resultado_torneo[nombre] = 10

                    elif nombre in resultado_torneo.keys():
                        puntaje = resultado_torneo[nombre]
                        resultado_torneo[nombre] = puntaje + 10

    #No sigue el standard DRY(don't repit yourself (xd?))
    return resultado_torneo

# diccionario_prueba = {"mateo":"me la banco y no me desvío", "pepe":"me desvío siempre", "fulano":"me desvío siempre"}
# res = torneo_de_gallinas(diccionario_prueba)
# print(res)


#3;2puntos
# requiere: {tablero es una matriz cuadrada}
# requiere: {5 <= |tablero[0]| <= 10]}
# requiere: {tablero sólo tiene 'X', 'O' y '' (espacio vacío) como elementos}
# requiere: {En tablero la cantidad de 'X' es igual a la cantidad de 'O' o bien la cantidad de 'X' es uno más que la cantidad de
# 'O'}
# asegura: {res = 1 <==> hay tres 'X' consecutivas en forma vertical (misma columna) y no hay tres 'O' consecutivas en forma
# vertical(misma columna)}
# asegura: {res = 0 <==> no hay tres 'O' ni hay tres 'X' consecutivas en forma vertical}
# asegura: {res = 3 <==> hay tres 'X' y hay tres 'O' consecutivas en forma vertical (evidenciando que beto hizo trampa)}
# }



def quien_gano_el_tateti_facilito(tablero: list[str])-> int:

    beto_hizo_trampa = gano_ana(tablero) and gano_beto(tablero)
    if gano_ana(tablero) and not beto_hizo_trampa:
        res = 1
    elif beto_hizo_trampa:
        res = 3
    else:
        res = 0

    return res

def gano_ana(tablero:list[str])->bool:
    longitud = len(tablero) #puedo hacer esto porque el tablero es cuadrada
    cantidad_cruces : int = 1

    for columna in range(len(tablero)):
        for filas in range(0, longitud - 1, 1):
                if tablero[filas][columna] == tablero[filas + 1][columna] and tablero[filas][columna] =="X":
                    cantidad_cruces +=1
                else:
                    cantidad_cruces = 1

                if cantidad_cruces == len(tablero):
                    return True
        # cantidad_cruces = 1 #restablezco la cantidad original
    return False


def gano_beto(tablero:list[str])->bool:
    longitud = len(tablero) #puedo hacer esto porque el tablero es cuadrada
    cantidad_circulos : int = 1


    for columna in range(len(tablero)):
        for filas in range(0, longitud-1, 1):
                if tablero[filas][columna] == tablero[filas + 1][columna] and tablero[filas][columna] =="O":
                    cantidad_circulos +=1
                else:
                    cantidad_circulos = 1

                if cantidad_circulos == len(tablero):
                    return True
        # cantidad_circulos = 1 #restablezco la cantidad original
    return False

tablero_ana = ["X","X","X","X","X",  "X","O","X","O","X",  "X","O","X","O","X",  "X","O","X","O","X",  "X","O","X","O","X",]
res_tablero = gano_ana(tablero_ana)
print(res_tablero)

#4; 2puntos
def cuantos_palindromos_sufijos(texto: str)-> int:
    sufijo : str =""
    res : int    = 0

    texto_limpio = limpiamos_texto(texto)
    for caracteres in texto_limpio:
        if caracteres !=" ":
            sufijo += caracteres

        if caracteres ==" ":
            if es_palindromo(sufijo):
                res += 1
            sufijo ="" #lo vaciamos de nuevo
            
    return res

def es_palindromo(palabra:str)->bool:
    indice :int = -1
    for caracter in palabra:
        if caracter != palabra[indice]:
            return False
        indice = indice - 1

    return True

#no lo modifico, creo uno a partir de una ya existente
def limpiamos_texto(text: str)-> str:
    res :str =""
    for caracteres in text:
        if caracteres !=" ":
            res += caracteres

        if caracteres ==" " and res[-1]!=" ":
            res += caracteres

        else:#si el anterior caracter si era un espacio entonces lo limpiamos
            pass
    return res



# texto_prueba ="oso oso mateo    oso  pepe"#me rompe la logica que la palabra no esta limpia
# res_12 = cuantos_palindromos_sufijos(texto_prueba)
# print(res_12)


#5, preg teoricas;
#(A)Cual es la funcion de un ciclo en python; la funcion de un ciclo en python es repetir un bloque de instrucciones repetidamente siempre que se cumpla una determinada condicion

#(B)Qué es una variable en python; es una posicon en memoria que puede guardar informacion de diversos tipos de datos, que durante la ejecucion de un programa se puede ir modificando

#(C); 
#nota: 8 2h10min