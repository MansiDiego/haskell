--Cantidad de numeros abundantes--
--Ejercicio 1;

cantidad_de_numeros_abundantes ::  Integer -> Integer -> Integer 
cantidad_de_numeros_abundantes d h 
        | d == h && es_abundante h       = 1
        | d == h && not (es_abundante h) = 0
        | es_abundante h                 = 1 + cantidad_de_numeros_abundantes d (h-1)
        | otherwise                      = cantidad_de_numeros_abundantes d (h-1)   


--aca esta la papa
es_abundante :: Integer -> Bool
es_abundante n 
        | suma_divisores_propios n (n-1) > n = True
        | otherwise                          = False


suma_divisores_propios :: Integer -> Integer -> Integer
suma_divisores_propios n 0 = 0
suma_divisores_propios n d 
        | mod n d == 0   = d + suma_divisores_propios n (d-1)
        | otherwise      = suma_divisores_propios n (d-1) 


---
---2---
cursadas_vencidas :: [(String, Integer, Integer)] -> [String]
cursadas_vencidas [] = []
cursadas_vencidas ((materia, año, cuatrimestre) : xs)
            | (vencio (materia, año, cuatrimestre)) = materia : cursadas_vencidas xs
            | otherwise                             = cursadas_vencidas xs
    

--aux: recibe una tripla y te determina si esa materia esta vencida o no
vencio :: (String, Integer, Integer) -> Bool
vencio (materia, año, cuatrimestre) 
            | año < 2021 = True
            | año == 2021 && cuatrimestre <= 1 = True
            | otherwise = False 








--3--
saturar_en_umbral_hasta_negativo :: [Integer] -> Integer -> [Integer]
saturar_en_umbral_hasta_negativo [] _ = []
saturar_en_umbral_hasta_negativo [x] u 
        | x >= 0  && x <= u = [x]
        | otherwise         = [u]
saturar_en_umbral_hasta_negativo (x:xs) u
        | x >= 0 && x <= u = x : saturar_en_umbral_hasta_negativo xs u
        | x >= 0 && x > u  = u : saturar_en_umbral_hasta_negativo xs u
        | otherwise        = []




--Cantidad Pares columna--
--La idea es ir laburando con un contador e ir elimnando elementos de la fila y e ir incrementando el contador, hasta llegar al numero de columna que quiero, y ahi hacer la modificiacion que yo quiera
--4
cantidad_de_pares_en_columna :: [[Integer]] -> Integer -> Integer
cantidad_de_pares_en_columna [] _ = 0
cantidad_de_pares_en_columna (fila:filas) columna
        | (condicion fila columna 0) = 1 + cantidad_de_pares_en_columna filas columna
        | otherwise                  = cantidad_de_pares_en_columna filas columna


condicion :: [Integer] -> Integer -> Integer -> Bool
condicion [] _ _ = False
condicion (x:xs) c j 
        | j == (c - 1) && mod x 2 == 0 = True
        | j == (c - 1) && mod x 2 /= 0 = False
        | otherwise              = condicion xs c (j+1)

--finalizado en 46 minutos(tiempo record)--2025 primer cuatri