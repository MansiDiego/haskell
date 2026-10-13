import random
##EJERCICIO 2##;
#tipo inout
def cero_en_posición_pares_1(s:list[int])->None:
    for contador in range(0,len(s)):
        if contador % 2 == 0:
            s[contador] = 0
    
mi_lista = [1,2,3,4,5,1]
cero_en_posición_pares_1(mi_lista)
print(mi_lista)



#tipo in
def cero_en_posicion_pares_2(s:list[int])->list[int]:
    res: list[int] = s.copy() #estamos haciendo pasaje por copia, la lista que recibimos copiamos sus valores en una nueva variable con distinta posicion en memoria
    longitud = len(res)
    
    for i in range(longitud):
        if i % 2 == 0:
            res[i] = 0
    return res
        
mi_lista2 = [1,2,3,4,5,6]
print(cero_en_posicion_pares_2(mi_lista2)) #PAKSA
print(mi_lista2)#FIJATE QUE LA LISTA SIGUE CON SUS MISMOS VALORES


#EJERCICIO 3 el param es de tipo "IN"
def sin_vocales(entrada: str) -> str:
    vocales : str = "aeiou"
    palabra_sin_vocales =""
    for elemento in entrada:
        if elemento not in vocales: #not in == no esta en :
            palabra_sin_vocales += elemento
    return palabra_sin_vocales

#random = "mateo"
#print(sin_vocales(random))
#print(random)

#EJERCICIO 4            
def remplazo(entrada: str) -> str:
    vocales : str = "aeiou"
    palabra_sin_vocales_con_guiones =""
    
    for elemento in entrada:
        if elemento not in vocales: #not in == no esta en :
            palabra_sin_vocales_con_guiones += elemento
        else:
            palabra_sin_vocales_con_guiones += "-"
            
    return palabra_sin_vocales_con_guiones

random_con_guion = "mateo"
print(remplazo(random_con_guion))
print(random_con_guion)


##EJERCICIO 5
#param tipo in
def da_vuelta_str(palabra: str) -> str:
    resultado : str = ""
    for indice in range(len(palabra)) :
        resultado += palabra[len(palabra) - indice - 1]
        
    return resultado
    

palabra_X = "plato"
print(da_vuelta_str(palabra_X))
print(palabra_X)

#EJERCICIO 2.6
def eliminar_repetidos(s:str)-> str:
    res : str =""
    for elemento in s: #donde elemento seria un caracter del string
        if elemento not in res:
            res = res + elemento
    return res
    
palabra_a_repeti = "gorlomi"
print(eliminar_repetidos(palabra_a_repeti))
print(palabra_a_repeti)




##EJERCICIO 3##
def resultadoMateria(notas:list[int])-> int:
    s = notas.copy()
    
    if promedio(s) >= 7 and mayores_a_4(notas):
        res = 1
    elif (promedio(s) > 4 and promedio(s) <= 7) and mayores_a_4(notas):
        res = 2
    elif (promedio(s) < 4) or not mayores_a_4(notas):
        res = 3
        
    return res   
                
                
                
                  
#auxiliar todos mayores que 4
def mayores_a_4(s:list[int])-> bool:
    for elemento in s:
        if elemento < 4:
            return False
    return True

#auxiliar promedio
def promedio(s:list[int])->int:
    cantidad_materias :int = 0
    sumatoria :int = 0
    
    for elemento in s:
        sumatoria += elemento
        cantidad_materias += 1
        
    res = sumatoria / cantidad_materias
    
    return res

#print(promedio([7,6,7,6]))  
#print(mayores_a_4([4,4,8]))
pepito_notas = [7,6,5,10]
print(resultadoMateria(pepito_notas))
print(pepito_notas) #verifico que no haya modificado la lista original, porque el parametro es tipo in



##EJERCICIO 4##
def saldo_Actual(movimientos:list[tuple[str, int]])-> int:
    s = movimientos.copy()
    saldo :int = 0
    
    for elemento in s:
        saldo += tipo_operacion(elemento)    
    
    return saldo

#Auxiliar: "tipo de operacion"
def tipo_operacion(datos: tuple[str, int]) -> int:
    operacion, valor = datos
    saldo_actual : int = 0
    if operacion == "I":
        saldo_actual = valor
    if operacion == "R":
        saldo_actual = -valor
    return saldo_actual 

#print(tipo_operacion(("R", 200)))
billetera_mateo = [("I", 1000), ("R", 500), ("I", 150), ("R", 50)]
print(saldo_Actual(billetera_mateo))
print(billetera_mateo)#para verificar que el param pasado es de tipo in



