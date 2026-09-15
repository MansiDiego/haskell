factorial :: Integer -> Integer
factorial n | n == 0 = 0
            | n == 1 = 1
            | otherwise = n * factorial (n - 1)
 
fibonacci :: Integer -> Integer 
fibonacci n | n == 0 = 0
            | n == 1 = 1
            | n == 2 = 1
            | n == 3 = 2
            | otherwise = fibonacci (n - 1) + fibonacci (n - 2) 


{-EJERCICIO 4-}
sumaImpares :: Integer -> Integer 
sumaImpares n | n == 1 = 1
              | otherwise = esImpar (n) + sumaImpares ( n - 1 )

esImpar :: Integer -> Integer 
esImpar n = (2 * n) - 1



{-EJERCICIO 5-}
medioFact :: Integer -> Integer 
medioFact n | n == 0 = 1
            | n == 1 = 1
            | otherwise = n * medioFact (n - 2)


{-EJERCICIO 6-}
todosDigitosIguales :: Integer -> Bool 
todosDigitosIguales n | n < 10    = True
                      | mod n 10 /= mod (div n 10) 10 = False 
                      | otherwise = todosDigitosIguales (div n 10)

--No era tan dificil, just do it--


{-EJERCICIO 7-}
iesimoDigito :: Integer -> Integer -> Integer 
iesimoDigito n i | n < 10                = n
                 | longitud n == i       = mod n 10
                 | otherwise             = iesimoDigito (div n 10) i


{--cantidadDigitos :: Integer -> Integer -> Bool 
cantidadDigitos n i | i == longitud (n) = True
                    | otherwise         = False 
--}

longitud :: Integer -> Integer 
longitud n | n < 10 = 1
           | otherwise = 1 + longitud (div n 10)


{-EJERCICIO 8-}
sumaDigitos :: Integer -> Integer
sumaDigitos n | n < 10 = n
              | otherwise = mod n 10 + sumaDigitos (div n 10)

{--
Ejercicio 9. Especificar e implementar una funci´on esCapicua :: Integer ->Bool que dado n ∈ N≥0 determina si n es
un n´umero capic´ua.
--}

esCapicua :: Integer -> Bool
esCapicua n | n < 10                       = True
            | compararExtremos n  == False = False
            | otherwise                    = esCapicua (eliminaExtremos n)

compararExtremos :: Integer -> Bool
compararExtremos  n | n < 10                                          = True
                    | mod n 10 == div n (10 ^ ((longitud (n)) - 1))   = True
                    | otherwise                                       = False

eliminaExtremos :: Integer -> Integer
eliminaExtremos n | n < 10    = div n 10
                  | otherwise = div (mod n (10 ^ (longitud (n) - 1))) 10


{-EJERCICIO 10-}
--a
fun1 :: Integer -> Integer
fun1 n | n == 0    = 1
       | otherwise = 2 ^ n + fun1 (n - 1)


--b 
fun2 :: (Integer, Float) -> Float 
fun2 (n , q) | n == 0    = 1
             | otherwise = q ^ n + (fun2 (n - 1, q))


--c
fun3 :: (Integer, Float) -> Float 
fun3 (n , q) | n == 0    = 1
             | n == 1    = q^1 + q^2 
             | otherwise = suma (2 * n , q)


suma :: (Integer, Float) -> Float 
suma (i, q) | i == 0 = 1
            | i == 1 = q
            | otherwise = q ^ i + suma (i - 1 , q)

--d

fun4 :: (Integer, Float) -> Float 
fun4 (n , q) | n == 0    = 1
             | otherwise = suma2 (2 * n, n, q)

suma2 :: (Integer , Integer, Float) -> Float
suma2 (i, n, q) | i < n     = 0
                | otherwise = q ^ i + suma2 (i - 1, n , q)


{-Ejercicio 11-}
eAprox :: Integer -> Float 
eAprox n | n == 0 = 1
         | otherwise = 1 / (fact n) + eAprox (n - 1)

fact :: Integer -> Float 
fact n | n == 0 = 1
       | n == 1 = 1 
       | otherwise = fromIntegral  n * fact ( n - 1 )


{--EJERCICIO 12--}
suc :: Integer -> Float
suc n | n == 1    = 2
      | otherwise = 2 + 1 / suc (n - 1)

raizDe2Aprox :: Integer -> Float
raizDe2Aprox n | n == 1    = 1
               | otherwise = ((suc n) - 1)


{-EJERCICIO 13--}
sumatoriaBase :: Integer -> Integer -> Integer 
sumatoriaBase n m | m == 1           = div (n * (n + 1)) 2 --APLIQUE GAUSS 
                  | n == 1           = m
                  | otherwise        = sumatoriaExponente n m + sumatoriaBase (n - 1) m


