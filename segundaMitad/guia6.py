#Fallar es parte del proceso, don't worry, pero tomemos esta enseñanza para ser mas "serio" y definir con mejor criterio que vale o no la pena.
import math #modulo para las sig. funciones : "qrt, round, floor, ceil, %"


#EJERCICIO 1; Es lo mismo recorrer la matriz de izq a derecha que derecha a izq?
def imprimirHolaMund ():
    res = "HOLA"
    return res
    
print (imprimirHolaMund())

#EJERCICIO 2;
def imprimir_un_verso ():
    res = "todo da vueltas como una gran pelota \ngirosss da media vuelta y fijate que pasa allá fuera" #toma \n como un operador que hace un salto de linea por consola
    return res
    
print (imprimir_un_verso())

#EJERCICIO 3;
#round(numero, ndigits)

#OBESERVACIÓN IMPORTANTE; La signatura en python va en el nombre de la funcion, es decir en la linea donde usamos la funcion "def" dada por el Built in de Python 
def rzde2 () -> float: 
    x = math.sqrt(2)
    res = round(x, 4) #el x hace referencia al primer valor, y el 4 dsp de la coma hace referencia a la cantidad de decimales
    return res

print(rzde2())

# def raizde2(x):
#     x = math.sqrt(x)
#     y = round(x, 4)
#     res = y
#     return res 

# print(raizde2(9))


#EJERCICIO 4
def factorial_de_dos() -> int:
    x = 2
    res = x
    return res

print (factorial_de_dos())


#EJERCICIO 5
def perimetro () -> float :
    x = 2 * math.pi
    return x

print (perimetro())
#nota: el perimetro es la longitud de la circunferencia, en este caso de radio 1, dado que la formula del perimetro es: 2 x pi x r (donde r es el radio)


#EJERCICIO 2
def imprimir_saludo (nombre: str) -> str:
    x = "hola " + nombre + " buenas tardes" #el + concatena los str, los "espacios son un caracter, asi que ser cuidadoso"
    return x

print(imprimir_saludo("mateo"))


#EJERCICIO 2.2
def raiz_cuadrada_de_numero (x:int) -> float:
    x = math.sqrt(x)
    return x
#nota: la signatura de python no tira error, por ejemplo si ponemos que devuelve un int, pero en realidad devuelve un float no nos va a avisar que la signatura esta mal...
print (raiz_cuadrada_de_numero(9))

#EJERCICIO 2.3
def farenheit_a_celcius(temp_far: float) -> float:
    temp_celcius = (((temp_far - 32) * 5)/9)  
    return temp_celcius

print(farenheit_a_celcius (100.0))


#EJERCICIO 2.4
def imprimir_dos_veces_estribillo (estribillo: str)->None:
    res = estribillo * 3
    return res

print(imprimir_dos_veces_estribillo ("maquina de goce, no se cuanto mas, "))


#EJERCICIO 2.5
def es_multiplo_de (n: int, m:int)-> bool:
    res = (n % m) == 0 
    return res

print(es_multiplo_de(4,2)) #esto devuelve true, dado que 4 es multiplo de 2, es decir 2 divide a 4


#EJERCICIO 2.6 
def es_par (numero: int) -> bool :
    res = es_multiplo_de(numero, 2)
    return res

print(es_par(5))


#EJERCICIO 2.7
def  cantidad_de_pizzas(comensales:int, min_cant_de_porciones: int) -> int :
    poricones_totales = comensales * min_cant_de_porciones
    res = math.ceil(poricones_totales/8) 
    return res
#nota: ceil es una funcion aportada por el modulo math, que basicamente lo que hace es redondear para arriba, por ejemplo: 2.3 = 3 ó 1.1=2
print(cantidad_de_pizzas(3, 3))


#EJERCICIO 3