##EJERCICIO 5 MATRICES##    
def pertenece_a_cada_uno_version_1(entradin:list[list[int]], ein:int, outres:list[bool])->None:
    m : list[list[int]] = entradin.copy()
    x : int = ein
    res : list[bool] = []
    outres.clear()
    
    for fila in m:
        if peretenece_en(fila, x):
            outres.append(True)
        else:
            outres.append(False)
    #no devuelve nada, xq es un procedimiento y no una funcion 
    #porque el parametro de la lista de bool es out, entonces no lo debo leer, pero si lo debo modificar
    
    
    
        
#auxiliar pertenece:
def peretenece_en(s:list[int], e:int)->bool:
    for elemento in s:
        if elemento == e:
            return True
    return False

outres = [True, True, True]
matriz = [[1,2,3], [4,5,6], [7,8,9]]
pertenece_a_cada_uno_version_1(matriz, 3, outres)
print(matriz)
print(outres)



#ejercicio 5.2
def pertenece_version_2(s:list[list[int]], e:int, o:list[bool]):
    o.clear()
    for fila in s:
        if peretenece_en(fila, e):
            o += [True]
        else:
            o += [False]
      
    #no devuelve nada
matriz_version_2 =[[1,2,2], [1,3,3], [1,2,3]]    
lista_de_bol = [False, False, False]
pertenece_version_2(matriz_version_2, 2, lista_de_bol)
print(lista_de_bol)
#importante diferenciar listas de procedimientos

#ejercicio 5.3
def pertenece_version_3(m:list[list[int]], e:int, o:list[bool]):
    o.clear()
    contador = 0
    longitud = len(m[0])
    
    while contador < longitud:
        if peretenece_en(m[contador], e):
            o.append(True)
        else:
            o.append(False)
        contador += 1

        
mr = [[1,2,3], [4,4,4], [2,3,4]]
lsr = [True, True, True]
pertenece_version_3(mr, 4, lsr)
print(lsr)
print(mr)


##EJERCICIO 6
#6.1;
def es_matriz_cuadrada(s:list[list[int]])->bool:
    m : list[list[int]] = s.copy()
    primer_fila : list[int] = m[0]
    if len(primer_fila) > 0:
        for filas in range(len(m)):
            if len(m[filas]) != len(primer_fila): #Comparo todas las filas contra la longitud de la primer fila
                return False
    return True                 

matriz_2 = [[1,2,3], [3,3,3], [7,7,7]]
print(es_matriz_cuadrada(matriz_2))#deveria devolverver true

#6.2 "filas ordenadas"
def filas_ordenadas(m: list[list[int]], res: list[bool]):
    res.clear()
    s = m.copy()
    for fila in s:
        if ordenada(fila):
            res.append(True)
        else:
            res.append(False)
            
def ordenada(fila:list[int])->bool:
    longitud = len(fila) - 1
    for index in range(longitud):
        if fila[index] > fila[index + 1]:
            return False
    return True


matriz_ordenada = [[1,2,3], [3,2,1], [1,2,3]]
outparam = [True, True, True]
filas_ordenadas(matriz_ordenada, outparam)
print(outparam)#deberia darme true, false, true.

#6.3
#m: in, #c: in
#devuelve los elementos de la columna c, donde c seria un indice
def columna(m : list[list[int]], c: int) -> list[int]:
    res : list[int] = []
    for fila in m:
        res.append(columna_correcta(fila, c))
        
    return res
    
#aux    
def columna_correcta(fila: list[int], columna:int)-> int:
    for indice in range(len(fila)):
        if columna == indice:
            return fila[indice]


matriz_2_valida = [[1,2,7], [1,2,7], [1,2,7]]
print(columna(matriz_2_valida, 2)) #me deveria devolver [7,7,7]


#6.4
#Columnas ordenadas
# in: m, es funcion(tiene retorno)
def columnas_ordenadas(m :list[list[int]])-> list[bool]:
    res : list[bool] = []
    columna_indice = 0
    
    while columna_indice < len(m[0]):
        columnas_de_la_matriz = columna(m ,columna_indice) #esto me devuelve todos los elementos pertenecientes a una columna en formato lista
        if ordenada(columnas_de_la_matriz):
            res.append(True)
        else:
            res.append(False)        
        columna_indice += 1
    return res

matriz_columna_ordenada = [[1,2,3], [2,3,4], [3,4,5]] 
matriz_columna_desordenada = [[3,4,5], [2,3,4], [1,2,3]]
una_si_una_no = [[1,3],[2,2]]

