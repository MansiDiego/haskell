{-
#comandos para el interprete:
#ghci(Una Obersevacion importante, para ejecutar el interprete con el comando ghci, hay que estar parado desde la terminal en el directorio en cuestion, es decir en la carpeta que tiene el archivo el cual nosotros queremos ejecutar)
#:r recarga el archivo
#:l carga el archivo al compilador
#:q sale del interprete
-}

doubleMe :: Integer -> Integer
doubleMe x = x + x


-- Ejer 1: F(1)=8, F(4)=131 F(16)=16 DEFINIR

parcialF :: Integer -> Integer
parcialF x | x == 1    = 8
           | x == 4    = 131
           | x == 16   = 16
           | otherwise = 0
--Ejer B

parcialG :: Integer -> Integer
parcialG y | y == 8 = 16
           | y == 16 = 4
           | y == 131 = 1
           | otherwise = 0

--ejercicio C

parcialH :: Integer -> Integer
parcialH x = parcialF(parcialG(x))

parcialK :: Integer -> Integer
parcialK x = parcialG(parcialF(x))



{--Ejercicio 2: Especificar e implentar;--}

{--(A)Absoluto de un numero entero (FACIL DE IMPLEMENTAR PARA LUEGO UTILIZAR)--}
absoluto :: Integer -> Integer
absoluto x | x > 0 = x
           | x < 0 = -x
           | otherwise = 0
--Observación, cuando laburas por terminal con los negativos hay que pasarselos como (-2), ya que sino no entiende que es un -2.


{--(B) Devuelve el valor maximo, entre 2 numeros enteros -}
maximo2' :: Integer -> Integer -> Integer 
maximo2' x y | x >= y = x
             | otherwise = y


{--(C):maximo3, DEVUELVE EL MAXIMO ENTRE TRES NUMEROS ENTEROS--}

maximo3 :: Integer-> Integer -> Integer -> Integer
maximo3 x y z | x >= y && x >= z = x
              | y >= x && y >= z = y
              | z >= y && z >= x = z

maximo2 :: Integer -> Integer -> Integer
maximo2 x y | x >= y = x
            | otherwise = y

--Version 2, modularizando el problema
maximo3' :: Integer-> Integer -> Integer -> Integer
maximo3' x y z = maximo2 (maximo2 x y) z


{--(D):Dados dos numeros racionales decide si alguno de los dos es 0--}
--version 1, con patterm matching
algunoEsCero :: Integer -> Integer -> Bool
algunoEsCero x y = x == 0 || y == 0 

--version 2, con guardas
algunoEsCero' :: Integer -> Integer -> Bool
algunoEsCero' x y | x == 0 || y == 0 = True
                  | otherwise = False


{--(E):Ambos son cero, dados 2 numeros racionales decide si ambos son iguales a 0--}
--version 1, con patterm matching
ambosSonCero :: Integer -> Integer -> Bool
ambosSonCero x y = x == 0 && y == 0 

--version 2, con guardas
ambosSonCero' :: Integer -> Integer -> Bool
ambosSonCero' x y | x == 0 && y == 0 = True
                  | otherwise = False


{--(F):enMismoIntervalo, dados 2 numeros determinar si pertenecen al mismo intervalo--}
enMismoIntervalo :: Integer -> Integer -> Bool
enMismoIntervalo x y | x <= 3  &&  y <= 3                     = True
                     | (x > 3 && x <= 7) && (y > 3 && y <= 7) = True
                     | x > 7 && y > 7                         = True
                     | otherwise                              = False


{-(G):sumaDistintos, dados 3 numeros racionales los suma sin repetir-}
sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z | x /= y && y == z = x + y
                    | y /= z && z == x = y + z
                    | z /= x && x == y = z + x
                    | (sondistintos x y z) == True  = x + y + z
                    | (sondistintos x y z) == False =  x

sondistintos :: Integer -> Integer -> Integer -> Bool
sondistintos x y z | x == y && x == z && y == z = False
                   | otherwise = True


{--(H):esMultiploDe, dados dos numeros naturales, decide si el primero es multiplo del segundo --}
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe x y | mod x y == 0  = True 
                 | otherwise     = False


{--(I):digitoUnidades, dado un numero entero, extrae su dıgito de las unidades.--}
digitoUnidades :: Integer -> Integer 
digitoUnidades x = mod (absoluto x) 10 


{--(J)digitoDecenas: dado un numero entero mayor a 9, extrae su dıgito de las decenas--}
digitoDecenas :: Integer -> Integer 
digitoDecenas x = mod (div (absoluto x) 10) 10



{-EJERCICIO 3-}
estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados x y | x * x + x * y * (valorK x y) == 0 = True
                      | otherwise = False

