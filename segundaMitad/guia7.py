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
