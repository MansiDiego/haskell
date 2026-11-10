##1er cuatrimestre 2023##
from queue import Queue as Cola

#problema ind_nesima_aparicion (in s: seq⟨Z⟩, in n: Z, in elem: Z) : Z {
#  requiere: {n>0}
#  asegura: {Si el elemento aparece menos de n veces en la secuencia, res= -1 }
#  asegura: {Si el elemento aparece al menos n veces en la secuencia, s[res] = elem }
#  asegura: {Si el elemento aparece al menos n veces en la secuencia, elem aparece n-1 
#  veces en s entre las posiciones 0 y res-1 }

#Por ejemplo, dadas
#s = [-1, 1, 1, 5, -7, 1, 3]
#n = 2
#elem = 1
#se debería devolver res = 2

def cantidad_de_apariciones(s:list[int], elem: int)-> int:
    total : int = 0
    for elementos in s:
        if elementos == elem:
            total += 1

    return total
# print(cantidad_de_apariciones([1,2,3,2], 2)) 

def ejercicio1(s:list[int], n:int, elem: int)-> int:
    if cantidad_de_apariciones(s, elem) < n:
        return -1
    
    apariciones : int = 0
    enesima : int = 0
    #tengo que devolver la enesima aparicion de elem
    for elementos in s:
        if elementos == elem:
            apariciones += 1
            if apariciones == cantidad_de_apariciones(s, elem) - 1:
                return enesima
        enesima += 1

# res = ejercicio1([1,2,3,3,2,1,2,2], 2, 2)
# print(res)

#1#(2 puntoss)
def cantidad_parejas_que_suman(s:list[int], n:int)-> int:
    if len(s) <=1:
        return 0
    contador : int = 0

    for i in range(0, len(s)-1, 1):
        for j in range(i+1, len(s)):
            if s[i] + s[j] == n: 
                contador += 1

    return contador

print(cantidad_parejas_que_suman([1,3,2,5,4,8], 5))


#2 (2,5 puntos) 
def pasar_por_auto_servicio(clientes:Cola[tuple[str, str, int]])-> str:
    clientes_respaldo : Cola[tuple[str, str, int]] = Cola()
    res_nombres = []
    
    while not clientes.empty():
        nombre, metodo, cantidad = clientes.get()
        clientes_respaldo.put((nombre, metodo, cantidad))

        if metodo != "efectivo" and cantidad <= 15:
            res_nombres.append(nombre)

    res = res_nombres[0] #es el primero que agregue 

    while not clientes_respaldo.empty():
        nombre, metodo, cantidad = clientes_respaldo.get()
        if nombre != res:
            clientes.put((nombre, metodo, cantidad))

    return res

clientes_prueba = Cola()

# clientes_prueba.put(("Ana", "efectivo", 13))
# clientes_prueba.put(("Juan", "qr", 22))
# clientes_prueba.put(("Bruno", "tarjeta", 14))
# clientes_prueba.put(("pepe", "tarjeta", 14))
# res = pasar_por_auto_servicio(clientes_prueba)
# print(res)
# print(clientes_prueba.queue)

##3
def intercambiar_e_invertir_columnas(m: list[list[int]], col1:int, col2:int):
    matriz_copia = [fila.copy() for fila in m]  #Para copiar una Matriz es importante!! Porque si haces matriz_copia = m.copy() haces una copia externa, y las filas apuntan a la misma posicion de memoria, por lo tanto la copia tiene que ser interna tambien
    
    for i in range(0, len(m)):
        matriz_copia[i][col1] = m[len(m) - 1 - i][col2]
        matriz_copia[i][col2] = m[len(m) - 1 - i][col1]

    for i in range(len(matriz_copia)):
        for j in range(len(matriz_copia[i])):
            m[i][j] = matriz_copia[i][j]


mat = [[1,2,3],[40,50,60], [-7,-8,-9]] #debe devolver [[1, -9, -8], [40, 60, 50], [-7, 3, 2]]
res_3 = intercambiar_e_invertir_columnas(mat, 1, 2)
print(mat)


##4##
def mantuvieron_residencia(censo1: dict[str, str], censo2:dict[str, str])-> dict[str, int]:
    res :dict[str, int]= {}
    
    for nombres in censo1.keys():
        if censo1[nombres] == censo2[nombres]:
            if censo1[nombres] not in res.keys():

                res[censo1[nombres]] = 1 #sino es una clave la creo
            else:
                res[censo1[nombres]] += 1 #si ya es una clave entonces le agrego uno mas

    return res

print(mantuvieron_residencia({'Juan': 'Merlo', 'Ana': 'Merlo', 'pedro': 'Merlo'}, {'Juan': 'Castelar', 'Ana': 'Merlo', 'pedro': 'Merlo'}))

#otro parcial, nota 10