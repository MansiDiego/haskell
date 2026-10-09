import unittest

from copiar_en_main import secuencia_ordenada_mas_larga, cantidad_digitos_impares

class test_secuencias(unittest.TestCase):
    def test_secuencia_1(self):
        resultado_esperado: list[int] = [1,2,3,4,5]
        resultado_obtenido: list[int] = secuencia_ordenada_mas_larga([1,2,3,4,5,1,2,3])
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_secuencia_vacia(self):
        resultado_esperado: list[int] = []
        resultado_obtenido: list[int] = secuencia_ordenada_mas_larga([])
        self.assertEqual(resultado_obtenido, resultado_esperado)

class test_digitos(unittest.TestCase):
    def test_digitos(self):
        resultado_esperado: int = 5
        resultado_obtenido: int = cantidad_digitos_impares([57, 2383, 812, 246])
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_sin_digitos_impares(self):
        resultado_esperado : int = 0
        resultado_obtenido : int = cantidad_digitos_impares([])
        self.assertEqual(resultado_esperado, resultado_obtenido)


if __name__ == '__main__':
    unittest.main(verbosity = 2)#indica que tanto se mostrara por panatalla, verbosity 2 es lo mas detallado posible, ya que te muetra el nombre de la funcion mas el resultado del test