valorK :: Integer -> Integer -> Integer 
valorK a b = div (-a) b   
{--Lo que hice fue basicamente hallar primero el valor de "K" usando una auxiliar, el valor de K, lo saque porque: a . a + a . b .k = 0 es lo mismo que a . (a + b . k ) = 0 y como por el requiere ni a ni b son 0, entonces esa expresion da 0 si y solo (a + b .k) = 0, por lo tanto k = -a/b.
Luego implemente usando practicamente la expresión de la especificación del ejercicio en cuesiton. Fin--}


{-EJERCICIO 4-}

--A--
productoInterno :: (Float, Float) -> (Float, Float) -> Float 
productoInterno (a , b) (c , d) = (a * c) + (b * d)    
--Producto interno, comunmente llamado producto escalar, dado que la salida es un escalar.

--B--
esParMenor :: (Float, Float) -> (Float, Float) -> (Float, Float)
esParMenor (x1 , y1) (x2, y2) |  x1 < x2 && y1 < y2 = (x1 , y1)
                              |  x1 > x2 && y1 > y2 = (x2 , y2)
                              |  x1 > x2 && y1 < y2 = (x2 , y1)
                              |  x1 < x2 && y1 > y2 = (x1 , y2)

--C--
absolutoT :: (Float, Float) -> (Float, Float)
absolutoT (x, y) | x < 0 && y < 0 = (-x, -y)
                 | x > 0 && y < 0 = ( x, -y)
                 | x < 0 && y > 0 = (-x, y)
                 | otherwise = (x, y)

--Auxiliar para flaots
absolutoT1 :: (Float) ->  Float
absolutoT1 x | x < 0 = -x
             | otherwise = x
--La funcion sqrt calcula la raiz cuadrada del valor que le pasemos por parametro
distancia :: (Float, Float) -> (Float, Float) -> Float
distancia (x1, y1) (x2, y2) =  sqrt((absolutoT1 (x1 - x2)) + (absolutoT1 (y1 - y2)))


{-(D): Sumaterna, dado 3 enteros los suma-}
sumaterna :: (Integer, Integer, Integer) -> Integer 
sumaterna (x, y, z) = (x + y + z)


