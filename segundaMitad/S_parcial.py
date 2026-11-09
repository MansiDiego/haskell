#ejercicio 1:
def ejercicio1 (s: list[int], n:int)-> list[int]:
    subseq :list[int] = []
    longitud = len(s) - 1
    #me saco el caso base de encima, que seria cuando me manden una lista de un solo elemento, o una lista vacia
    if len(s) <= 1:
        return s
    
    for i in range(longitud, 0, -1):
        subseq.append(s[i])
        if sumatoria(subseq) == n:
            return subseq
        
        elif sumatoria(subseq) > n:
            subseq = []
    


def sumatoria(s:list[int])-> int:
    suma_total : int = 0
    for elemento in s:
        suma_total += elemento
    return suma_total

resultado = ejercicio1([1,3,2,5,4,1,8], 5) #debe devolver [4,1]
print(resultado)


##3## Es un procedimiento
def ejercicio3( m:list[list[int]] ):
    
    for filas in m:
        elemento_final = busca_minimo_de_fila(filas)
        filas.append(elemento_final)#observacion, append agrega al final de la lista

def busca_minimo_de_fila(s: list[int])-> int:
    minimo = s[0]
    for elemento in s:
        if elemento < minimo:
            minimo = elemento
    return minimo

matriz_modifica = [[0,2,3], [7,0,8], [93, 0 ,1]]
ejercicio3(matriz_modifica)
print(matriz_modifica)


##Ejercicio 4##
#las claves son ciudadanos
#las claves de eleccion 1 y 2 coinciden
#tenemos que devolver un diccionario que contenga la cantidad de votos que tiene un candidato, pero ese candidato se cuenta si y solo si aparece en ambos diccionarios
def ejercicio4(eleccion1: dict[str, str], eleccion2:dict[str, str])-> dict[str, int]:
    res : dict[str, int] = {} 
    
    for ciudadano1, voto1 in eleccion1.items():
        for ciudadno2, voto2 in eleccion2.items():
            
            if voto1 not in res and (voto1 == voto2) and (ciudadano1 == ciudadno2):  
                res[voto1] = 1

            elif voto1 in res and (voto1 == voto2) and (ciudadano1 == ciudadno2):
                res[voto1] = res[voto1] + 1

    return res


res = ejercicio4({"ana": "X", "beto": "X", "caro":"X"} ,  {"ana": "X", "beto":"Y", "caro":"X"})
print(res)

###Solucion a tener en cuenta:
# for ciudadano, voto1 in eleccion1.items():
#     voto2 = eleccion2[ciudadano]  # Acceso directo al voto de esa misma persona en la segunda elección
    
#     if voto1 == voto2:
#         # Votó al mismo candidato en ambas
#         if voto1 not in res:
#             res[voto1] = 1
#         else:
#             res[voto1] += 1