sumatoriaExponente :: Integer ->  Integer -> Integer
sumatoriaExponente i j | j == 1    = i
                       | otherwise = i ^ j + sumatoriaExponente i (j - 1)


{--EJERCICIO 14--}
sumaPotencias :: Integer -> Integer -> Integer -> Integer 
sumaPotencias q n m | n == 1    = auxSobreB q n m 
                    | otherwise = auxSobreB q n m + sumaPotencias q (n - 1) m


auxSobreB :: Integer -> Integer -> Integer -> Integer 
auxSobreB q a b | b == 1    = q ^ (a + 1)
                | otherwise = q ^ (a + b) + auxSobreB q a (b - 1)


{--EJERCICIO 15--}
sumaRacionales :: Integer  -> Integer -> Float
sumaRacionales n m | n == 1    = auxSobreDenominador 1 m
                   | otherwise = auxSobreDenominador n m + sumaRacionales (n - 1) m

auxSobreDenominador :: Integer -> Integer -> Float 
auxSobreDenominador n d | d == 1    = fromIntegral n 
                        | otherwise = fromIntegral n / fromIntegral d + auxSobreDenominador n (d - 1)


{--EJERCICIO 16--}
menorDivisor :: Integer -> Integer
menorDivisor n | n == 1    = n
               | otherwise = menorDivisorDesde n 2

menorDivisorDesde :: Integer -> Integer -> Integer 
menorDivisorDesde n i | mod n i == 0 = i
                      | otherwise    = menorDivisorDesde n (i + 1)


--B--
esPrimo :: Integer -> Bool 
esPrimo n | n == 1    = False
          | n == 2    = True
          | (menorDivisorDesde n 2) == n = True
          | otherwise                    = False


--C--
sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos a b | a == 1 || b == 1              = True 
                | menorDivisorDesde' a b 2 == 0 = False
                | otherwise                     = True


menorDivisorDesde' :: Integer -> Integer -> Integer -> Integer 
menorDivisorDesde' a b i | mod a i == 0 && mod b i == 0 = 0
                         | i >= a && i >= b             = 1
                         | otherwise = menorDivisorDesde' a b (i + 1)


--D--
{--nEsimoPrimo :: Integer -> Integer 
nEsimoPrimo i | i == 1                            = 2
              | primoPosición i > primoAnterior i = i
              | otherwise                         = nEsimoPrimo (i + 1)

--ESTA AUXILIAR BUSCA EL PRIMO MAS CERCANO MAYOR QUE EL INDICE, SI PASO 2 DEVUELVE 2, LO CUAL ES PARCIALMENTE INCORRECTO, PERO LO ARREGLAMOS EN LA PRINCIPAL
primoPosición :: Integer -> Integer
primoPosición i | esPrimo i = i
                | otherwise = primoPosición (i + 1) 

primoAnterior :: Integer -> Integer
primoAnterior i | i == 1    = 2
                | otherwise = primoAnterior (i - 1) 
--}
-----
-----
--REHACER EJERCICIO "16 D"
-----
----
{-
contadorDePrimos :: Integer -> Integer 
contadorDePrimos i | i == 1    = 1
                   | otherwise = 1 + esPrimo i

nEsimoPrimo :: Integer -> Integer
nEsimoPrimo n = buscarPrimo n 2 0

buscarPrimo :: Integer -> Integer -> Integer -> Integer
buscarPrimo n candidato cantidad
    | esPrimo candidato && cantidad + 1 == n = candidato
    | esPrimo candidato                      = buscarPrimo n (candidato + 1) (cantidad + 1)
    | otherwise                              = buscarPrimo n (candidato + 1) cantidad
--}

{-EJERCICIO 17-}
esFibonacci :: Integer -> Bool
esFibonacci n | n == 0    = True
              | n == 1    = True
              | otherwise = auxPrincipal 1 n

auxPrincipal :: Integer -> Integer -> Bool
auxPrincipal i n | fibonacci i == n = True      
                 | fibonacci i > n  = False
                 | otherwise        = auxPrincipal (i + 1) n

{-EJERCICIO 18-}
--Implementar la funcion mayor digito par, talque recibe un n, y me devuelve el digito para mas grande de ese "n".


ultimoDigitoPar :: Integer -> Integer  
ultimoDigitoPar n | mod (mod n 10) 2 == 0 = (mod n 10)
                  | otherwise             = -1


elmayor :: Integer -> Integer -> Integer 
elmayor x y | x >= y    = x
            | otherwise = y


mayorDigitoPar :: Integer -> Integer 
mayorDigitoPar n | n < 10    = ultimoDigitoPar n
                 | otherwise = elmayor  (ultimoDigitoPar n) (mayorDigitoPar (div n 10)) 