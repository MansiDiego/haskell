{-Deshacer el último cambio: Presioná Ctrl + Z (en Windows/Linux). Cada vez que lo tocás vuelve un paso hacia atrás en el historial de edición del archivo actual. Si te pasás volviendo, con Ctrl + Y (o Ctrl + Shift + Z) rehacés lo deshecho.-}

-- EJERCICIO 1 (2 puntos)
-- problema mediaMovilN (lista: seq⟨Z⟩, n: Z) : Float {
--   requiere: {|lista| > 0}
--   requiere: {n > 0 ∧ n ≤ |lista|}
--   asegura: {res es el promedio de los últimos n elementos de lista}
-- }


{--
---{EJERCICIO 1} (2PUNTOS), 50":20s'}

mediaMovilN :: [Integer] -> Integer -> Float 
mediaMovilN (x : xs) 1 = ultimoElemento (x:xs)
mediaMovilN (x : xs) n = (sumaDeUltimosNelementos (x:xs) n) / (fromIntegral n) 
--mediaMovilN [x] 1      = fromIntegral x El caso base de n=1 queda cubierto con mi auxiliar

ultimoElemento :: [Integer] -> Float 
ultimoElemento [x]    = fromIntegral x   
ultimoElemento (x:xs) = ultimoElemento xs 


sumaDeUltimosNelementos :: [Integer] -> Integer -> Float 
sumaDeUltimosNelementos (x:xs) 0 = 0
sumaDeUltimosNelementos (x:xs) n = ultimoElemento (x : xs) + sumaDeUltimosNelementos (sacaUltimoElemento (x:xs)) (n - 1)
--Me faltaba una auxiliar que saque el Ultimo Elemento a la lista


sacaUltimoElemento :: [Integer] -> [Integer] 
sacaUltimoElemento [x]    = []
sacaUltimoElemento (x:xs) = x : [] ++ sacaUltimoElemento xs 


---


-- EJERCICIO 2 (2 puntos)    n>0
-- problema esAtractivo (n: Z) : Bool {
--   requiere: {n > 0}
--   asegura: {res = true <=> la cantidad de factores primos de n (distintos o no) es también un número primo.}
-- }
-- Aclaración: los factores primos de 30 son [5,3,2]. Los factores primos de 9 son [3,3]. 

{-EJERCICIO 2} 42"00' (2 PUNTOS)-}
esAtractivo :: Integer -> Bool
esAtractivo 1 = False
esAtractivo n = esPrimo (longitudDelosFactoresPrimosDeN (factoresPrimos n (n-1)))

--AUX1
--Descomposición de N en factores primos 
factoresPrimos :: Integer -> Integer -> [Integer]
factoresPrimos 2 _        = [2]
factoresPrimos n 1        = []
factoresPrimos n indice | mod n indice == 0 && esPrimo (indice) = indice : [] ++ factoresPrimos n (indice - 1)
                        | otherwise                              = factoresPrimos n (indice - 1)

--AUX2
longitudDelosFactoresPrimosDeN :: [Integer] -> Integer
longitudDelosFactoresPrimosDeN [x] = 1
longitudDelosFactoresPrimosDeN (x:xs) = 1 + longitudDelosFactoresPrimosDeN xs

--AUX3
esPrimo :: Integer -> Bool 
esPrimo 1 = False
esPrimo 2 = True 
esPrimo n | sumaDeDivisores n n == n + 1 = True
          | otherwise                    = False

--AUX4
sumaDeDivisores :: Integer -> Integer -> Integer  
sumaDeDivisores n 1 = 1
sumaDeDivisores n i | mod n i == 0 = i + sumaDeDivisores n (i - 1)
                    | otherwise    = sumaDeDivisores n (i - 1)

--"REPASAR CREAR FUNCION NUMEROS PRIMOS"--


--


-- EJERCICIO 3 (2 puntos)
-- problema palabraOrdenada (palabra: seq⟨Char⟩) : Bool {
--   requiere: {True}
--   asegura: {res = true <=> cada uno de los elementos no blancos de palabra es mayor o igual al anterior caracter no blanco, si existe alguno.}
-- }
-- Aclaración: 'a' < 'b' es True. 


palabraOrdenada :: [Char] -> Bool
palabraOrdenada []  = True
palabraOrdenada [x] = True
palabraOrdenada (x:y:xs) | primerChar <= charSiguiente = palabraOrdenada xs
                         | otherwise = False
        where 
        primerChar    = primerElemento (quitarEspacios (x:y:xs)) 
        charSiguiente = primerElemento (quitarEspacios (y:xs))

primerElemento :: [Char] -> Char 
primerElemento [x] = x
primerElemento (x:xs) = x


quitarEspacios :: [Char] -> [Char]
quitarEspacios [] = []
quitarEspacios (x:xs) 
        | x /= ' '  = x : quitarEspacios xs
        | otherwise = quitarEspacios xs 

 --HASKELL UTILIZA EL ESTANDAR ASCII, CON LO CUAL A < B, PORQUE SU CODIGO INTERNO NUMERICO ES A= 97 Y B = 98



---REHACER MAÑANA---
-- EJERCICIO 4 (3 puntos)
-- problema similAnagrama (palabra1: seq⟨Char⟩, palabra2: seq⟨Char⟩) : Bool⟩{
--   requiere: {True}
--   asegura: {res = true <=> (para todo caracter no blanco, la cantidad de apariciones de ese caracter en palabra1 es igual a la cantidad de apariciones en palabra2, y además existe al menos un caracter en palabra1 que tiene una posición distinta en palabra2)}
-- }

--Principal
similAnagrama :: String -> String -> Bool
similAnagrama (x:xs) (y:ys)
                | sonLaMismaPalabra (palabra1Limpia) (palabra2Limpia)                                                                           = False
                | (longitudDeLaPalbra (palabra1Limpia) == longitudDeLaPalbra (palabra2Limpia)) && perteneceBiss  palabra1Limpia palabra2Limpia  = True
                | otherwise                                                                                                                     = False
                where 
                palabra1Limpia = sacaBlancossBiss (x : xs)
                palabra2Limpia = sacaBlancossBiss (y : ys)

--AUX SACA LOS BLANCOS
sacaBlancossBiss :: String -> String
sacaBlancossBiss [] = []
sacaBlancossBiss (x : xs)
                | x == ' '  = sacaBlancossBiss xs
                | otherwise = x : sacaBlancossBiss xs 


--DESCARTA EL CASO QUE SEAN LA MISMA PALABRA, POR EJEM; MATEO MATEO
sonLaMismaPalabra :: String -> String -> Bool
sonLaMismaPalabra [] []       = True
sonLaMismaPalabra (x : xs) (y : ys)
                | x == y      = sonLaMismaPalabra xs ys
                | otherwise   = False


--AUX Longitud, LA IDEA DE ESTA AUXILIAR ES QUE YA RECIBE PALABRAS LIMPIAS DE "BLANCOS", Por algo hice la funcion sacar blancos
longitudDeLaPalbra :: String -> Integer 
longitudDeLaPalbra [] = 0
longitudDeLaPalbra (x:xs) = 1 + longitudDeLaPalbra xs


--AUX Pertenece
pertenece :: Char -> String -> Bool
pertenece letra [] = False
pertenece letra (x : xs) 
                | letra == x = True
                | otherwise  = pertenece letra xs

--AUX complementaria de pertenece, para determinar si A Contenida en B
perteneceBiss :: String -> String -> Bool
perteneceBiss [] _ = True
perteneceBiss (x:xs) (y:ys) 
                | pertenece x (y:ys) = perteneceBiss xs (y:ys)
                | otherwise          = False

--}
{-PARCIAL DEL 2024 2C-}


