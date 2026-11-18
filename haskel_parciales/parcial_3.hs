media_movil :: [Integer] -> Integer -> Float
media_movil [] _ = 0
media_movil [x] n 
        | n == 1    = fromIntegral x
        | otherwise = 0
media_movil (x:xs) n =  promedio (ultimos_n_elementos (reverseBiss2 (x:xs)) n) 

--auxiliar Principal
ultimos_n_elementos :: [Integer] -> Integer -> [Integer]
ultimos_n_elementos _ 0 = []
ultimos_n_elementos (x:xs) n = x : ultimos_n_elementos xs (n-1)



promedio :: [Integer] -> Float
promedio [] = 0
promedio [x] = fromIntegral x
promedio (x:xs) = fromIntegral (sumatoria (x:xs)) / fromIntegral (longitud_media_movil (x:xs))


--AUXILIARES:

reverseBiss2 :: [Integer] -> [Integer]
reverseBiss2 [] = []
reverseBiss2 [x] = [x]
reverseBiss2 (x:xs) = reverseBiss2 xs ++ [x]

longitud_media_movil :: [Integer] -> Integer
longitud_media_movil [] = 0
longitud_media_movil [x] = 1
longitud_media_movil (x:xs) = 1 + longitud_media_movil xs

sumatoria :: [Integer] -> Integer 
sumatoria [] = 0
sumatoria [x] = x
sumatoria (x:xs) = x + sumatoria xs



--2-- Es Atractivo
es_atractivo_principal :: Integer -> Bool 
es_atractivo_principal n = es_primo (es_atractivo n (n-1)) 


es_atractivo :: Integer -> Integer -> Integer
es_atractivo _ 0 = 0
es_atractivo n d
        | d == 0 = 0
        | mod n d == 0 && es_primo d = 1 + es_atractivo n (d - 1)
        | otherwise = es_atractivo n (d - 1)

es_primo :: Integer -> Bool
es_primo n 
        | n <= 1 = False
        | n == 2 = True
        | suma_de_divisores n 2 > 0 = False
        | otherwise                 = True


suma_de_divisores :: Integer -> Integer -> Integer 
suma_de_divisores n d 
        | d == n = 0
        | mod n d == 0 = d + suma_de_divisores n (d + 1)
        | otherwise    = suma_de_divisores n (d + 1)


--completar mañana  60 min 2 ejercicios a pelo re cansado pero chill y bien-- 

--ejercicio 3---
palabra_ordenada :: String -> Bool
palabra_ordenada [] = True
palabra_ordenada [x] = True 
palabra_ordenada (x:y:xs)
                | x ==' '     = palabra_ordenada (y:xs)
                | x <= y       = palabra_ordenada (y:xs)
                | otherwise   = False



--Ejercicio 4--
--Anagrama--

similar_anagrama :: String -> String -> Bool
similar_anagrama [] []   = True
similar_anagrama [x] [y] = False
similar_anagrama (x:xs) (y:ys)
                | (mismos_caracteres (x:xs) (y:ys)) && (posiciones_distinas (x:xs) (y:ys)) = True
                | otherwise = False


---Me falta una funcion que se fije que exista por lo menos una posicion distinta:
posiciones_distinas :: String -> String -> Bool
posiciones_distinas [] []  = False
posiciones_distinas [x] [] = False
posiciones_distinas [] [y] = False
posiciones_distinas (x:xs) (y:ys)
                | x == y    = posiciones_distinas xs ys
                | otherwise = True





---Tienen los mismos caracteres, es decir ambas estan contenidas
mismos_caracteres :: String -> String -> Bool 
mismos_caracteres (x:xs) (y:ys)
                | caracteres_pertenecen_a_palabra (x:xs) (y:ys) && caracteres_pertenecen_a_palabra (y:ys) (x:xs) = True
                | otherwise                                                                                      = False




--Con esta funcion nos fijamos que todos los caracteres de una palabra esten en la otra palabra
caracteres_pertenecen_a_palabra :: String -> String -> Bool
caracteres_pertenecen_a_palabra (x:xs) [] = True
caracteres_pertenecen_a_palabra (x:xs) (y:ys)
                | pertenece_a_la_palabra (x:xs) y = caracteres_pertenecen_a_palabra (x:xs) ys
                | otherwise                       = False



quitar_blancos :: String -> String 
quitar_blancos [] = []
quitar_blancos (x:xs) 
                | x/=' '   = x : quitar_blancos xs
                | x == ' ' = quitar_blancos xs



pertenece_a_la_palabra :: String -> Char -> Bool
pertenece_a_la_palabra [] _ = False
pertenece_a_la_palabra (x:xs) caracter
                | x == caracter = True
                | otherwise     = pertenece_a_la_palabra xs caracter

--Nota 9, el ejercicio de anagramas es peculiar, la idea es ir eliminando elementos de la primer palabras con la segunda, y luego si se vacian al mismo tiempo entonces son anagramas
--rehacer--1 parcial 2c 2024
