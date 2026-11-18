-- Ejercicio 1
ejercicio1 :: [Integer] -> Integer -> [Integer]
ejercicio1 [] n = [] --voy a llegar a este caso base 
-- ejercicio1 [x] n = [x] --si le queda un solo elemento devuelve un solo elemento
ejercicio1 (x: y :xs) n | x * y == n   = ejercicio1 xs n 
                        | otherwise    =  x :  ejercicio1 (y:xs) n 
                        
                        --hacerlo de esta manera lo que me genera es que sino cumple lo pedido los agrego directamente, pero puede que me elimine un caso en el que si cumpla y lo omito por la forma de recorrer recursivamente
                            


--aritmetica:
-- * producto: a * b = devuelve un integer
-- division a/b     = devuelve un float
-- div a b = te devuelve la cantidad de veces que entra b en a
-- mod a b = te devuelve el resto de a dividido por b
--Cadena de caracteres = [Char]= ['m', 'a', 't', 'e', 'o'] == String "mateo", para concatenar listas usamos ++
--fst y snd me dan el primer valor de una dupla y el segundo valor de una dupla(dupla son tuplas de 2 elementos), estas operaciones fst y snd solo funcionan en duplas
-- fromintegral recibe un argumento (tipo numero entero) y lo convierte en algo mas general, util para trabajar con enteros y floats a la vez


--FACT:
factorial :: Integer -> Integer
factorial 0 = 1
factorial x = x * factorial ( x - 1 )

-- FIBONACCI:
fibonacci :: Integer -> Integer 
fibonacci 0 = 1
fibonacci 1 = 1
fibonacci n = fibonacci(n-1) + fibonacci(n - 2)

--Maximo de una lista:
maximo :: [Integer] ->  Integer
maximo []     = 0
maximo [x]    = x 
maximo (x:xs) 
        | x > maxsimoCola = x
        | otherwise  = maxsimoCola
        where maxsimoCola = maximo xs

minimo :: [Integer] -> Integer
minimo [] = 0
minimo [x] = x
minimo (x:xs)
        | x < minimo xs = x
        | otherwise  = minimo xs


---replicate
replicateBiss :: Integer -> Integer -> [Integer]
replicateBiss n x
        | n <= 0     = []
        | otherwise  = x : replicateBiss (n - 1) x


---take;
takeBiss :: Integer -> [Integer] -> [Integer]
takeBiss n [] = []
takeBiss n (x:xs)
        | n <= 0 = []
        | otherwise = x : takeBiss (n-1) xs


--reverse ;
reverseBiss :: [Integer] -> [Integer]
reverseBiss [x] = [x]
reverseBiss []  = []
reverseBiss (x:xs) = reverseBiss xs ++ [x]

---pertenece ;
perteneceBisss :: [Integer] -> Integer -> Bool
perteneceBisss [] _ = False
perteneceBisss (x:xs) n 
        | x == n    = True
        | otherwise = perteneceBisss xs n





-- --Principal;
cantidadSinDigitosRepetidos :: Integer -> Integer -> Integer
cantidadSinDigitosRepetidos d h 
        | d == h  && (digitos_repetidos (digitos_en_lista d))          = 0
        | d == h  && (digitos_repetidos (digitos_en_lista d)) == False = 1 
        | digitos_repetidos (digitos_en_lista h) == False              = 1 + cantidadSinDigitosRepetidos d (h - 1)
        | otherwise                                                    = 0 + cantidadSinDigitosRepetidos d (h - 1)


--voy a aplicar una solucion recursiva para recorrer los digitos del numero en cuestion
digitos_repetidos :: [Integer] -> Bool
digitos_repetidos []  = False
digitos_repetidos (x:xs) 
        | pertence_digito_a_lista xs x = True
        | otherwise                    = digitos_repetidos xs 


digitos_en_lista :: Integer -> [Integer]
digitos_en_lista 0 = []
digitos_en_lista n = mod n 10 : [] ++ digitos_en_lista (div n 10)


pertence_digito_a_lista :: [Integer] -> Integer -> Bool
pertence_digito_a_lista [] _ = False
pertence_digito_a_lista [x] e 
                        | x /= e    = False
                        | otherwise = True   
pertence_digito_a_lista (x:xs) e 
                        | x == e    = True
                        | otherwise = pertence_digito_a_lista xs e




---ejercicio 5;
distanciaEntreExtremosDelMaximo :: [Integer] -> Integer 
distanciaEntreExtremosDelMaximo [x] = 0
distanciaEntreExtremosDelMaximo (x:xs) = posicion_final_extremo(x:xs) - (primera_aparicion (x:xs) (extremo_maximo(x:xs)))

--aux_5:
posicion_final_extremo :: [Integer] -> Integer 
posicion_final_extremo [x] = 0
posicion_final_extremo (x:xs) = (longitud_lista (x:xs)) - (primera_aparicion  (lista_invertida(x:xs)) (extremo_maximo(x:xs))) - 1

longitud_lista :: [Integer] -> Integer 
longitud_lista []  = 0
longitud_lista [x] = 1
longitud_lista (x:xs) = 1 + longitud_lista xs


lista_invertida :: [Integer] -> [Integer]
lista_invertida [x] = [x]
lista_invertida []  = []
lista_invertida (x:xs) = lista_invertida xs ++ [x]


extremo_maximo :: [Integer] -> Integer
extremo_maximo (x:[]) = x
extremo_maximo (x:xs)
        | x > extremo_maximo xs = x
        | otherwise = extremo_maximo xs



    --Busco la primera aparicion de mi elemento
primera_aparicion :: [Integer] -> Integer -> Integer 
primera_aparicion [] _ = 0
primera_aparicion (x:xs) e
            | x == e = 0
            | otherwise = 1 + primera_aparicion xs e 

---
--Ejercicio 6 matrices

ejercicio6 :: [[Integer]] -> [[Integer]]
ejercicio6 matriz = modificarMatriz matriz 0


-- Recorremos las filas de la matriz
modificarMatriz :: [[Integer]] -> Integer -> [[Integer]]
modificarMatriz [] _ = []
modificarMatriz (fila:filas) i =
        modificarFila fila i : modificarMatriz filas (i + 1)


-- Modificamos el elemento correspondiente de cada fila
modificarFila :: [Integer] -> Integer -> [Integer]
modificarFila (x:xs) 0
        | mod x 2 == 0 = 0 : xs
        | otherwise   = 1 : xs
 
modificarFila (x:xs) i =
        x : modificarFila xs (i - 1)
