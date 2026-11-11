##devolver la subsecuencia estrictamente decreciente de mayor longitud, si hay 2 iguales devuelvo la de mayor indice##

def ejercicio1(s:list[int])-> list[int]:
    if len(s)<= 1:
        return s

    secuencia_actual : list[int] = [s[0]]
    mejor_secuencia : list[int] = [s[0]]
        #1 2 3 4 5 No, yo quiero 5 4 3 2 1 "7"
    for i in range(1, len(s), 1):
        if s[i] < s[i - 1]:
            secuencia_actual.append(s[i])

        else:
            if  len(mejor_secuencia) <= len(secuencia_actual):
                mejor_secuencia = secuencia_actual.copy()

            secuencia_actual = [s[i]] #reinicio la secuencia actual desde el elemento que me rompio la condicion 

    
    
    if len(mejor_secuencia) <= len(secuencia_actual):
        mejor_secuencia = secuencia_actual.copy()

    return mejor_secuencia

pruebass_subseq_decrecientes = [5,3,2,1,7,4,3,2,1,2,3]
res_1 = ejercicio1(pruebass_subseq_decrecientes)
print(res_1)


##Mismo problema pero ahora quiero el indice desde donde arranca##
##hacerle un parche para obtener el indice final de la mejor secuencia, en vez del  inicio
def ejercicio1Bis(s:list[int])-> list[int]:

    if len(s) <= 1:
        return s
    
    indice_mejor_secuencia : int = 0
    indice_actual : int = 0
    indice_mejor_final : int = 0
    indice_final_actual : int = 0


    mejor_secuencia : list[int] = [s[0]]
    secuencia_actual : list[int] = [s[0]]

    for i in range(1, len(s), 1):
        if s[i] < s[i-1]:
            secuencia_actual.append(s[i])

        #se rompio
        else:
            indice_final_actual = i - 1

            if len(mejor_secuencia) <= len(secuencia_actual):
                mejor_secuencia = secuencia_actual.copy()
                indice_mejor_secuencia = indice_actual
                indice_mejor_final = indice_final_actual

            secuencia_actual = [s[i]]
            indice_actual = i

    #salgo del for, y puede que mi secuencia actual sea la mas larga pero la ultima, entonces nunca ejecuta el el else, por lo tanto tengo que hacer un if afuera del for para comprobar cual es la mejor

    if len(mejor_secuencia) <= len(secuencia_actual):
        mejor_secuencia = secuencia_actual.copy()
        indice_mejor_secuencia = indice_actual
        indice_mejor_final = indice_final_actual

    return (mejor_secuencia, indice_mejor_final)

pruebass_subseq_decrecientes = [5,3,2,1,7,4,3,2,1,2,3]
res_1Bis = ejercicio1Bis(pruebass_subseq_decrecientes)
print(res_1Bis)

#Me encanto esa estructura


##