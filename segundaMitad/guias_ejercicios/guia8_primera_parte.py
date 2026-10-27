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

##
#COLAS
##
#1;
def generar_nros_al_azar(cantidad:int, desde:int, hasta:int)-> Queue:
    q = Queue()
    contador = 0
    while contador < cantidad:
        elemento = random.randint(desde, hasta) 
        contador += 1
        q.put(elemento) #estoy encolando elementos
    return q

colimba = generar_nros_al_azar(5, 0, 21)
print(colimba.queue)


#2;
def cantidad_de_elementos(c:Queue)->int:
    copia = Queue()
    contador :int = 0
    while not c.empty():
        elemento  = c.get()
        copia.put(elemento)
        contador += 1

    while not copia.empty():
        elemento = copia.get()
        c.put(elemento)

    return contador

co = Queue()
for i in range (5):
    co.put(i)

# ver = cantidad_de_elementos(co)
# print(ver)
print(co.queue)



#3
def buscar_el_maximo_colas(c:Queue)->int:
    copia = Queue()
    primero = c.get()
    copia.put(primero) #aca esta la primer persona de la fila
    el_mayor = primero

    while not c.empty():
        clientes = c.get()
        copia.put(clientes)

        if el_mayor <= clientes:
            el_mayor = clientes 

    while not copia.empty():
        cliente = copia.get()
        c.put(cliente)

    return el_mayor

print(buscar_el_maximo_colas(co))
print(co.queue)



#4
def buscar_nota_minima(c:Queue[tuple[str, int]]) -> tuple [str, int]:
    copia = Queue()
    primer_tupla = c.get()
    materia, nota_minima = primer_tupla
    copia.put(primer_tupla)

    #desencolo y voy comparando las notas
    while not c.empty():
       tupla_materia_Y_nota = c.get()
       materia, nota = tupla_materia_Y_nota
       copia.put(tupla_materia_Y_nota)

       if nota <= nota_minima:
            nota_minima = nota
            tupla_correcta = materia, nota

    #la dejo como estaba
    while not copia.empty():
        tupla_materia_y_nota = copia.get()
        c.put(tupla_materia_y_nota)

    return tupla_correcta

cflex = Queue()
cflex.put(("algoritmos", 10))
cflex.put(("algebra", 5))
cflex.put(("termodinamica", 7))
tupla_menor = buscar_nota_minima(cflex)
print(tupla_menor)#devuelve la tupla que tiene la nota minima



#12
#la idea es que si c1= [1,2,3] y c2= [7,5,4] entonces intercalar = [1,7,2,5,3,4]
fila_chango = Queue()
for i in range(1,4,1):
    fila_chango.put(i)
fila_carfour = Queue()
fila_carfour.put(7)
fila_carfour.put(5)
fila_carfour.put(4)


def intercalar(c1:Queue, c2:Queue)-> Queue:
    copia_c1 : Queue = Queue()
    copia_c2 : Queue = Queue()
    intercalada : Queue = Queue()
    
    while not c1.empty() and not c2.empty():
        desencolar_c2 = c2.get()
        desencolar_c1 = c1.get()
        intercalada.put(desencolar_c1)
        intercalada.put(desencolar_c2)
        copia_c2.put(desencolar_c2)
        copia_c1.put(desencolar_c1)

    while not copia_c1.empty() and not copia_c2.empty():
        desencolar_copia_c1 = copia_c1.get()
        desencolar_copia_c2 = copia_c2.get()
        c1.put(desencolar_copia_c1)
        c2.put(desencolar_copia_c2)

    return intercalada

#recordar que la estructura de datos de una cola sigue el patron "fifo" first in, first out
# una_y_una = intercalar(fila_chango, fila_carfour)
# print(una_y_una.queue)
# print(fila_carfour.queue)



#13;


def armar_secuencia_de_bingo()-> Queue:
    contador : int = 0
    c : Queue = Queue()
    carton_testing = []
    while contador <= 99:
        numero_aleatorio = random.randint(0, 99)
        if numero_aleatorio not in carton_testing:
            c.put(numero_aleatorio)
            carton_testing.append(numero_aleatorio)
            contador += 1

    return c


bolillero = armar_secuencia_de_bingo()
# carton = armar_carton_de_bingo()

def carton_bingoo()-> list[int]:
    contador : int = 1
    salida = []
    
    while contador <=12:
        numeros_aleatorios = random.randint(0,99)
        if numeros_aleatorios not in salida:
            salida.append(numeros_aleatorios)
            contador += 1
    return salida



def jugar_carton_de_bingo(carton_bingo: list[int], bolillero_bingo: Queue[int])->int:

    cantidad_minima_de_jugadas :int = 0
    copia_carton : list[int] = []
    
    while len(copia_carton) < 12:
        primero_elemento = bolillero_bingo.get()

        #dado que no tengo elementos repetidos puedo implementarlo de esta manera
        if primero_elemento in carton_bingo: 
            copia_carton.append(primero_elemento)
            
        cantidad_minima_de_jugadas += 1

    return cantidad_minima_de_jugadas

# primer_carton = carton_bingoo()
# primer_bolillero = armar_secuencia_de_bingo()
# cantidad_de_jugadas_minimas_para_la_primer_prueba = jugar_carton_de_bingo(primer_carton, primer_bolillero)
# print(cantidad_de_jugadas_minimas_para_la_primer_prueba)

#EJERCICIO 14:
#la entrada es una cola de tuplas
def pacientes_urgentes(c: Queue[(int, str, str)])-> int:
    cantidad_de_pacientes_urgentes : int = 0
    copia_c = Queue()
    
    while not c.empty():
        paciente = c.get()
        prioridad, nombre, especialidad = paciente #lo tengo que ir renombrando, ya que los diferentes elementos de la cola son distintos pacientes con distintos valores(urgencia,nombres, especialdiad)
        if prioridad <= 4:
            cantidad_de_pacientes_urgentes += 1
        copia_c.put(paciente)

    while not copia_c.empty():
        paciente = copia_c.get()
        c.put(paciente) #para dejar la cola, tal cual como estaba, ya que el arg es de tipo in

    return cantidad_de_pacientes_urgentes

cola_de_pacientes = Queue()
cola_de_pacientes.put((1, "pedro", "cardiologo"))
cola_de_pacientes.put((7, "rodolfo", "clinico"))
cola_de_pacientes.put((4, "pedrito", "gastronterologo"))

# cuantos = pacientes_urgentes(cola_de_pacientes)
# print(cuantos)
# print(cola_de_pacientes.queue)

##--15--##
def entidad(c: Queue)-> Queue[tuple[str, int, bool, bool]]:
    resto = Queue()
    cola_de_banco_por_prioridad = Queue()
    cola_de_banco_por_preferencia = Queue()
    cola_de_banco_ordenada = Queue()

    while not c.empty():
        elemento = c.get()
        nombre, edad, preferencia, prioridad = elemento
        if prioridad:
            cola_de_banco_por_prioridad.put(elemento)
        elif preferencia:
            cola_de_banco_por_preferencia.put(elemento)
        else:
            resto.put(elemento)

    while not cola_de_banco_por_prioridad.empty():
        persona = cola_de_banco_por_prioridad.get()    
        cola_de_banco_ordenada.put(persona)

    while not cola_de_banco_por_preferencia.empty():
        persona = cola_de_banco_por_preferencia.get()
        cola_de_banco_ordenada.put(persona)

    while not resto.empty():
        persona = resto.get()
        cola_de_banco_ordenada.put(persona)

    return cola_de_banco_ordenada

