#NOTA: Las palabras claves no pueden ser utilizadas como nombre de variables
import math
radius = 5
#EJERCICIOS DE THINK-KPYTHON

#1, Calcular el volumen de una esfera de radio 5, obs: formula para una esfera de radio r (4/3 x pi x r^3)
volumen = (4/3) * math.pi * (radius **3) 
##print(volumen)

#2
e1 = math.e ** 2 #(busca en el modulo math, la variable definida como e y la elevamos al cuadrado)
e2 = math.pow(math.e, 2) #aca estamos usando "pow" que basicamente recibe por argumentos el primer elemento que queremos elevar, y el 2do elemento es la potencia
e3 = math.exp(2) #la base es "e" y el argumento que recibe es a lo que lo queremos elevar
print(e1)
print(e2)
print(e3)#tiene menos decimales

#------#
#------#

#Acá arranca la guia 7;
#EJERCICIO 1

#version 1, con un for i in lista, lo que hice fue basicamente recorrer la lista con el for, y si mi elemento pertenece a la lista devuelvo true,y si mi lista esta vacia devuelvo false
def peretenece(s:list[int], e:int)-> bool:
    
    for entero in s:
        if entero == e:
            return True   
            
    return False

print(peretenece([2], 2))

#version 2 con un "for i in range"
def perteneceBis2(s:list[int], e: int) -> bool:  
          
    for indice in range(len(s)):
        if s[indice] == e: #La idea seria que si matchea entonces devuelve true, y sino matchea nunca, entonces devuelve false
            return True
        
    return False
        
print(perteneceBis2([5,3,2], 5))

#version 3 usando un while
def perteneceBis(s:list[int], e:int)-> bool:
    
    longitud = len(s) #len(s) me devuelve la cantidad de elementos que tiene dicha secuencia
    i=0
    while longitud >= 1:
        if s[i] == e: 
            return  True
        i = i + 1                  #quiero que se modifique dentro del while
        longitud = longitud - 1    #quiero que se modifique dentro del while
        
    return False

print(perteneceBis([9,8,7,6], 9))


#EJERCICIO 2
#devuelve true si y solo si e divide a algun elemento de s
def divide_a_todos(s:list[int], e:int)-> bool:
    
    for elemento in s:
        if elemento % e != 0:
            return False
        
    if len(s) == 0:
        return False
    
    return True 
        
print(divide_a_todos([2,4,6,8,10], 2))        
        
#EJERCICIO 3
def suma_total(s:list[int])-> int:
    contador = 0
    longitud = len(s)
    suma = 0
    
    while contador < longitud:          #voy a ir aumentando el contador por cada iteración, hasta llegar a la longitud de s y que corte ahí
        suma = suma + s[contador]       #Arranco desde 0, y digo sumame el elemento en posicion s[0], hago lo mismo para el elemento en posicion s[1]... asi sucesivamente
        contador = contador + 1
        
    return suma

print(suma_total([10,20,30]))

#EJERCICIO 3'BIS con un for
def sumas(s:list[int])->int:
    sumat = 0
    for elemento in s:
        sumat = sumat + elemento #CONSULTAR POR QUÉ ESTOY MODIFICANDO UN BLOQUE DENTRO DE LA IDENTACION, ES DECIR LO MODIFIQUE EN UN FOR, Y SE MODIFICO AFUERA
    return sumat    

print(sumas([1,2,3]))

#EJERCICIO 4
def maximo(s:list[int])-> int:
    maxim = s[0]

    for elemento in s:
        if  elemento >= maxim: #Lo que estoy haciendo es; primer elemento es >= que primer elemento? Si!, se fija con el 2do, 2do elemento es >=1? ese res = maxim, luego compara el 3ero con el maxim y se queda con el maxim, y asi sucesivamente      
            maxim = elemento
    return maxim
        
print(maximo([1,2,7,3,4,11]))

#EJERCICIO 4 BIS con un While;
def maxBis(s:list[int])-> int:
    maximo_elemento = s[0]
    longitud = len(s)
    contador = 0
    
    while contador < longitud: #Para que se deje de ejecutar este bloque de codigo cuando el indice supere la cantidad de elementos de la secuencia
        if s[contador] >= maximo_elemento:
            maximo_elemento = s[contador]        
        contador +=1
        
    return maximo_elemento

print(maxBis([1,2,3,9,1,11]))


#EJERCICIO 5;
def minimo(s:list[int])->int:
    minimo = s[0]
    
    for elemento in s:
        if elemento <= minimo:
            minimo = elemento
            
    return minimo

print(minimo([1,2,3,4,1,3]))


