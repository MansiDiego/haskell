#ejercicio 1
def promedio_de_salidas(registro: dict[str, list[int]])-> dict[str, tuple[int, float]]:
    res : dict[str, tuple[int, float]] = {}

    for nombre, listas_de_tiempos in registro.items():
        for tiempo in listas_de_tiempos:
            if tiempo > 0 and tiempo < 61:

                if nombre not in res.keys():
                    res[nombre] = (1, tiempo)

                else: #voy a ir actualizando el promedio por iteracion
                    cantidad_de_salas = res[nombre][0] + 1
                    tiempo_total   = res[nombre][1] + tiempo
                    res[nombre]    = (cantidad_de_salas, tiempo_total)
                        

            #que pasa si el tiempo es >61 o menor a 0 entonces no me modifica el promedio ya que estoy contando la cantidad de salas de las cuales escapo, de las que no escapo no modifican el promedio
            else:
                if nombre not in res.keys():
                    res[nombre] = (0, 0.0)

                #si ya esta no lo agrego, solo debo curbrir el caso, para los jugadores, que no hayan ganado ninguna sala de escape, por lo tanto su promedio es 0 y su cantidad de salidas es 0

    for nombre, tuplas in res.items():
        
        cantidad = tuplas[0]
        sumatoria_tiempo = tuplas[1]
        if cantidad != 0:
            promedio = sumatoria_tiempo / cantidad
            res[nombre] = (cantidad, promedio)
        else:
            pass

    return res


prueba_ejercicio1 = {"Mateo": [30, 20, 33], "Pepe":[0,0,0,61]}
res_ejercicio1 = promedio_de_salidas(prueba_ejercicio1)
print(res_ejercicio1)


###Ejercicio 2##
def tiempo_mas_rapido(s: list[int])-> int:
    mas_rapido = 0
    for i in range(len(s)):
        if s[i] < s[mas_rapido]:
            mas_rapido = i

    return mas_rapido

res_2 = tiempo_mas_rapido([30,1,29,0])
print(res_2)


##Ejercicio 3## Reimplementar usando mi herramienta
def racha_mas_larga(tiempos: list[int])-> tuple[int, int]: 
    indice_actual : int = 0
    indice_del_mejor_incio : int = 0
    indice_del_mejor_final : int = 0
    indice_del_final_de_secuencia_actual = 0
    longitud_de_la_mejor_secuencia = 0
    longitud_de_la_secuencia_actual = 0

    for i in range(len(tiempos)):
        if tiempos[i] > 0 and tiempos[i] < 61:
            longitud_de_la_secuencia_actual += 1
            final_del_for = i
        else:
            indice_del_final_de_secuencia_actual = i 

            if longitud_de_la_mejor_secuencia < longitud_de_la_secuencia_actual:
                longitud_de_la_mejor_secuencia = longitud_de_la_secuencia_actual
                indice_del_mejor_final = indice_del_final_de_secuencia_actual
                indice_del_mejor_incio = indice_actual
            
            if len(tiempos) - 1 != i:
                indice_actual = i + 1
 
            longitud_de_la_secuencia_actual = 0
            
    if longitud_de_la_mejor_secuencia < longitud_de_la_secuencia_actual:
        longitud_de_la_mejor_secuencia = longitud_de_la_secuencia_actual
        indice_del_mejor_final = final_del_for
        indice_del_mejor_incio = indice_actual

    return  (indice_del_mejor_incio, indice_del_mejor_final)

tiemposss = [1,2,3,4,61,1,2,3,4,61,1,2,3,4,5,6,7,8,9]
res_3 = racha_mas_larga(tiemposss)
print(res_3)



##4##
def escape_en_solitario (amigos_por_salas:list[list[int]]) -> list[int]:
    #la longitud de cada fila es 4
    res :list[int] = []

    for fila in range(len(amigos_por_salas)):
        if amigos_por_salas[fila][0] == 0 and amigos_por_salas[fila][1] == 0 and amigos_por_salas[fila][3] == 0 and amigos_por_salas[fila][2] !=0:
            res.append(fila)
    
    return res

salas_de_escape_ejer4 = [[0,0,22,0],[3,3,3,3],[3,3,3,3],[0,0,3,0]]
res_4 = escape_en_solitario(salas_de_escape_ejer4)
print(res_4)
#me devolvio las salas donde escaparon "solitariamente"

#5 choices:
#A.2
#B.2
#C.1

#tiempo estimado: 1:45h nota:10