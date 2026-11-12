-- Ejercicio 1
ejercicio1 :: [Integer] -> Integer -> [Integer]
ejercicio1 (x:y:xs) n | x * y == n   = xs
                      | otherwise    = [x] ++ [y] ++ ejercicio1 xs n  


--AUX: que no utilice pero sirve para modularizar
parsConsecutivos :: Integer -> Integer-> Integer -> Bool
parsConsecutivos x y n
        | x * y == n  = True
        | otherwise   = False
