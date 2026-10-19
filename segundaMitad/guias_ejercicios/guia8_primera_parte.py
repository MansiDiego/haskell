import random 
from queue import LifoQueue as Pila #importa lifoqueue y le asigna el alias pila
from queue import Queue #del modulo queue asignamos la cola como "Queue"

##Para trabajar con colas y pilas usando el modulo queue, solo podemos utilizar para la materia "put","get","empty" 

#TAD PILA; "LIFO, LAST IN, FIRST OUT"
# p = Pila ()  # crea una pila
# p . put (1)  # apila un 1
# p . get ()   # desapila
# p . empty () # devuelve true si y solo si la pila esta vacia

#TAD COLA;"FIFO, FIRST IN, FIRST OUT"
# q = Queue() # crea una cola
# q.put(1)    # "encola 1"
# q.get()     # "desencola"
# q.empty()   # devuelve true si esta vacia la cola



#EJERCICIOS:
#1:
def generar_numeros_al_azar(cantidad: int, desde:int, hasta:int)-> Pila[int]:
    p = Pila()
    contador = 1

    while contador <= cantidad:
        numero_aleatorio = random.randint(desde, hasta)
        p.put(numero_aleatorio)
        contador += 1
    return p

mi_pila = generar_numeros_al_azar(5, 0, 11)
#print(mi_pila.queue)
#un atajo para espiar que me devolvio la pila, ya que no se puede hacer simplemente print(pila), es hacer print(pila.queue), esto muestra lo que genero la pila






#2:
mi_pila_cargada = Pila()
lista_para_cargar = [1,1,1,2]
#Funcion Auxiliar, no retorna nada, solo me crea una pila
def apilo(lista: list[int]):

    for elemento in lista:
        mi_pila_cargada.put(elemento)

apilo(lista_para_cargar)
#print(mi_pila_cargada.queue)

def cantidad_de_elementos(p: Pila) -> int:
    contador : int = 0
    q = Pila()
    #desapile p, por lo tanto la modifique, que es algo que no quiero hacer, ya que el argumento es tipo "in"    
    while not p.empty():
        cabeza_pila = p.get()
        q.put(cabeza_pila)
        contador += 1   
    #apilo de nuevo p
    while not q.empty():
        base_pila = q.get()
        p.put(base_pila)

    return contador
# print(cantidad_de_elementos(mi_pila_cargada)) #deberia devolverme 4
# print(mi_pila_cargada.queue) #deberia devolverme la pila original



#3
#auxiliar para pasarle una pila
pila_x1 = Pila()
def auxiliar_crea_una_pila(lista: list[int]):
    for elementos in lista:
        pila_x1.put(elementos)
        #no tiene retorno, porque es un procedimiento


def buscar_el_maximo(p:Pila[int]) -> int:
    pila_copia = Pila()
    lista_con_elementos : list[int] = []

    #desapilo y voy comprobando los elementos
    while not p.empty():
        cabeza_pila = p.get()
        lista_con_elementos.append(cabeza_pila)#lo que voy sacando lo meto a una lista para luego recorrerla
        pila_copia.put(cabeza_pila)            #lo que voy sacando lo voy agregnado a una copia, para luego restablecerla

    #apilo lo que desapile
    while not pila_copia.empty():
        base = pila_copia.get()
        p.put(base)

    s = lista_con_elementos 
    el_mayor = s[0]
    for elemento in s:
        if elemento >= el_mayor:        
            el_mayor = elemento

    return el_mayor

#auxiliar_crea_una_pila([1,2,3,4,7,1])#recibe esa lista y ahora lo transformo en una pila
#print(buscar_el_maximo(pila_x1))#deberia devolverme el 7




#4
#funcion principal    
def buscar_nota_maxima(p: Pila[tuple[str, int]]) -> tuple[str, int]:
    lista_para_manipular :list[tuple[str, int]] = []
    q = Pila()

    #apilo todo en q para hacer una copia de p, pero invertida
    while not p.empty():
        elemento = p.get()
        q.put(elemento)
        lista_para_manipular.append(elemento)

    #vuelvo a dejar a p como estaba
    while not q.empty():
        elemento = q.get()
        p.put(elemento)

    resultado = la_mas_alta(lista_para_manipular)
    return resultado

#aux; recibe una lista de tuplas y devuelve al tupla con la nota mas alta:
def la_mas_alta(s:list[tuple[str, int]])-> tuple[str, int]:
    nombre, nota = s[0]
    la_mayor = nota
    
    for nombre, nota in s:
        if nota >= la_mayor:
            la_mayor = nota
            tupla_correcta = nombre, nota

    return tupla_correcta