#EJERCICIO 6
#ord devuelve true si solo si la secuencia esta ordenada de menor a mayor, por ej: 3,4,5 => true
def ord(s:list[int]) -> bool :

    indice = 1

    #Esto seria como mi caso base, basicamente seria si la secuencia es vacia entonces devuelve true
    if len(s) == 0:
        return True

    #La idea seria que: si elemeneto > que el que le sigue entonces no esta ordenada la list, de menor a mayor, por lo tanto retorna true, pero si nunca cumple la condición booleana del if, entonces devuelve por default true
    for elemento in s:
        if elemento <= s[indice]:
            return False

        indice = indice + 1

        #Basicamente lo que estoy haciendo aca, es fijarme si el indice llego hasta el ultimo elemento de s, entonces devuelvo true
        if (len(s) - 1) == indice:
            return True 

    
print(ord([4,3,1,0]))



#EJERCICIO 7 POS MAXIMO;
def pos_maximo(s:list[int])-> int:
    longitud = len(s)
    indice = 0

    if longitud == 0:
        res = -1

    while longitud > indice:
        pos_max = s[0]

        if s[indice] > pos_max:
            res = indice
            pos_max = s[indice]

        else:
            res = 0
            pos_max = s[0]

        indice = indice + 1


    return res

print(pos_maximo([1,2,7,1,6]))


##ES POR ACA, lo resolvi usando un for i in range(inicio, hasta, ritmo)
def pos_maximoBis(s:list[int])-> int:
    longitud = len(s) 
    elMaximo = s[0]

    if len(s)==0:
        return -1

    for indice in range(0,longitud, 1):
        if s[indice] > elMaximo:
            elMaximo = s[indice]
            res = indice

    return res

print(pos_maximoBis([1,2,7,1,9,9,22]))


#EJERCICIO 8
def pos_minimo(s:list[int])->int:
    longitud = len(s)
    elMinimo= s[0]

    if longitud==0:
        return -1 

    for indice in range(0, longitud, 1):
        if s[indice] < elMinimo:
            elMinimo = s[indice]
            res = indice

    return res

print(pos_minimo([1,2,3,0,0]))



#EJERCICIO 9;
def long_mayor_a_siete(palabras:list[str]) -> bool: #Recordar que en python las variables en la signatura van en minuscula, y en haskell van en mayus
    
    #Esto seria como un caso base
    if len(palabras) == 0:
        return False
    
    for palabra in palabras:
        res = False #arranca por default como false, y si hay una palabra que tiene longitud mayor a 7, entonces cambiamos a true
        if len(palabra) > 7:
            res = True
            break #lo que hacemos es cortar el bucle cuando encontro algo que satisface el condicional dentro del bucle
            
    return res
        
print(long_mayor_a_siete(["termo", "l", "tener", "pato", " lagartija"])) #DEVERIA DEVOLVER true, xq len(lagartija) > 7


#EJERCICIO 10;
def es_palindroma(palabra: str ) -> bool: 
    if len(palabra) <= 1: #dado que las palabras vacias y con un solo caracter son palindromas
        return True

    index_UltimoCaracter = (len (palabra) - 1) 

    res = True     
    for caracter in palabra:
        if caracter != palabra[index_UltimoCaracter]:
            res = False
        
        index_UltimoCaracter = index_UltimoCaracter - 1
        #el for arranca iterando desde la primer posición, y el index arranca desde la ultima posicion, hasta que el for termine de recorrer la palabra completa    
    return res

print(es_palindroma("amas"))


#EJERCICIO 11; (obj, devolver true si hay 3 elementos consecutivos que son iguales, por eje: [1,2,3,3,3,8] ó [1,7,7,7,1])
def iguales_consecutivos(s:list[int]) -> bool:
    if len(s) < 3: #por ejemplo [7,2] o [7] o [] devuelva false directamente
        return False    
    
    longitud = (len(s) - 2) #para que no se salga de rango, ya que i+2=k, y si llego hasta k seria out of range
    res = False
    for indice in range(0, longitud, 1): 
        if s[indice] == s[indice + 1] == s[indice + 2]:
            res = True            
    return res

print(iguales_consecutivos([5,7,3,1,1,1,4]))

#EJERCICIO 12; (Obj, devolver true si la palabra tiene almenos 3 vocales distintas)



def vocales_distinas(s:str)->bool:
    res = False
    vocales_de_la_palabra = []
    vocales = "aeiou"
    
    if len(s) < 3:
        return False
        
    for caracter in s:
        if pertenece_a(caracter, vocales):
            vocales_de_la_palabra = vocales_de_la_palabra + [caracter] #voy metiendo solo vocales en una lista vacia 
         
    if (len(vocales_de_la_palabra) < 6) and (vocales_3_distintas(vocales_de_la_palabra)):
        res = True
        
    return res
            
