{--recursion doble--}
recursion_doble :: Integer -> Integer -> Integer
recursion_doble 0 _ = 0
recursion_doble i m = aux i m m


aux :: Integer -> Integer -> Integer -> Integer
aux i m j
    | j == 0    = i^j + recursion_doble (i-1) m
    | otherwise = i^j + aux i m (j-1)

--La idea general de la recursion, lo haces para toda la cola y vez que condicion pones de finalizacion para el primer caso, la cabeza es el problema, no la cola.