{--
* Ejercicio 1

problema hayPrimosGemelos (d: Z,h: Z) : Bool {
  requiere: {0 < d â‰¤ h}
  asegura: {res = true <=> existen dos numeros p1 y p2 contenidos en el rango [d..h] tales que p1 y p2 son primos gemelos}
}

AclaraciÃ³n: Se dice que p1 y p2 son primos gemelos si ambos son primos y ademÃ¡s |p2-p1| = 2
--}

--Principal
hayPrimosGemelos :: Integer -> Integer -> Bool
hayPrimosGemelos _ 0 = False
hayPrimosGemelos d h  
                | d == 1 && h == 1             = False
                | d == h   && d/=1             = False
                | (recorreD d h) == True       = True
                | otherwise                    = hayPrimosGemelos d (h-1)


recorreD :: Integer -> Integer -> Bool
recorreD d h 
        | d == 1                                            = recorreD (d+1) h
        | d == h = False
        | esPrimo d && esPrimo h && (absoluto (d - h) == 2) = True
        | otherwise                                         = recorreD (d+1) h 


--aux valor absoluto
absoluto :: Integer -> Integer 
absoluto x
        | x >= 0    = x
        | otherwise = (-x)


--aux
esPrimo :: Integer -> Bool
esPrimo p
        | sumaDeDivisoresB p indice == (p+1) = True
        | otherwise                          = False
        where
        indice = p


