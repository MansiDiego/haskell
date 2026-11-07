#idea general, es usar 2 secuencias, la primera la obtengo recorriendo por primera vez el for, y voy comparando en el segundo for, y me voy quedando con la que me sirve
def problema_de_secuencias(s: list[int]) -> list[int]:
    #caso base
    if len(s) <= 1:
        return s

    mejor: list[int] = [s[0]]  #les agrego el primer elemento a ambas
    actual: list[int] = [s[0]]

    for i in range(1, len(s)):
        # Si mantiene el orden con respecto al elemento anterior:
        if s[i] >= s[i - 1]:
            actual.append(s[i])
        
        else:
            # Se rompió la racha: comparamos la racha terminada contra la mejor
            if len(actual) > len(mejor):
                mejor = actual
            # Empezamos una racha nueva con el elemento actual
            actual = [s[i]]

    # Chequeo final obligatorio: por si la racha más larga fue la última
    # (como pasa en [1, 2, 3, 4] o en la que termina al final de la lista)
    if len(actual) > len(mejor):
        mejor = actual

    return mejor
# lista_prueba = [1,2,3,4,0,1,2,3,4,0,1,2,1,2,3,4,4,5,6,7]
# res = problema_de_secuencias(lista_prueba)
# print(res)

##La idea es laburar con 2 secuencias, e ir fijandome si la actual es la mejor##
#####


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

lista_prueba = [1,2,3,4,0,1,2,3,4,0,1,2,1,2,3,4,4,5,6,7]
res = algoritmo_herramienta(lista_prueba)
print(res)