{-(E): sumarSoloMultiplos-}
sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (x, y, z) d = ((esMultiploDe' x d) + (esMultiploDe' y d) + (esMultiploDe' z d))


esMultiploDe' :: Integer -> Integer -> Integer
esMultiploDe' x y | mod x y == 0 = x
                  | otherwise    = 0


{-(F):posPrimerPar, devuelve la posicion del primer par si es que hay alguno, o sino devuelve 4 si son todos impares-}
posPrimerPar :: (Integer, Integer, Integer )-> Integer
posPrimerPar (x, y, z) | espar x   = 0
                       | espar y   = 1
                       | espar z   = 2
                       | otherwise = 4 

espar :: Integer -> Bool
espar x | mod x 2 == 0 = True
        | otherwise    = False


{-(G):crearPar, debe ser polimorfica, es decir debe poder recibir valores de cualquier tipo-}
crearPar :: t1 -> t2 -> (t1, t2)
crearPar t1 t2 = (t1, t2)


{-(H):invertir, Invierte los elementos del par pasado como parametro-}
invertir :: (a, b) -> (b, a)
invertir (a, b) = (b, a) 
--Comentario adicional, en este caso desde la signatura ya se esta laburando al funcion, es decir con la signatura de la funcion ya sirve polimorficamente para cualquier tipo y ademas resuelve la   especificación


{-(I): Reescribir los ejercicios productoInterno, esParMenor y distancia, Usando renombres de tipos: "type Punto2D = (Float, Float)"-}

{-
productoInterno :: (Float, Float) -> (Float, Float) -> Float 
productoInterno (a , b) (c , d) = (a * c) + (b * d)  
-}
type Punto2D = (Float, Float)

productoInterno2 :: Punto2D -> Punto2D -> Float 
productoInterno2 (a , b) (c , d) = (a * c) + (b * d)  



{-esParMenor :: (Float, Float) -> (Float, Float) -> (Float, Float)
esParMenor (x1 , y1) (x2, y2) |  x1 < x2 && y1 < y2 = (x1 , y1)
                              |  x1 > x2 && y1 > y2 = (x2 , y2)
                              |  x1 > x2 && y1 < y2 = (x2 , y1)
                              |  x1 < x2 && y1 > y2 = (x1 , y2)-}

esParMenor2 :: Punto2D -> Punto2D -> Punto2D
esParMenor2 (x1 , y1) (x2, y2) |  x1 < x2 && y1 < y2 = (x1 , y1)
                               |  x1 > x2 && y1 > y2 = (x2 , y2)
                               |  x1 > x2 && y1 < y2 = (x2 , y1)
                               |  x1 < x2 && y1 > y2 = (x1 , y2)



{--distancia :: (Float, Float) -> (Float, Float) -> Float
distancia (x1, y1) (x2, y2) =  sqrt((absolutoT1 (x1 - x2)) + (absolutoT1 (y1 - y2)))--}

distancia2 :: Punto2D -> Punto2D -> Float
distancia2 (x1, y1) (x2, y2) =  sqrt((absolutoT2 (x1 - x2)) + (absolutoT2 (y1 - y2)))

absolutoT2 :: Float ->  Float
absolutoT2 x | x < 0     = -x
             | otherwise =  x


{-(EJERCICIO 5)-}
todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (t0, t1, t2) | (funCion t0 > gunCion t0) && (funCion t1 > gunCion t1) && (funCion t2 > gunCion t2) = True
                          | otherwise = False

                          
funCion :: Integer -> Integer 
funCion n | n <= 7    = n * n 
          | otherwise = (2 * n) - 1 


gunCion :: Integer -> Integer 
gunCion n | mod n 2 == 0 = div n 2
          | otherwise = (3 * n ) + 1                         

{-(EJERCICIO 6: ES BISIESTO)-}
--UN AÑO ES BISIESTO SI ES DIVISIBLE POR 4, O SI ES DIVISIBLE POR 100 ENTONCES TAMBIEN POR 400.
type Anio = Integer 
type EsBisiesto = Bool

bisiesto :: Anio -> EsBisiesto
bisiesto anio | (mod anio 4 /= 0) || (mod anio 100 == 0 && mod anio 400 /= 0) = False
              | otherwise =  True
--OBSERVACION DE LOS RENOMBRES DE TIPOS, SE NOTAN EN MAYUSCULAS CUANDO SE DEFINEN, Y EN LA SIGNATURA, PERO LUEGO COMO VARIABLES SE USAN EN MINUSCULA



{-(EJERCICIO 7, calcula la distancia entre 2 puntos no euclideos)-}
distanciaManhattan ::(Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (x1, y1, z1) (x2, y2, z2) = absolutotupla (x1 - x2) + absolutotupla (y1 - y2) + absolutotupla (z1 - z2)

absolutotupla :: Float -> Float
absolutotupla x | x < 0     = -x
                | otherwise =  x

--(B: REIMPLEMENTAR CON UN RENOMBRE DE TIPOS, PARA LABURAR CON CORDENADAS Y NO CON TERNAS)
type Punto3D = (Float, Float, Float)

distanciaManhattan2 ::Punto3D -> Punto3D -> Float
distanciaManhattan2 (x1, y1, z1) (x2, y2, z2) = absolutotupla (x1 - x2) + absolutotupla (y1 - y2) + absolutotupla (z1 - z2)




{-EJERCICIO 8-}
{-Comparar, labura con 2 parametros... a(entero) y b(entero), y devuelve un entero x... res= 1 si solo si Suma ultimos 2 digitos de a < suma ultimos dos digitos de b
                                                                                        res = -1 si solo si suma ultimos 2 digitos de a > suma ultimos dos digitos de b
                                                                                        res = 0 si solo si suma ultimos 2 digitos de a =  suma ultimos dos digitos de b                
                                                                                        -}
{-PRINCIPAL-}                                                                                        
comparar :: Integer -> Integer -> Integer
comparar a b | sumaUltimosDosdigitos a > sumaUltimosDosdigitos b = -1
             | sumaUltimosDosdigitos a < sumaUltimosDosdigitos b = 1
             | otherwise = 0

{-AUXILIAR-}
sumaUltimosDosdigitos :: Integer -> Integer
sumaUltimosDosdigitos x | x == 0 = 0
                        | x <= 9 = x
                        | otherwise = (ultimoDigito x) + (anteUltimoDigito x) 


{-mod x 10 me devuelve el ultimo digito ó el resto, ya que es lo mismo, de la division entera, por ejemplo mod 123 10 => res = 3-}
{-div x 10 me quita el ultimo digito, por ejemplo div 123 10 => res = 12-}

{-AUXILIARES DE SUMAULTIMOSDIGITOS-}
ultimoDigito :: Integer -> Integer
ultimoDigito x = mod x 10 

anteUltimoDigito :: Integer -> Integer
anteUltimoDigito x = mod (div x 10) 10

{--Haskell es tipo lazy, primero al funcion y luego los argumentos, si es que se necesitan--}

--{EJERCICIO 9}--
--(A)Si n es igual 0 entonces devuelve 1, sino devuelve 0

--(B) Si n es igual a 1 devuelve 15, si n es igual a -1 entonces devuelve -15

--(C) Si N <= 9 devuelve 7, si N >= 3 entonces devuelve 5

--(D) AGARRA 2 FLOATS, LOS SUMA Y CALCULA SU DIVISION

--(E) AGARRA UNA TUPLA, CALCULA LA SUMA DE SUS COMPONENTES, Y LO DIVIDE POR 2

--(F) AGARRA UN FLOAT Y UN ENTERO ME TRUNCA EL FLOAT(LE ELIMINA LOS DECIMALES) Y LO COMPARA CON EL ENTERO, DEVUELVE TRUE O FALSE DEPENDE LO QUE CORRESPONDA.
--FIN PRACTICA 3--