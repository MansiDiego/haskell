#diccionarios y archivos##:

#EJERCICIO 16
#DICCIONARIOS;
def calcular_promedio_por_estudiante(notas: list[tuple[str, int]])-> dict[str, int]:
    promedio_por_estudiante = {}
    lista_promedios = []
    contador = 0
    divisor = 1
    
    for tupla in notas:
        alumno, nota = tupla
        if not alumno in lista_promedios:
            lista_promedios.append(tupla)
        else:
            lista_promedios[contador - 1][2] + nota
            divisor += 1
        
    

    return promedio_por_estudiante

alumnos = [("sole", 9.5),("maxi", 8.0),("sole", 9.0)]
res = calcular_promedio_por_estudiante(alumnos)
print(res)