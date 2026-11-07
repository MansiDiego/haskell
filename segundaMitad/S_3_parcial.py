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
#es procedimiento, no tiene retorno
def cambiar_matriz(A: list[list[int]]) -> None:
    ultimo = A[-1][-1]

    for i in range(len(A) - 1, -1, -1):
        for j in range(len(A[i]) - 1, -1, -1):

            if i == 0 and j == 0:
                A[i][j] = ultimo
            elif j == 0:
                A[i][j] = A[i - 1][-1]
            else:
                A[i][j] = A[i][j - 1]


matriz_random = ([[1,2,3],[4,5,6],[7,8,9]])
cambiar_matriz(matriz_random)
print(matriz_random)


##falta el 4 y repasar el 3