--aux para la funcion que determina si un numero es primo, basado en la logica que la suma de los divisores de un numero primos son el 1 y el mismo primo, entonces la suma de todos los divisores de un numero primo es igual a p+1
sumaDeDivisoresB :: Integer -> Integer -> Integer
sumaDeDivisoresB n 0 = 0
sumaDeDivisoresB n indice
                | mod n indice == 0 = indice + sumaDeDivisoresB n (indice - 1)
                | otherwise         = sumaDeDivisoresB n (indice - 1)

{-"VALOR 2 PUNTOS"-}

{-
* Ejercicio 2

Representaremos un dia de cursada de cierta materia con una tupla String x String x Z x Z, donde:

    La primera componente de la tupla contiene el nombre de una materia
    La segunda componente de la tupla contiene el dÃ­a de cursada (lunes, martes, etc)
    La tercera componente de la tupla contiene el horario de inicio de la cursada de ese dÃ­a
    La cuarta componente de la tupla contiene el horario de fin de la cursada de ese dÃ­a

Se pide implementar materiasTurnoTarde, que dada una lista de cursadas devuelva aquellas materias que se cursan en el turno tarde (14 a 17hs)

problema materiasTurnoTarde (s: seqâŸ¨String x String x Z x ZâŸ©) :seqâŸ¨StringâŸ© {
  requiere: { s[i]1 es alguno de los siguientes valores: "Lunes", "Martes", "MiÃ©rcoles", "Jueves", "Viernes"}
  requiere: { s[i]2 â‰¥ 8 para todo i tal que 0 â‰¤ i < |s|}
  requiere: { s[i]3 â‰¤ 22 para todo i tal que 0 â‰¤ i < |s|}
  requiere: { s[i]2 < s[i]3 para todo i tal que 0 â‰¤ i < |s|}
  asegura: { res no tiene elementos repetidos}
  asegura: { res contiene los nombre de todas las materias incluÃ­das en s tales el horario de cursada de dichas materias se superpone (total o parcialmente) con el rango (14..17)}
  asegura: { res contiene solamente los nombre las materias incluÃ­das en s tales el horario de cursada de dichas materias se superpone (total o parcialmente) con el rango (14..17)}
}
-}

--Principal
materiasTurnoTarde :: [(String, String, Integer, Integer)] -> [String]
materiasTurnoTarde [] = []
materiasTurnoTarde ((materia, dia, horarioInicio, horarioFin) : xs) 
                | esTurnoTarde (materia, dia, horarioInicio, horarioFin) && not estaRepetida = materia : [] ++ materiasTurnoTarde xs 
                | otherwise                                                                  = materiasTurnoTarde xs
                where
                estaRepetida = pertenece materia xs
                

--Dado que x representa la primer tupla dentro de la lista de tuplas

--AUX: Me determina si la materia pertenece al rango horario
esTurnoTarde :: (String, String, Integer, Integer) -> Bool
esTurnoTarde (materia, dia, horarioInicio, horarioFin)
                | horarioInicio >= 14 && horarioFin <= 17 = True
                | otherwise                               = False
                

{--
--Ahora me gustaria hacer una funcion que me quite todos las materias repetidas--Funcion secundaria
cursadaLimpia :: [(String, String, Integer, Integer)] -> [(String, String, Integer, Integer)]
cursadaLimpia [] = []
cursadaLimpia (x:xs) 
                | pertenece x xs = cursadaLimpia xs
                | otherwise      = x : cursadaLimpia xs
--}

--AUX de la secundaria:
pertenece :: String -> [(String, String, Integer, Integer)] -> Bool
pertenece materia [] = True
pertenece materia ((materia2, dia2, horarioInicio2, horarioFin2): xs)
                | materia == materia2 = True
                | otherwise           = False

