from queue import Queue as Cola
#ejercicio 1;
#devolver la subsecuencia de mayor longitud, con sus elementos ordenados de forma creciente, si hay 2 o mas de misma longitud => debo devolver la de menor indice(la primera)
def ejercicio1(s: list[int])-> list[int]:
    
    if len(s) == 1:
        return s
    
    secuencia_actual : list[int] = [s[0]]
    mejor_secuencia : list[int] = [s[0]]
    #forma estrictamente creciente 1,3,7,8,1... /= 1,1,3,7,7,8, esta ultima secuencia no es estrictamente creciente, ya que hay elementos que son iguales
    for i in range(1, len(s), 1):
        if s[i] > s[i-1]:
            secuencia_actual.append(s[i])
        else:
            if len(secuencia_actual) > len(mejor_secuencia):
                mejor_secuencia = secuencia_actual.copy()
            secuencia_actual = [s[i]]

    if len(secuencia_actual) > len(mejor_secuencia):
        mejor_secuencia = secuencia_actual.copy()

    return mejor_secuencia


secuencias_pruebas = [1,2,3,4,5,6,7,8,1,2,3,1,2,3,4,5,6,7,8,9]
res_1 = ejercicio1(secuencias_pruebas)
print(res_1)


##Ejercicio 2###
def ejercicio2(pedidos: Cola[tuple[str, int]], stock: int)-> Cola[str]:
 
    pedidos_respaldo : Cola[tuple[str, int]] = Cola()
    res : Cola[str] = Cola()
   

    while not pedidos.empty():
        producto, cantidad = pedidos.get() 
        if cantidad <= stock: #porque se va a despachar, ya que cumplimos con la cantidad que piden
            res.put(producto)
            stock -= cantidad

        else:
            pedidos_respaldo.put((producto, cantidad))

            
    while not pedidos_respaldo.empty():
        tuplas = pedidos_respaldo.get()
        pedidos.put(tuplas)

    return res

# pedidoss = Cola()
# pedidoss.put(("A", 3))
# pedidoss.put(("B", 5))
# pedidoss.put(("C", 2))
# pedidoss.put(("D", 1))
# # print(pedidoss.queue)
# res_2 = ejercicio2(pedidoss, 6)
# print(res_2.queue)



##EJERCICIO 3
#m inout, procedimiento que modifica la matriz
def ejercicio3(m: list[list[int]]):
    
    for i in range(0, len(m), 1):
        minimo_de_fila = minimo(m[i])
        m[i].append(minimo_de_fila) 

#la lista es no vacia
def minimo(s:list[int])-> int:
    minimo = s[0]
    for elemento in s:
        if elemento < minimo:
            minimo = elemento

    return minimo
matriz_prueba = [[0,2,3],[0,7,7],[0,8,7]]
ejercicio3(matriz_prueba)
print(matriz_prueba)
# print(minimo([1,0,3]))

##EJERCICIO 4

def ejercicio4(eleccion1: dict[str, str], eleccion2: dict[str, str])-> dict[str, int]:
    conservaron_su_voto : dict[str, int] = {}

    for persona, voto in eleccion1.items():
        for persona2, voto2 in eleccion2.items():
            if persona == persona2 and voto == voto2:

                if voto not in conservaron_su_voto.keys():
                    conservaron_su_voto[voto] = 1
                else:
                    conservaron_su_voto[voto] += 1

    return conservaron_su_voto

# elec1 = {"ana": "Milei", "beto":"Massa", "norberto":"Massa"}
# elec2 = {"ana": "Massa", "beto":"bulrich", "norberto":"bulrich"}
# res_4 = ejercicio4(elec1, elec2) 
# print(res_4)