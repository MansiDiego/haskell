from queue import Queue as cola

#segundo cuatrimestre de 2024;
#me quedo con la primer subsecuencia mas larga que encuentro y devuelvo una tupla que contiene(len de la secuencia)
def subsecuencia_mas_larga(s:list[int])-> tuple[int, int]:
    # para el caso base, que  deberia devolver (1,0)
    mejor_largo  = 1
    mejor_indice = 0

    largo_actual  = 1
    indice_actual = 0

    for i in range(1, len(s), 1):
        if todos_consecutivos([s[i - 1], s[i]]):
            largo_actual +=  1
        else:
            if largo_actual > mejor_largo:
                mejor_largo  = largo_actual
                mejor_indice = indice_actual

            #en cualquier caso, cada vez que se encuentra una nueva secuencia nos fijamos el largo(reseteamos su valor), y indexamos su indice(lo almacenamos en memoria)
            largo_actual = 1
            indice_actual = i

    if largo_actual > mejor_largo:
        mejor_largo = largo_actual
        mejor_indice = indice_actual

    return mejor_largo, mejor_indice

#aux todos_consecutivos:
def todos_consecutivos(s: list[int])-> bool:
    longitud = len(s) - 1
    for i in range(0, longitud, 1):
        if not( s[i] - s[i + 1] == 1 or s[i + 1] - s[i] == 1):
            return False
    return True
    

# # print(todos_consecutivos([-10, 2,1,2,1,]))
# # #con esto me saco un 
# res_1 = subsecuencia_mas_larga([3, 2, 1])
# print(res_1) #resultado_esperado (3,0)

# res_2 = subsecuencia_mas_larga([-10, 2,1,2,1, 1,2,1,2])
# print(res_2) #resultado_esperado (4,1)

# res_3 = subsecuencia_mas_larga([-2, -1, 0, 1, 0, -1, 0, 1, 2])
# print(res_3) #resultado_esperado (10,1)


##--##
#ejercicio2
#examenes tipo in
#   requiere:{ Cada elemento de examenes es no vacío y tiene longitud par }
#   asegura: { res tiene la misma cantidad de elementos que examenes }
#   asegura: { res[i] es igual a la máxima cantidad de respuestas correctas que Ana podría haber respondido en el i-ésimo exámen resuelto en examenes, para 0 <= i < cantidad de elementos de examenes }
# }
#tengo que devolver la cantidad de respuestas posibles(correctas) por examen, por ej

ana = cola()
ana.put([True, False, True, True])
ana.put([True, False, True, True])
ana.put([True, False, True, True])

def mejor_resultado_ana(examenes:cola[list[bool]])-> list[int]:
    examenes_respaldo : cola[list[bool]] = cola()
    res : list[int] = []

    while not examenes.empty():
        examen = examenes.get()
        examenes_respaldo.put(examen)
        cantidad_respuestas = nota_por_examen(examen)
        res.append(cantidad_respuestas)

    while not examenes_respaldo.empty():
        examen = examenes_respaldo.get()
        examenes.put(examen)

    return res

def nota_por_examen(s:list[bool])-> int:
    correctas = 0
    correctas_false = 0
    
    for elementos in s:
        if elementos == True:
            correctas += 1
        
        else:
            correctas_false += 1
    
    optimista = len(s) // 2
    if correctas > correctas_false:
        minimo = correctas_false
    else:
        minimo = correctas


    if correctas == optimista:
        return len(s)
    else:
        return optimista + minimo

    
    
# res = mejor_resultado_ana(ana)
# print(res)#deberia devolverme [3,3,3]


##3##
#asegura: para todo m[i][j] != m[i][j]M@pre

def modificar_matriz(m:list[list[int]]):
    ultimo_elemento = m[-1][-1]
    ultima_fila     = m[-1]
    hasta : int  = -1
    paso : int   = -1
    inicio : int = len(ultima_fila) - 1

    for fila in range(inicio, hasta, paso):
        for columnas in range( inicio, -1, -1):
            
            if columnas == 0 and fila == 0:
                m[0][0] = ultimo_elemento

            elif columnas == 0:
                m[fila][columnas] = m[fila - 1][-1] 

            else:
                m[fila][columnas] = m[fila][columnas - 1]#se me va de indice

mattriz_random = [[1,2,3], [4,5,6], [7,8,9]]
modificar_matriz(mattriz_random)
print(mattriz_random)


##falta el 4 y repasar el 3
def palabras_por_vocales(palabra: str)-> dict[int, int]:
    res : dict[int, int]= {}
    cantidad_de_vocales_por_palabra : int = 0
    vocales : str = "aeiouAEIOU"
    palabra_limpia : str = espacios_igual_a_1(palabra) #tiene un solo espacio

    for caracteres in palabra_limpia:  
        if caracteres in vocales:
            cantidad_de_vocales_por_palabra += 1

        #termino la palabra, me fijo la cantidad de vocales, y la agrego a donde corresponde
        elif caracteres ==" ":
        #esto seria en el caso de que la clave(que es la cantidad de vocales que tiene una palabra random) existe en dict
            if cantidad_de_vocales_por_palabra not in res.keys():
                res[cantidad_de_vocales_por_palabra] = 1

        # en el caso de que la clave no exista, creamos la clave y le agregamos el valor.
            elif cantidad_de_vocales_por_palabra in res.keys():
                cantidad_de_palabras = res[cantidad_de_vocales_por_palabra] 
                res[cantidad_de_vocales_por_palabra] = cantidad_de_palabras + 1

            cantidad_de_vocales_por_palabra = 0 #para contar nuevamente la cantidad de vocales que tiene la nueva palabra

    #para la ultima palabra, que no finaliza con un espacio
    if cantidad_de_vocales_por_palabra not in res.keys():
                res[cantidad_de_vocales_por_palabra] = 1

    elif cantidad_de_vocales_por_palabra in res.keys():
                cantidad_de_palabras = res[cantidad_de_vocales_por_palabra] 
                res[cantidad_de_vocales_por_palabra] = cantidad_de_palabras + 1

    return res


#algoritmo para sacar espacios, bello
def espacios_igual_a_1(palabra:str)-> str:
    res =""
    for caracteres in palabra:
        if caracteres != " ":
            res += caracteres
        
        elif caracteres == " " and res[-1]!=" ":
            res += caracteres

        else:
            pass
    return res

##observaciones: el ejercicio de pilas es muy accesible y el de diccionarios tambien, estrategia, encarar primero esos ejercicios, y luego considerar matrices antes que "subsecuenias"


