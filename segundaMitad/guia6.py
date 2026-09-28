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

def alguno_es_0 (numero1: int, numero2:int) -> bool:
    res = numero1 == 0 or numero2 == 0
    return res

print(alguno_es_0(3, 2))


#EJERCICIO 3.2

def ambos_son_0(numero1: int, numero2:int) -> bool:
    res = (numero1 == 0) and (numero2 == 0)
    return res

print(ambos_son_0(0,0))


#EJERCICIO 3.3

def es_nombre_largo (nombre: str) -> bool:
    res = (3 <= len(nombre)) and (len(nombre) <= 8)
    return res

print(es_nombre_largo("mateo"))


#EJERCICIO 3.4
#un año es bisiesto si es multiplo de 400, o bien es multiplo de 4 pero no de 100, si es multiplo de 400 => año=400 x k => año/400=k, con k E a Z, entonces año /400 tiene resto 0
def es_bisiesto(año: int) -> bool:
    res = (año % 400 == 0) or ((año % 4 == 0) and ( año % 100 !=0))
    return res

print(es_bisiesto(200))


#EJERCICIO 4; composicion de funcione usando min y max
#3 kg por cada centímetro hasta 3 metros
#2 kg por cada centímetro arriba de los 3 metros  


def peso_pino(altura: int)-> int:
    res = convierte_altura_a_peso(altura)
    return res


def es_peso_util(pesoDelPino: int)->bool:
    res = 400 < pesoDelPino and  pesoDelPino < 1000           
    return res


def sirve_pino (alturaDelPino: int) -> bool:
    res = es_peso_util(peso_pino(alturaDelPino))
    return res

#auxiliar, recibe una altura y la convierte en peso "kg", independientemente si el arbol mide mas o menos de 3 metros:
def convierte_altura_a_peso(alturas: int ) -> int:
    parteInferior = min (alturas*3, 900) #como maximo me da el 900, es decir si altura es 250cm (2,5m) 250*3<900 entonces me da el resultado
    parteSuperior = 2 * (alturas - 300)
    total         = parteInferior + max(0, parteSuperior) #la funcion max, la usamos porque si el pino mide menos de 300 centimetros, entonces cuando hagamos altura-300 me queda negativo
    return total


def sirvepinobis (altura: int) -> bool:
    res = (altura > 134) and (altura < 350)
    return res

print(sirvepinobis(300))
print(sirve_pino(100))


#EJERCICIO 5
def doble_si_es_par(numero:int)-> int:
    if numero % 2 == 0:
        res= numero * 2
    else:
        res = numero
    return res          

print(doble_si_es_par(8))

#EJERCICIO 5.2
#version 1 con if-then-else
def devolver_valor_si_es_par_si_no_el_que_sigue(numero:int) -> int:
    if numero % 2 == 0:
        res = numero
    else:
        res = numero + 1
    return res
        
#version 2 con dos if
def devolver_mismo_valor_si_es_par_sino_el_siguiete (numero : int) -> int:
    if numero % 2 == 0:
        res = numero
    if numero % 2 !=0 :
        res = numero + 1
    return res
    
print(devolver_valor_si_es_par_si_no_el_que_sigue(2))
print(devolver_mismo_valor_si_es_par_sino_el_siguiete(3))

#5.3
#version 1 doble if [prioriza si es divisible por 9, devuelve num * 3]
def doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero:int) -> int:
    if numero % 3 == 0:
        res = numero * 2
    if numero % 9 == 0:
        res = numero * 3
    else:
        res = numero
    return res

#version 2, usado if then else, pero con doble identación "prioriza si es divisible por 3, devuelve num * 2"
def doble_o_triple(numero: int) -> int:
    if numero % 3 == 0:
        if numero % 9 == 0:
            res = numero * 2 
        else:
            res = numero * 3
    else:
        res = numero
    return res

#version 3 usando operadores logicos
def dobleTrple (numero: int) -> int:
    if numero % 9 != 0 and numero % 3 == 0: 
        res = numero * 2
    if numero % 9 == 0 and numero % 3 == 0:
            res = numero * 3
    else:
        res = numero
    return res

print(doble_si_es_multiplo3_el_triple_si_es_multiplo9(18))
print(doble_o_triple(18))
print(dobleTrple(18))

#5.4
def lindo_nombre(nombre: str)->None:
    if len(nombre)>=5 :
        res = "Tu nombre tiene muchas letras"
    else:
        res = "Tu nombre tiene menos de 5 caracteres"
    return res

print(lindo_nombre("mate"))

#5.5
def elrango(numero: int) -> None:
    if numero < 5:
        res = "menor a 5"
    if numero >= 10 and numero <= 20:
        res = "entre 10 y 20"
    if numero > 20:
        res= "mayor a 20"
    return res

