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


#EJERCICIO 6;
