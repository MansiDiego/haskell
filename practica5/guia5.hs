--{EJERCICIO 1}--
--Dada una lista de algun tipo de dato(que no se cual, ni tampoco me importa), devolver un entero que indique la cantidad de elementos que tiene dicha lista
longitud :: [t] -> Integer 
longitud []    = 0
longitud (x:xs) = 1 + longitud xs














































---Problema en cuestion;
{-EJERCICIO 2.5-}
quitar :: (Eq x) => x -> [x] -> [x]
quitar n [] = []
quitar n (x: xs) | n == x = (x:xs)
| otherwise = x : quitar n xs


{--EJERCICIO 3.3--}


maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x : y : xs) | x > y = maximo(x : xs)
| otherwise = maximo (y : xs)



{--EJERCICIO 3.3 CON RECURSION MAS UNA AUXILIAR--}

maximo2 :: [Integer] -> Integer
maximo2 [x] = x
maximo2 (x : xs) = maxi x (maximo2 xs)


maxi :: Integer -> Integer -> Integer
maxi x y | x > y = x
| otherwise = y





{-EJERCICIO 3.9-}
---
ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar (x : xs) = ordenar (quitar (maximo (x : xs)) (x : xs)) ++ [maximo (x : xs)]


{-EJERCICIO 6-}

type Texto = String
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]

--Implementar una funcion que me diga si una persona aparece en mi lista de contactos

enLoscontactos :: Nombre -> ContactosTel -> Bool
enLoscontactos n ( _ : _ ) = False
{--enLoscontactos n (x : xs) | n == Contacto = True
| otherwise = enLoscontactos n (x : xs) --}