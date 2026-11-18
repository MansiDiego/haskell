-- primer cuatri de 2025:--

hay_primos_gemelos :: Integer ->  Integer -> Bool 
hay_primos_gemelos d h 
            | d + 2 > h                            = False
            | es_primoBiss d && es_primoBiss (d+2) = True
            | otherwise                            = hay_primos_gemelos (d+1) h


es_primoBiss :: Integer  -> Bool
es_primoBiss n 
    | n <= 1                     = False
    | suma_de_divisores n 2 == 0 = True
    | otherwise                  = False

suma_de_divisores :: Integer -> Integer -> Integer 
suma_de_divisores n d 
                    | n == d            = 0
                    | mod n d == 0      = 1
                    | otherwise         = suma_de_divisores n (d + 1)




---  2PUNTOS   ---
---ejercicio 2 ---

materias_turno_tarde :: [(String, String, Integer, Integer)] -> [String]
materias_turno_tarde [] = []
materias_turno_tarde ((materia, dia, inicio, fin) : xs) 
                        | (inicio >= 14) && (inicio < 17) && (fin <= 22) && (pertenece_a_la_semana dia) = materia : materias_turno_tarde xs  
                        | otherwise   = materias_turno_tarde xs


pertenece_a_la_semana :: String -> Bool
pertenece_a_la_palabra [] = False 
pertenece_a_la_semana (x:xs) 
                | (x:xs) == "Lunes"     = True
                | (x:xs) == "Martes"    = True
                | (x:xs) == "Miercoles" = True
                | (x:xs) == "Jueves"    = True
                | (x:xs) == "Viernes"   = True
                | otherwise = False


--Ejercicio 3--
maxima_suma_de_tres_consecutivos :: [Integer] -> Integer
maxima_suma_de_tres_consecutivos [] = 0
maxima_suma_de_tres_consecutivos [x,y,z] = sumatoria [x,y,z]
maxima_suma_de_tres_consecutivos (x: y: z: xs)
            | sumatoria (x: y: z: []) > maxima_suma_de_tres_consecutivos (y:z:xs) = sumatoria [x,y,z]
            | otherwise = maxima_suma_de_tres_consecutivos (y:z:xs)


sumatoria :: [Integer] -> Integer 
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs


--Matrices--Ejercicio 4 2,5 puntos
suma_elementos_de_iesima_columna :: [[Integer]] -> Integer -> Integer 
suma_elementos_de_iesima_columna [] _ = 0
suma_elementos_de_iesima_columna (fila:filas) c = suma_elementos_de_la_columna_c_de_indice_j fila c 0 + suma_elementos_de_iesima_columna filas c


--Columna funciona como indice, pero tengo que convertir el valor a indice
suma_elementos_de_la_columna_c_de_indice_j :: [Integer] -> Integer -> Integer -> Integer 
suma_elementos_de_la_columna_c_de_indice_j (x:xs) c j
                    | (c - 1) == j = x
                    | otherwise = suma_elementos_de_la_columna_c_de_indice_j xs c (j+1) --donde j es el subindice de la columna
---La idea de los ejercicios de matrices es primero que nada recorrer la matriz con filas, lo segundo es con cada fila trabajarla en un auxiliar que le vaya quitando elementos, sino coincide la columna con el subindice, si coinciden entonces estoy parado sobre el elemento que quiero modificar, modifico el elemento y lo devuelvo, eso es lo que agarra la funcion principal