print(elrango(4))


#5.6
def jubilado_o_chambeador(edad: int, sexo:str)-> None:
    if sexo == "M":
        if edad < 18:
            res = "toca ir de vacaciones"
        if edad > 65:
            res = "toca ir de vacaciones"
        else:
            res = "toca trabajar"
    if sexo == "F":
        if edad < 18:
            res = "toca ir de vacaciones"
        if edad > 60:
            res = "toca ir de vacaciones"
        else:
            res = "toca trabajar"
    return res

print(jubilado_o_chambeador(61,"F"))

#EJERCICIO 6
#IMPRIMIR REPETICIONES USANDO CONDICIONAL WHILE

numero = 1
while numero <= 10:
    print(numero)
    numero = numero + 1

def repeticiones()->None:
    n = 1
    while n < 11 :
        res = print(n)
        n = n + 1
    return res

repeticiones() #La funcion solo imprime numeros del 1 al 10 por pantalla, hay que llamar a la funcion para que se ejecute

#6.2
def numeros_pares () ->None:
    n = 2
    while n <= 40:
        res = print(n)
        n = n + 2   
    return res

numeros_pares()

#6.3
def eco() -> None:
    palabra = "eco"
    contador = 1
    while contador <= 10:
        res = print(palabra)
        contador = contador + 1
    return res

eco()


#6.4
def despegue(n: int)-> None:
    while n >= 1:
        res = print(n)
        n = n - 1
    print ("despegue")
    return res  
    
despegue(7)

#6.5
def tiempo(partida:int, llegada:int)-> None:
    año = partida - 1 
    while año >= llegada:
        res = print("viajo un año al pasado, estamos en el año " + str(año))
        año = año - 1
    return res

tiempo(200, 198)

#otra forma de encarar el mismo ejercicio sin hacer renombre de tipos, y resolverlo interpolando variables
def tiempobis(partida:int, llegada:int)-> None:
    año = partida - 1 
    text = "viajo un año al pasado, estamos en el año "
    while año >= llegada:
        res = print(f"{text} {año}")
        año = año - 1
    return res

tiempo(200, 198)
        



#6.4
def monitoreo(partida:int, llegada:int)-> None:
    año = (partida - 20)
    while año >= llegada:
        res = print("viajo 20 años al pasado, estamos en el año " + str(año))
        año = (año - 20)
    print("Aristoteles")
    return res

monitoreo(500, 384)
        
        
#7.1 BUCLE FOR, ARRANCA DESDE I(QUE SERIA 1) Y LLEGA HASTA EL SEGUNDO ARGUMENTO(QUE NO LO INCLUYE), Y SU RITMO ES DE 1 EN 1
for i in range (1, 11, 1):
    print(i)

#7.2
#SERIA for "indice" in range (inicio, final, paso)
for i in range (10, 42, 2):
    print(i)
    
#7.3
for i in range (1, 11, 1):
    print("eco")
    
#7.4
def cohete(n:int) ->None:    
    for n in range (n, 0, -1):
        print(n)
    print("despegue")
    
cohete(5)

#7.5
def monitoreoBis(partida:int, llegada:int) -> None:
    fin = (llegada - 1)
    txt = "Usted viajo un año al pasado, ahora esta en el año "
    i = partida - 1
    for i in range (i, fin, -1):
        print(f"{txt} {i}")
        
monitoreoBis(200, 198)
#NOTA: si queremos llegar hasta un valor dado, lo mas conveniente es o sumarle 1 o restarle uno(dependiendo el caso), dado que el for i in range no toca el limite es decir es invervalo abierto


#7.6

def aristoteles(salida: int) -> None:
    i = (salida - 20)
    txt = "usted viajo 20 años al pasado, ahora esta en el año "
    for i in range(i , 384, -20):
        print(f"{txt} {i}")
    print("aristoteles")
    
aristoteles(500)

#9.1 cual es el resultado de evaluar 3 veces seguidas ro1
g: int = 0

def ro(x: int) -> int:
    global g
    g = g + 1
    return x + g

print(ro(1))#primera evaluacion: me queda g = vale 1 y x vale 1
print(ro(1))#segunda evaluacion: me queda g = vale 2 y x vale 1
print(ro(1))#tercera evaluacion: me queda g = vale 3 y x vale 1
#NOTA: el valor se esta modificando porque el pasaje es por referencia, y no por copia(valor), es decir le estamos pasando el nombre("g") de la posicion en memoria

def rt(x: int, g: int) -> int:
    g = g + 1
    return x + g

print(rt(1, 0))
print(rt(1, 0))
print(rt(1, 0))
#NOTA:en este caso el pasaje es por copia, y no por referencia, por ende no estamos modificando el valor en memoria

