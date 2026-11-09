#ordenada de forma creciente, si hay 2 iguales devuelvo la de menor indice
def algoritmo_herramienta(s:list[int])-> list[int]:
    if len(s) <= 1:
        return s
    
    actual : list[int] = [s[0]]
    mejor  : list[int] = [s[0]]

    for i in range(1, len(s)):
        if s[i] >= s[i - 1]:
            actual.append(s[i])
        else:
            if  len(actual) > len(mejor):
                mejor = actual
                actual = [s[i]] 

    if len(mejor) >= len(actual):
        return mejor
    else:
        return actual

# lista_prueba = [1,2,3,4,0,1,2,3,4,0,1,2,1,2,3,4,4,5,6,7]
# res = algoritmo_herramienta(lista_prueba)
# print(res)

#para el problema de subsecuencias;
def subsecuencia_mas_larga_de_menor_indice(s: list[int]) -> list[int]:
    if len(s) <= 1:
        return s

    mejor_secuencia: list[int] = [s[0]]
    secuencia_actual: list[int] = [s[0]]
    mejor_indice = 0
    indice_actual = 0


    for i in range(1, len(s)):
        if s[i] >= s[i-1]:
            secuencia_actual.append(s[i])
        else:
            if len(secuencia_actual) > len(mejor_secuencia):
                mejor_secuencia = secuencia_actual.copy()
                mejor_indice = indice_actual

            secuencia_actual = [s[i]]#1,2,3,4,1(el 1 es el que rompe el orden)
            indice_actual = i
    # Comprobamos la última secuencia
    if len(secuencia_actual) > len(mejor_secuencia):
        mejor_secuencia = secuencia_actual.copy()
        mejor_indice = indice_actual

    return mejor_secuencia, mejor_indice

# res = subsecuencia_mas_larga_de_menor_indice([1,2,3,4,5,1,3,4,5])
# print(res)


def subsecuencia_mas_larga_de_mayor_indice(s:list[int])->list[int]:
    #caso base
    if len(s)<= 1:
        return s, 0
    
    secuencia_actual :list[int] = [s[0]]
    mejor_secuencia :list[int]  = [s[0]]
    mejor_indice : int = 0
    indice_actual : int = 0

    for i in range(1, len(s)):

        if s[i] >= s[i-1]:
            secuencia_actual.append(s[i])
        else:
            if len(secuencia_actual) >= len(mejor_secuencia):
                mejor_secuencia = secuencia_actual.copy()#no le quiero pasar la posicion en memoria, sino que le quiero pasar el valor
                mejor_indice = indice_actual

            secuencia_actual = [s[i]]
            indice_actual = i

    if len(secuencia_actual) >= len(mejor_secuencia):
        mejor_secuencia = secuencia_actual.copy()
        mejor_indice = indice_actual

    return mejor_secuencia, mejor_indice 

prueba = [1,2,3,1,2,3]
ress_2 = subsecuencia_mas_larga_de_mayor_indice(prueba)
print(ress_2)

##agregar 2 mas, pero que la secuencia sea decreciente y obtener la de menor indice, la secuencia sea decreciente y obtener la de mayor indice