#función Aux:            
def pertenece_a(x:str, palabra: str)-> bool:
    res = False
    for i in palabra:
        if x == i:
            res = True
        
    return res

#funcion aux: Solo recibe vocales, y verifica que haya al menos 3 vocales distintas
def vocales_3_distintas(s:str)->bool:
    longitud = (len(s)-2)
    res = False

    for indice in range(0, longitud, 1):
        if s[indice] != s[indice + 1] != s[indice + 2] and s[indice] != s[indice + 2]:
            res = True 
    return res


print(vocales_distinas("bicicleta"))#funco joyas

#EJERCICIO 13
##AUXILIAR 1; agarra la lista original y me devulve una sub secuencia pero ordenada..y la subseq termina cuando hay un elemento mayor que el siguiente
def subseq_ordenada(s:list[int])-> list[int]:
    longitud = (len(s)-1)
    secuencia = []
#por si recibe una lista vacia    
    if s == []:
        return []
#por si recibe una lista con un solo elemento
    if len(s) == 1:
        secuencia = s

    for indice in range(0, longitud,  1):
        if s[indice] <= s[indice + 1]:
            secuencia = secuencia + [s [indice]]
            if len(secuencia) == longitud:
                secuencia = secuencia + [s[indice + 1]]
        else:
            return secuencia + [s[indice]] #ultimo elemento de la secuencia ordenada 
           
    return secuencia
#print(subseq_ordenada([1,2,2,34,5,6,7,8]))


#AUXILIAR 2; RECIBE MUCHAS SECUENCIAS ORDENADAS, LAS QUE SEAN, Y ME DEVUELVE LA TOTALIDAD MENOS LA PRIMER SECUENCIA ORDENADA
def siguiente_secuencia(s:list[int])->list[int]:
    resto = []
    longitud = len(s) - 1
    for i in range(0, longitud, 1):
        if s[i] > s[i+1]:#cuando se me desordena la lista, es decir estoy buscando el elemento que rompe la secuencia
            desde = i+1
            for index in range(desde, len(s), 1):
                resto = resto + [s[index]]        
            return resto
    return [] #si nunca entro al primer if, es decir si la lista esta ordenada, entonces devuelvo vacio, porque existe solo una lista.
#print(siguiente_secuencia([1,2,3,4]))

##PRINCIPAL
def secuencia_ordenada_mas_larga(s:list[int])-> list[int]:
    secuencia_actual = subseq_ordenada(s)
    restos = siguiente_secuencia(s)
    secuencia_sig = (subseq_ordenada(restos)) #2da secuencia

    while restos != []:
        if len(secuencia_actual) < len(secuencia_sig):
            secuencia_actual = secuencia_sig

        restos = siguiente_secuencia(restos)
        if restos !=[]:
            secuencia_sig = subseq_ordenada(restos)
        
    return secuencia_actual

print(secuencia_ordenada_mas_larga([1,2,3,4,1,2,3,1,2,3,4,5,6,7,7]))
###mamita querida
###
###
###
###

#EJERCICIO 14
def cantidad_digitos_impares(s:list[int])-> int:
    total_impares_en_lista = 0

    for numero in s:
        total_impares_en_lista = total_impares_en_lista + digitos_impares_por_numero(numero)
    
    return total_impares_en_lista

#AUXILIAR QUE RECIBE UN NUMERO, Y LISTA SUS DIGITOS EN UNA LISTA
def melicrack(x:int)-> list[int]:
    digitos_del_numero_en_lista = []
    while x > 0:    
        digitos_del_numero_en_lista = digitos_del_numero_en_lista + [x % 10]
        x = (x // 10)

    return digitos_del_numero_en_lista

#AUXILIAR; recibe un numero y me duelve la cantidad de digitos impares que tiene, por ej; "123" = 2(porque el 1 y el 3 son digitos impares) 
def digitos_impares_por_numero(x:int)-> int:
    cantidad = 0
    digitos_del_numero = melicrack(x)
    
    for digito in digitos_del_numero:
        if digito % 2 != 0:
            cantidad += 1

    return cantidad


#print(cantidad_digitos_impares([57, 2383, 812, 246]))   #deberia devolver 5

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
    res = []
    for indice in range(0,len(s)):
        if indice % 2 == 0:
            res += [0] 
        else: 
            res += [s[indice]]
    return res


#mi_lista2 = [1,2,3,4,5,6]
#print(cero_en_posicion_pares_2(mi_lista2))#PAKSA


#print(cero_en_posicion_pares_1([2]))