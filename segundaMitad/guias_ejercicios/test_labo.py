import unittest
import random
from queue import LifoQueue as Pila #importa lifoqueue y le asigna el alias pila
from queue import Queue #del modulo queue asignamos la cola como "Queue"


from labo import es_multiplo_de, doble_si_es_par, farenheit_a_celsius, suma_total_biss, pertenece_version_1, pertenece_version_2, pertenece_version_3

class test_multiplo(unittest.TestCase):
    def test_es_multiplo(self):
        resultado_obtenido = es_multiplo_de(4, 2)
        resultado_esperado = True
        self.assertEqual(resultado_esperado, resultado_obtenido)

class test_doble(unittest.TestCase):
    def test_doble_si_cumple(self):
        resultado_obtenido:int = doble_si_es_par(2)
        resultado_esperado:int = 4
        self.assertEqual(resultado_esperado, resultado_obtenido)

class test_farenheit(unittest.TestCase):
    def test_coinciden_las_magnitudes(self):
        resultado_obtenido = farenheit_a_celsius(100)
        resultado_esperado = 37.7778
        self.assertEqual(resultado_obtenido, resultado_esperado)

#PENDIENTE 2 Y 3
class test_labo(unittest.TestCase):
    def test_suma(self):
        resultado_esperado = 6
        resultado_obtenido = suma_total_biss([1,2,3])
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_suma_de_negativos(self):
            resultado_esperado = 2
            resultado_obtenido = suma_total_biss([1,-2,3])
            self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_suma_lista_vacia(self):
            resultado_esperado = 0
            resultado_obtenido = suma_total_biss([])
            self.assertEqual(resultado_esperado, resultado_obtenido)

class test_pertenece_version_1(unittest.TestCase):
    def pertenece_lista_vacia(self):
          resultado_obtenido = pertenece_version_1([], 3)
          resultado_esperado = False
          self.assertEqual(resultado_obtenido, resultado_esperado)

    def pertenece_true(self):
        resultado_obtenido = pertenece_version_1([1,2,3], 3)
        resultado_esperado = True
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def pertenece_false(self):
        resultado_obtenido = pertenece_version_1([1,2,3], 4)
        resultado_esperado = False
        self.assertEqual(resultado_obtenido, resultado_obtenido)


class test_pertenece_version_2(unittest.TestCase):
    def pertenece_lista_vacia2(self):
          resultado_obtenido = pertenece_version_2([], 3)
          resultado_esperado = False
          self.assertEqual(resultado_obtenido, resultado_esperado)

    def pertenece_true2(self):
        resultado_obtenido = pertenece_version_2([1,2,3], 3)
        resultado_esperado = True
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def pertenece_false2(self):
        resultado_obtenido = pertenece_version_2([1,2,3], 4)
        resultado_esperado = False
        self.assertEqual(resultado_obtenido, resultado_obtenido)


class test_pertenece_version_3(unittest.TestCase):
    def pertenece_lista_vacia3(self):
          resultado_obtenido = pertenece_version_3([], 3)
          resultado_esperado = False
          self.assertEqual(resultado_obtenido, resultado_esperado)

    def pertenece_true3(self):
        resultado_obtenido = pertenece_version_3([1,2,3], 3)
        resultado_esperado = True
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def pertenece_false3(self):
        resultado_obtenido = pertenece_version_3([1,2,3], 4)
        resultado_esperado = False
        self.assertEqual(resultado_obtenido, resultado_obtenido)

#19/10, arranco con casos de test de la p7 ejercicio 6.4


#ejercicio 2.13
def armar_secuencia_bingo():
    res = []
    q = Queue()
    while contador <= 99:
        numeros = random.randint(0, 99)
        res.append(numeros)
        q.put(numeros)
        contador += 1
    return q

def jugar_carton_de_bingo(carton: list[int], bolillero:Queue)->int:
    minimas_jugadas = 0
    validos = 0
    for numeros in bolillero:
        for numeros_del_carton in carton:
            if numeros_del_carton == numeros:
                minimas_jugadas += 1
                validos += 1
                if len(carton) == len(validos):
                    return minimas_jugadas
            else:
                minimas_jugadas += 1
    return minimas_jugadas      

#cargo el bolillero
bolillero_a = Queue()
for i in range(99):
    valor = random.randint
    bolillero_a.put(valor)

#print(jugar_carton_de_bingo())
print(bolillero_a.queue)







if __name__ == '__main__':
    unittest.main(verbosity = 2)