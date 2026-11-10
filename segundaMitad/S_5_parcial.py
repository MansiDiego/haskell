#segundo cuatrimestre 2023

#1(2puntos)
def problema_enesima_posicion(s:list[int], n:int, elem:int)-> int:
#  requiere: {n>0}
#  asegura: {Si el elemento aparece menos de n veces en la secuencia, res= -1 }
#  asegura: {Si el elemento aparece al menos n veces en la secuencia, s[res] = elem }
#  asegura: {Si el elemento aparece al menos n veces en la secuencia, elem aparece n-1 
#  veces en s entre las posiciones 0 y res-1 }

    n_veces = cantidad_apariciones(s, elem)
    apariciones = 0

    if n_veces < n:
        return -1

    if n_veces >= n :
        for i in range(len(s)):
            if s[i] == elem:
                apariciones += 1
                
                if n_veces - 1 == apariciones:
                    return i
                

def cantidad_apariciones(s:list[int], e:int)-> int:
    cantidad : int = 0
    
    for elementos in s:
        if elementos == e:
            cantidad +=1

    return cantidad


#Por ejemplo, dadas
s = [-1, 1, 1, 5, -7, 1, 3]
n = 2
elem = 1

print(problema_enesima_posicion(s,n,elem))
#se debería devolver res = 2 pa ksa


##2##(2)puntos
#intercalar elementos de 2 listas, las posiciones pares van los elementos de s1(0,2,4,6), las posiciones impares los elementos de s2(1,3,5,7);
#problema mezclar (in s1: seq⟨Z⟩, in s2: seq⟨Z⟩) : seq⟨Z⟩ {
#  requiere: {|s1| = |s2| }
#  asegura: {|res| = 2 * |s1|}
#  asegura: {res[2*i] = s1[i] y res[2*i+1] = s2[i], para i entre 0 y |s1|-1}
#}
#TIP: realizar la iteración mediante índices y no mediante elementos

def mezclar(s1 : list[int], s2 : list[int])->list[int]:
    res = []

    for i in range(0, len(s1)):

        if i % 2 == 0:
            res.append(s1[i])

        elif i % 2 !=0:
            res.append(s2[i])

    return res

s1_ = [7,7,7,7]
s2_ = [81,81,81,81]
resultado_2 = mezclar(s1_, s2_)
print(resultado_2) #indices = [0,1,2,3,4] por lo tanto res =[3,7,3,7]


##Ejercicio 4###(3 puntos) 
##4## matriz capicua
def matriz_capicua(m: list[list[int]])-> bool:
    for fila in m:
        if fila_capicua(fila):
            pass
        else:
            return False
    return True


def fila_capicua(s:list[int])-> bool:
    for i in range(0, len(s), 1):
        if s[i] == s[len(s) - 1 - i]:
            pass
        else:
            return False
        
    return True

# print(fila_capicua([1,2,2,1]))
# #Por ejemplo, dada la matriz
# m = [[1,2,2,1],[-5,6,6,-5],[0,1,1,0]]
# # #se debería devolver res = true
# resultado_4 = matriz_capicua(m)
# print(resultado_4)


#3 3 puntos; Repasar
def frecuencia_posiciones_por_caballo(caballos: list[str], carreras: dict[str, list[str]]) -> dict[str, list[int]]:
    res = {}

    # Inicializamos el diccionario
    for caballo in caballos:
        res[caballo] = [0] * len(caballos)

    # Recorremos las carreras
    for carrera in carreras:
        posiciones = carreras[carrera] #seria para cada clave, obtengo su valor, que su valor es una lista de posiciones[]

        # Recorremos las posiciones de cada carrera
        for i in range(len(posiciones)):
            caballo = posiciones[i]
            res[caballo][i] += 1 #me voy parando en las claves de cada caballo particular, en su indice correspondiente y agrego el valor

    return res

# #paro

caballos = ["linda", "petisa", "mister", "luck" ]

carreras = {"carrera1":["linda", "petisa", "mister", "luck"],
            "carrera2":["petisa", "mister", "linda", "luck"]}


resultado_1 = frecuencia_posiciones_por_caballo(caballos, carreras)
print(resultado_1)


#nota 7 puntos, observacion, muy quemado para hacerlo bien, pero sale de una