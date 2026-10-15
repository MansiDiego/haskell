#thinkpython cap 4 y 5
#implementar nuevamente el ejercicio de matriz transpuesta,
#implementar tateti pero en una matriz, y no en una lista
#resolver una carilla de ejercicios de la practica 8

#quiero transponer una matriz

#le paso un numero de columna, y saco elementos de ese numero de columna en particular, y los voy agregando a una lista
def filas_a_columnas(m:list[list[int]])-> list[list[int]]:
    indice_columna : int = 0
    fila : list[int] = m[0]
    matriz_traspuesta : list[list[int]] = []
    matriz = m.copy()

    while indice_columna < len(fila):
        fila_transpuesta:list[int] = []
        for filas in matriz:
            fila_transpuesta.append(filas[indice_columna])#aca podría ir otra condicion random

        matriz_traspuesta.append(fila_transpuesta) 
        indice_columna += 1

    #sale del while y ya tenemos construida nuestra matriz traspuesta
    return matriz_traspuesta




matriz_original2 = [[2,2,2], [3,3,3], [7,7,7]]
#print(filas_a_columnas(matriz_original2)) #deberia devolver: [[2,3,7], [2,3,7], [2,3,7]]
#print(matriz_original2)