# print(columnas_ordenadas(matriz_columna_ordenada)) #deveria devolverme true, true, true
# print(columnas_ordenadas(matriz_columna_desordenada)) #deveria devolverme false, false, false
# print(columnas_ordenadas(una_si_una_no)) #me devuelve true, false
# print(matriz_columna_ordenada)

#6.5, transponer, es decir cambiar las columnas de la matriz por filas
def transponer(m: list[list[int]]) -> list[list[int]]:
    matriz : list[list[int]] = m.copy()
    res : list[list[int]]    = []
    columna_indice : int     = 0

    while columna_indice < len(matriz[0]): #gracias a la condicion de que la matriz es cuadrada, por ende la longitud de su fila = longitud de su columna
        columna_transpuesta_ahora_es_fila = columna(matriz, columna_indice)
        res.append(columna_transpuesta_ahora_es_fila)
        columna_indice += 1
        
    return res

matriz_original = [[7,7,7], [5,5,5], [3,3,3]]
#print(transponer(matriz_original)) #use la orignal como dato, pero el pasaje fue por copia, por lo tanto genere una nueva sin modificar la orignal
#print(matriz_original) #me fijo que no haya modificado la original


#6.6 TA-TE-TI TRADICIONAL
def quien_gana_tateti(m: list[str])-> int:
    matriz_copia = m.copy()
    ganador : int = resultado(matriz_copia)
    
    if ganador == "O":
            res = 0
    elif ganador == "X":
            res = 1
    else:
            res = 2
    
    return res            
    
def resultado(m :list[str]) -> str:
    
    jugador1 : str = "X"
    jugador2 : str = "O"
    sin_jugador : str = ""
    index_componente = 0
    res : str = sin_jugador
    
    # se fija si gana por filas
    while index_componente < len(m) :
        #gana jugador 1, con filas horizontales
        if (m[0] == jugador1) and (m[index_componente] == m[index_componente + 1] == m[index_componente + 2]):
            res = jugador1
        elif (m[3] == jugador1) and (m[index_componente] == m[index_componente + 1] == m[index_componente + 2]):
            res = jugador1
        elif (m[6] == jugador1) and (m[index_componente] == m[index_componente + 1] == m[index_componente + 2]):
            res = jugador1
            
        #gana jugador 2, con filas horizontales
        if (m[0] == jugador2) and (m[index_componente] == m[index_componente + 1] == m[index_componente + 2]):
            res = jugador2
        elif (m[3] == jugador2) and (m[index_componente] == m[index_componente + 1] == m[index_componente + 2]):
            res = jugador2
        elif (m[6] == jugador2) and (m[index_componente] == m[index_componente + 1] == m[index_componente + 2]):
            res = jugador2
            
        index_componente += 3 #mas 3 porque hace los saltos por fila, la primer fila tiene 3 elementos y asi sucesivamente
        
    # se fija si gana por columnas
    while index_componente < len(m):
        #gana el jugador 1, con columnas verticales
        if (m[0] == jugador1)   and ( m[index_componente] == m[index_componente + 3] == m[index_componente + 6]):
            res = jugador1
        elif (m[1] == jugador1) and ( m[index_componente] == m[index_componente + 3] == m[index_componente + 6]):
            res = jugador1
        elif (m[2] == jugador1) and ( m[index_componente] == m[index_componente + 3] == m[index_componente + 6]):
            res == jugador1
            
        #gana el jugador 2, con columnas verticales
        if (m[0] == jugador2)   and ( m[index_componente] == m[index_componente + 3] == m[index_componente + 6]):
            res = jugador2
        elif (m[1] == jugador2) and ( m[index_componente] == m[index_componente + 3] == m[index_componente + 6]):
            res = jugador2
        elif (m[2] == jugador2) and ( m[index_componente] == m[index_componente + 3] == m[index_componente + 6]):
            res = jugador2

        index_componente += 1
        
    #gana por diagonales
    #gana j1
    if m[0] ==  jugador1:
        if m[0] == m[4] == m[8]:#indices de la diagonal
                res = jugador1
    #diagonal de derecha a izq
    elif m[2] == jugador1:
        if m[2] == m[4] == m[6]:
            res = jugador1
    
    #gana por diagonales el jugador 2
    #diagonal de izq a derecha            
    if m[0] ==  jugador2:
        if m[0] == m[4] == m[8]:#indices de la diagonal
                res = jugador2
    #diagonal de derecha a izq
    elif m[2] == jugador2:
            if m[2] == m[4] == m[6]:
                res = jugador2
                
    return res

