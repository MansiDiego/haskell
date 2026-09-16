--{EJERCICIO 1}--
--Dada una lista de algun tipo de dato(que no se cual, ni tampoco me importa), devolver un entero que indique la cantidad de elementos que tiene dicha lista
longitud :: [t] -> Integer 
longitud []    = 0
longitud (x:xs) = 1 + longitud xs
--LAS COMILLAS SIMPLES 'char' son para un unico caracter, no es valido pasar 'hola' y las comillas "hola" toman una cadena de char y lo vuelven un solo elemento(por lo tanto si le paso ["h", "o", "l"] labura como las comillas simples y devuelve 3, pero si le paso "hol" devuelve 1, xq toma la cadena como un solo elemento)

--1.B
--Dada una lista de elementos devuelve el ultimo elemento, la especificacion es |s| - 1, que lo que estaria indicando es que es el ultimo elemento, es decir dame el elemento empezando desde el final
ultimo :: [e] -> e
ultimo [e]     = e
ultimo (x : xs) = ultimo xs

--1.C
--Principio labura con una lista de tipo T y devuelve otra lista de tipo T.
principio :: [t] -> [t]
principio [x] = []
principio (x:xs) = x : principio xs


---1.D
--REVERSO, tiene todos los elementos que "S" pero en orden invertido
reverso :: [t] -> [t]
reverso []       = [] --seria mi caso base
reverso (x : xs) = reverso xs ++ [x] 
-- ++ Concatena 2 listas, y [x] es la lista unitaria



{-EJERCICIO 2.1-}
--dada un elemento "e" y una lista [t] devolver bool(segun si pertenece o no)

pertenece :: (Eq t) => t -> [t] -> Bool 
pertenece t []       = False 
pertenece t (x : xs) | t == x    = True
                     | otherwise = pertenece t xs 



{-EJERCICIO 2.2-}
todosIguales :: (Eq t) => t -> [t] -> Bool 
todosIguales t []       = True 
todosIguales t (x : xs) | t /= x    = False
                     | otherwise = todosIguales t xs 

























{-
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

--}