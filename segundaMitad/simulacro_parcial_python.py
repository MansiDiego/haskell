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