tateti_gana_j1_por_columnas = ["X", "O", "O", "X", "X", "O", "X", "O", "X"]
#print(resultado(tateti_gana_j1_por_columnas))
tateti_gana_j2_por_diagonal = ["O","X", "X", "X", "O", "X", "O", "X", "O"]
#print(resultado(tateti_gana_j2_por_diagonal))
no_gana_ninguno = ["X", "O", "O", "O", "X", "X", "X", "O", "O"]

#print(quien_gana_tateti(tateti_gana_j1_por_columnas))
#print(quien_gana_tateti(tateti_gana_j2_por_diagonal))
#print(tateti_gana_j1_por_columnas)
#print(tateti_gana_j2_por_diagonal)
#print(quien_gana_tateti(no_gana_ninguno))
#print(no_gana_ninguno)
#OBSERVACIÓN LINDO EJERCICIO PARA TESTEAR MUCHAS COSAS

#ejercicio final, p7
#7.1
def nombre_de_los_estudiantes()->str:
    nombres :str = ""
    entrada = input("ingresa un nombre, si ingresa listo o no ingresa nada, la funcion frenara al instante: ")
    while entrada!="": 
        if entrada !="listo":
            nombres += "" + entrada    
            res = nombres   
        if entrada == "listo":
            return res
        entrada = input("ingresa un nombre, si ingresa listo o no ingresa nada, la funcion frenara al instante: ")
        
    return res
#print(nombre_de_los_estudiantes())

#7.2
def historial_sube()->list[tuple[str, int]]:    
    historial : list[tuple[str, int]] = []    
    operacion = input("Ingrese la operacion que desesa realizar, C D X : ")
    monto = input("Ingresa el monto: ")
    
    while operacion !="X":
        if operacion == "C":
            historial.append([("C", monto)])
            
        if operacion == "D":
            historial.append([("D", monto)]) 
            
        operacion = input("ingresa la operacion que desea realizar, C D X: ")
        if operacion == "X":
            break #tuve que meter un break, porque sino me quiere ejecutar la linea de monto antes de comparar la condicion del bucle.
        monto = input("ingresa el monto: ")    
    return historial  
        
#print(historial_sube())


#7.3
def siete_y_medio()-> tuple[str, list[int]]:
    entrada = input("elija la opción correspondiente, sacar una carta o plantarse: ")
    historial_de_cartas :list[int] = []
    while entrada != "plantarse":
        
        carta_random1 : int = random.randint(1,12)
        historial_de_cartas.append(carta_random1)
        entrada = input("elija la opción correspondiente, sacar una carta o plantarse: ")
        
        if sumatoria(historial_de_cartas) > 7.5:#informamos si el usuario se paso de siete y medio
            break       


    #se planto y nos fijamos si esta por arriba de los 7.5 o por debajo
    if sumatoria(historial_de_cartas) > 7.5:
        res = ("el usuario perdio",(historial_de_cartas))  
    else:
        res = ("el usuario gano",(historial_de_cartas))        
          
    return res
#aux
def sumatoria(s:list[int])-> float:
    resultado = 0
    for elemento in s:              
        if elemento !=8 and elemento !=9 and elemento <10:      
            resultado += elemento
        elif elemento >= 10 and elemento <=12:
            resultado += 0.5
        else:
            resultado += 0
    return resultado


#print(siete_y_medio())

#7.4
#aux, veo si tiene al menos 1 mayuscula
def tiene_una_mayuscula(s:str)-> bool:
    for caracter in s:
        if caracter > "A" and caracter < "Z":
            return True
    return False
#aux, ve si tiene al menenos una letra minuscula
def tiene_una_minuscula(s:str)->bool:
    for caracter in s:
        if caracter < "A":
            return True
    return False
#aux, veo si tiene al menos un digito numerico
var_digitos = "0123456789"
def tiene_un_digito_numerico(s: str)-> bool:
    if pertenece_para_ultimo_ejercicio(s, var_digitos):
        return True
    else:
        return False 
#aux para recorrer los digitos
def pertenece_para_ultimo_ejercicio(s:str, digitos:str) -> bool:
    for caracter in s:
        for digito in digitos:
            if caracter == digito:
                return True
    return False


#principal:
def fortaleza_psw(contra:str) -> str:
    if tiene_una_mayuscula(contra) and tiene_una_minuscula(contra) and tiene_un_digito_numerico(contra) and len(contra)>8:
        res = "VERDE"
    elif len(contra)< 5:
        res = "ROJO"
    else:
        res = "AMARILLA"
    return res
pwsrd_cacharro = "ojos"
print(fortaleza_psw(pwsrd_cacharro))#rojo
#chao p7!