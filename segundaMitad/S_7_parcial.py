from queue import LifoQueue as Pila

##primer cuatrimestre de 2025##
#eje 1:
# problema prefijo_que_mas_suma (in s: seq⟨Z⟩) : Z {
#   requiere: { |s| > 0 }
#   asegura: { res = ∑ ki=0 s[i] para algún k tal que 0 ≤ k < |s| }
#   asegura: { res ≥ ∑ ki=0 s[i] para todos los k tales que 0 ≤ k < |s| }
# }
def prefijo_que_mas_suma(s: list[int])-> int:
    if len(s) == 2:
        return s[0] + s[1]

    suma_max : int = 0
    suma_actual : int = 0

    for i in range(0,len(s)-1, 1):
        suma_actual = s[i] + s[i+1]
        if suma_actual > suma_max:
            suma_max = suma_actual
        
        suma_actual = 0

    return suma_max

lista_prueba_1 = [1,2,3,6,0,1,8]#debe devolver 9
print(prefijo_que_mas_suma(lista_prueba_1))



##ejercicio 2##(2 puntos);
def primera_entrega_en_blanco(examenes: Pila[tuple[str, int]])-> str:
    #la primera componente hace referencia a el nombre del estudiante y la segunda componennte hace referencia a la cantidad de hojas que entrego, debo devolver el primer estudiante que entrego en blanco(0 hojas)

    examenes_respaldo : Pila[tuple[str, int]] = Pila()
    alumnos_en_blanco : list[str] = []
    

    while not examenes.empty():
        nombre, cantidad_hojas = examenes.get()
        examenes_respaldo.put((nombre, cantidad_hojas))

        if cantidad_hojas == 0:
            alumnos_en_blanco.append(nombre)

    while not examenes_respaldo.empty():
        tupla = examenes_respaldo.get()
        examenes.put(tupla) #dejo la pila de examenes tal cual como estaba

    ultima_posicion = len(alumnos_en_blanco)-1
    primer_entraga = alumnos_en_blanco[ultima_posicion]

    return primer_entraga

# pila_examenees = Pila()
# pila_examenees.put(("pepe", 0))
# pila_examenees.put(("fulano", 3))
# pila_examenees.put(("ron", 0))
# pila_examenees.put(("fuliño", 3))
# res_2 = primera_entrega_en_blanco(pila_examenees)
# print(res_2)



##Ejercicio 3## (2 puntos)
def desplazar_columnas_hacia_arriba(m:list[list[int]], col:int):
    ultima_posicion = len(m) - 1
    m[ultima_posicion][col] = m[0][col]

    for i in range(0, len(m)-1, 1): #la ultima fila la modifique primero
        m[i][col] = m[i+1][col] #siguiente fila, en la columna indicada
    
# mat = [[2,2,2],[3,3,3],[7,7,7]]
# res_3 = desplazar_columnas_hacia_arriba(mat, 2)
# print(mat)



##Ejercicio 4##(2,50)
    # Quien sale en primer puesto recibe 3 puntos
    # Quien sale en segundo puesto recibe 2 puntos
    # Quien sale en tercer puesto recibe 1 punto
# problema armar_ranking (in podios: seq⟨Diccionario⟨Z,String⟩⟩): Diccionario⟨String,Z⟩ {
#   requiere: { Cada diccionario de podios tiene como claves los valores 1, 2 y 3 (o algún subconjunto de los mismos) }
#   requiere: { Sea d un diccionario de la secuencia podios, entonces d no contiene valores repetidos }
#   asegura: { nom es clave de res si y sólo si existe un diccionario en podios tal que nom es valor de dicho diccionario }
#   asegura: { Cada clave c de res tiene como valor la sumatoria de los puntos obtenidos por c en cada una de las competencias de podios (suma 3 puntos si salió primero, 2 puntos si salió segundo, 1 punto si salió tercero y 0 puntos si no estuvo en el podio de esa competencia) }
# }

def armar_ranking(podios: list[dict[int, str]])-> dict[str, int]:

    res :dict[str, int] = {}

    for diccionarios in podios:
        for puestos, nom in diccionarios.items():
            if puestos == 1:
                if nom not in res.keys():
                    res[nom] = 3 #creo la clave 
                else:
                    res[nom] += 3

            elif puestos == 2:
                if nom not in res.keys():
                    res[nom] = 2
                else:
                    res[nom] += 2

            elif puestos == 3:
                if nom not in res.keys():
                    res[nom] = 1
                else:
                    res[nom] += 1
            
            else:#no esta en el podio, entonces no suma nada
                if nom not in res.keys():
                    res[nom] = 0
                else:
                    res[nom] += 0

    return res

# primera_competencia = {3: "mateo", 1:"rodri", 2:"santi"}
# segunda_comptencia = {1:"mateo", 2:"rodri", 3:"santi"}
# lista_prueba_4 = [primera_competencia, segunda_comptencia]
# res_4 = armar_ranking(lista_prueba_4)
# print(res_4)


##Choices##
#075x2 = 1,50p
#nota 10 puntos, 1h:20min