--REVISAR LUEGO LA FUNCION "PERTENECE"

{-
problema sumaIesimaColumna (matriz: seq⟨seq⟨Integer⟩⟩, col: Integer) : Integer {
  requiere: {Todos los elementos de la secuencia matriz tienen la misma longitud}
  requiere: {|matriz| > 0}
  requiere: {|matriz[0]| > 0}
  requiere: {1 ≤ col ≤ |matriz[0]|}
  asegura: {res es la sumatoria de los elementos matriz[i][col-1] para todo i tal que 0 ≤ i < |matriz|}
-}

sumaIesimaColumna :: [[Integer]] -> Integer -> Integer 
sumaIesimaColumna [] _         = 0
sumaIesimaColumna (fila : xs ) numeroCol = obtenerElemento fila numeroCol + sumaIesimaColumna xs numeroCol
 

--AUX NECESITO UNA AUXILIAR QUE AL PASARLE un nro de COLUMNA Y UYNA FILA ME DEVUELVA EL ELEMENTO QUE QUIERO OBTENER
obtenerElemento :: [Integer] -> Integer -> Integer
obtenerElemento [] _     = error "indice fuera de rango"
obtenerElemento (x:_) 1  = x
obtenerElemento (_:xs) c = obtenerElemento xs (c - 1)

{-EJERCICIO MUY SENCILLO, PERO ME COSTO PORQUE NO SABIA COMO OBTENER EL ELEMENTO EN COLUMNA EN CUESTION-}




--
--
{-EJERCICIO 3-}
{--
problema maximaSumaDeTresConsecutivos (s: seq⟨ℤ⟩) : ℤ {
  requiere: { |s| ≥ 3 }
  asegura: { res es la suma de tres elementos que se encuentran en posiciones consecutivas de s }
  asegura: { Para cualquier i en el rango 1 ≤ i < |s|-1, se cumple que s[i-1] + s[i] + s[i+1] ≤ res }
--}


maximaSumaDeTresConsecutivos :: [Integer] -> Integer 
maximaSumaDeTresConsecutivos (x:xs) = primeraPos + segundaPos + terceraPos 
                where
                primeraPos = obtenerElementoB (x:xs) 1
                segundaPos = obtenerElementoB (x:xs) 2
                terceraPos = obtenerElementoB (x:xs) 3


--AUX: RECIBE EL NUMERO DE COLUMNA, Y ME DEVUELVE EL ELEMENTO QUE ESTA EN ESA POSICION, ARRANCANDO DESDE 1
obtenerElementoB :: [Integer] -> Integer -> Integer
obtenerElementoB [] _     = error "indice fuera de rango"
obtenerElementoB (x:_) 1  = x
obtenerElementoB (_:xs) n = obtenerElementoB xs (n-1)   


--MEJORA PORQUE EL ENUNCIADO ESTA COMO EL OGT
maximaSumaDeTresConsecutivosBis ::  [Integer] -> Integer
maximaSumaDeTresConsecutivosBis [x,y,z] = (x + y + z)
maximaSumaDeTresConsecutivosBis (x:y:z: xs)
                | x + y + z > loAnterior = x + y + z 
                | otherwise              = loAnterior --LO ANTERIOR NO HACE REFERENCIA A UNA POSICION EN LA FILA, SINO QUE HACE REFERENCIA A OTRA SUMA DE 3 NUMEROS CONSECTUIVOS
                where                                 -- QUE ESTAN LUEGO DE NUESTRA SUMA DE 3 NUMEROS CONSECUTIVOS
                loAnterior = maximaSumaDeTresConsecutivosBis (y: z : xs)




{-OTRO PARCIAL-}

{--EJERCICIO 4 DE MATRIZ--}
--REMPLAZA EL MINIMO DE CADA FILA
{--
reemplazarMinimoDeCadaFila :: [[Integer]] -> Integer -> [[Integer]]
reemplazarMinimoDeCadaFila 
--}

--Busca el minimo, y cuando llega al minimo lo remplaza
minimo :: [Integer] -> Integer -> [Integer]
minimo [] n = [n]
minimo (x: y : xs) n 
                | x <= y     =  minimo (y:xs) n
                | otherwise = x : minimo xs n  