#auxiliar; a partir de una lista, la transformo en una pila
pila_de_prueba = Pila()
def creo_pila(s:list[tuple[str, int]]):
    for elemento in s:
        pila_de_prueba.put(elemento)
    return pila_de_prueba

#pila_fulana = creo_pila([("Algebra", 4), ("Analisis", 8), ("algoritmos", 10)]) #Acá genere una pila, que cada elemento de la pila es una tupla
#print(buscar_nota_maxima(pila_fulana))#me deberia devolver la tupla con la nota mas alta


#5
def problema_esta_bien_balanceado(s: str)-> bool:
    p = Pila()
    pila_respaldo = Pila()
    primer_elem = Pila()
    #hay 2 formas de que la formula no este bien balanceada, la primera es que arranque con ")" y la segunda es que la cantidad de parentesis de apertura != parentesis de cierre

    #primera forma;

    primer_elem.put(s[0])
    chusmeo_que_es = primer_elem.get()
    if chusmeo_que_es == ")":
        return False 

    #segunda forma;

    #Apilo los elementos
    for caracteres in s:
        p.put(caracteres)

    apertura : int = 0
    cierre : int   = 0

    #desapilo
    while not p.empty():
        elemento = p.get()     
        if elemento == "(":
            apertura += 1
        elif elemento == ")":
            cierre += 1
        pila_respaldo.put(elemento)

    #vuelvo a apilar
    while not pila_respaldo.empty():
        elemento = pila_respaldo.get()
        p.put(elemento)

    #nos fijamos que las cantidades coincidan
    if apertura == cierre:
        res = True
    else:
        res = False
    
    return res

#lista_de_prueba_ejer5 = "((2+2)(3*3))"
#print(problema_esta_bien_balanceado(lista_de_prueba_ejer5))#deberia devolver True

#6: "Calculadora";
def evaluar_expresion(s:str)-> float:
    p = Pila()
    res = []

    #le saco los espacios que me molestan
    for caracter in s:
        if caracter !=" ":
            res.append(caracter)

    #apilar
    for elemento in res:
        if not pertenece_a_operadores(elemento): #si es un numero lo agrego a la pila
            #casteo el elemento a tipo int
            cast_elemento = int(elemento)
            p.put(cast_elemento)
        
        else:   #sino saco los 2 elementos superiores de la pila y le aplico el operador
            if elemento == "+":
                superior = p.get()
                inferior = p.get()
                expresion = superior + inferior
                p.put(expresion)

            elif elemento == "-":
                superior = p.get()
                inferior = p.get()
                expresion = inferior - superior
                p.put(expresion)

            elif elemento == "*":
                superior = p.get()
                inferior = p.get()
                expresion = superior * inferior
                p.put(expresion)

            elif elemento == "/":            
                superior = p.get()
                inferior = p.get()
                expresion = superior / inferior
                p.put(expresion)

    return expresion


def pertenece_a_operadores(s:str)-> bool:
    valores = "+-*/"
    for elementos in valores:
        if s == elementos:
            return True
        
    return False 
# print(pertenece_a_int("o")) 
#print(evaluar_expresion("3 4 + 5 * 2 -"))#deberia devolverme 33


#7
def intercalar(p1: Pila, p2:Pila)-> Pila:
    #p1 y p2 son tipo in
    #req; p1 y p2 tienen la misma cantidad de lementos
    #as; res solo contiene los elementos de p1 y p2 
    #as; res contiene los elementos de p1 y p2 intercalados, respetando el orden orignal
    #as; la cabeza/tope de res es la cabeza/tope de p2
    #as; el tamaño de res = el doble tamaño de p1
    res : Pila = Pila() 
    q1  : Pila = Pila()
    q2  : Pila = Pila()

    while not p1.empty():
        elemento = p1.get()    
        q1.put(elemento)

    while not p2.empty():
        elemento = p2.get()
        q2.put(elemento)

    while not q1.empty() and not q2.empty(): #quiero vaciar las dos
        plato_q1 = q1.get()
        plato_q2 = q2.get()
        res.put(plato_q1)
        res.put(plato_q2)
        #ademas voy restableciendo las pilas originales, al mismo tiempo
        p1.put(plato_q1)
        p2.put(plato_q2)    
    
    return res

def aplilar(s:list[int])->Pila[int]:
    x : Pila = Pila()
    for elementos in s:
        x.put(elementos)
    return x

l1 = [1,2,3]
l2 = [0,0,6]
apilada_l1 = aplilar(l1)
apilada_l2 = aplilar(l2)
intercalada = intercalar(apilada_l1, apilada_l2)
print(intercalada.queue)