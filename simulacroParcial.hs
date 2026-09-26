
sumaDivisores :: Integer -> Integer -> Integer
sumaDivisores elemento divisor | divisor == 1 = 1
                               | divisor == 0 = 0
                               | esDivisor elemento divisor  = divisor + sumaDivisores elemento (divisor - 1)
                               | otherwise                   = sumaDivisores elemento (divisor - 1)


esDivisor :: Integer -> Integer -> Bool
esDivisor elemento divisor | mod elemento divisor == 0 = True
                           | otherwise                 = False 

---
---

{-EJERCICIO 2 DEL PARCIAL-}
f2 :: [(String, Integer , Integer )] -> [String] 
f2 [] = []
f2 ((materia, anio, cursada):xs) | vencio (materia, anio, cursada) && pertenece materia (f2 xs)            = f2 xs
                                 | vencio (materia, anio, cursada) && pertenece materia (f2 xs) == False   = materia : (f2 xs)
                                 | otherwise                                                               = f2 xs 


type Cursada      = (Materia, Anio, Cuatrimestre)
type Materia      = String
type Anio         = Integer 
type Cuatrimestre = Integer  

--SE PUEDE LLAMAR A LOS ELEMENTOS DE LA TUPLA SIMPLEMENTE CON EL NOMBRE DE SU VARIABLE, Y LISTORTI
vencio :: Cursada -> Bool
vencio (materia, anio, cuatrimestre) | anio - 1993 == 28 && cuatrimestre <= 1 = True
                                     | anio - 1993 < 28                       = True
                                     | otherwise                              = False


pertenece :: (Eq t ) => t -> [t] -> Bool
pertenece t [] = False
pertenece t (x : xs)  | t == x       = True
                      | otherwise    = pertenece t xs




---
---
{-EJERCICIO 3-}
--Y lo declarativo?
f3 :: [Integer] -> Integer -> [Integer]
f3 [] _      = []     
f3 (x: xs) u | x >= 0 && x <= u = x : f3 xs u
             | x >= 0 && x > u  = u : f3 xs u
             | x < 0 = []