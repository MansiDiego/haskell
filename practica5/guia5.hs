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
reverso1 :: [t] -> [t]
reverso1 []       = [] --seria mi caso base
reverso1 (x : xs) = reverso1 xs ++ [x] 
-- ++ Concatena 2 listas, y [x] es la lista unitaria



{-EJERCICIO 2.1-}
--dada un elemento "e" y una lista [t] devolver bool(segun si pertenece o no)

pertenece :: (Eq t) => t -> [t] -> Bool 
pertenece t []       = False 
pertenece t (x : xs) | t == x    = True
                     | otherwise = pertenece t xs 



--2.2
--Todos iguales que dada una lista de elementos, devuelve true si y solo si todos sus elementos son iguales.
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [x]     = True
todosIguales []      =  True
todosIguales (x:xs) | pertenece x xs = todosIguales xs
                    | otherwise      = False


--2.3
--devuelve falso si hay 2 elementos repetidos en la lista, y devuelve true si todos los elementos son distintos
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [x] = True
todosDistintos []  = True
todosDistintos (x : xs) | pertenece x xs = False
                        | otherwise      = todosDistintos xs



--2.4
-- La idea es que si hay al menos un elemento en la lista que aparece 2 veces entonces devolvemos True, si no hay ningun repetido devolvemos false
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos []  = False
hayRepetidos (x : xs) | pertenece x xs = True
                      | otherwise      = hayRepetidos xs



--2.5--
--Dado un elemento "e" y una lista elimina la primer aparicion de e en la lista s (si es que aparece e en la lista s)
quitar :: (Eq t) => t -> [t] -> [t]
quitar x []       = [] 
quitar x (y : ys) |  x == y   = ys
                  | otherwise = y : quitar x ys 


--2.6--
--Dado un elemento "e" y una lista s, elimna toda las apariciones de e en la lista s(si es que e aparece en la lista, sino devuelve la lista tal cual esta)
quitartodosiguales :: (Eq t) => t -> [t] -> [t]
quitartodosiguales x []       = [] 
quitartodosiguales x (y : ys) | x == y    = quitartodosiguales x (quitar x (y : ys))
                              | otherwise = y : quitartodosiguales x ys

--2.7--
--Dada una lista elimina repetidos y devuelve otra lista, dejando a elementos que no se repiten--
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos (x : xs) | (x:xs) == [x]  = [x]
                           | hayRepetidos (x:xs) = eliminarRepetidos xs
                           | otherwise           = x : eliminarRepetidos xs


--2.8--
--mismos elementos, que dada dos listas devuelve verdadero sí y solamente sí ambas listas contienen los mismos elementos sin tener en cuenta la cantidad de repeticiones.
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos xs ts  = contenidadEn xs ts && contenidadEn ts xs

contenidadEn :: (Eq t) => [t] -> [t] -> Bool
contenidadEn [] _        = True
contenidadEn (x : xs) ts = pertenece x ts && contenidadEn xs ts  
---Voy a usar pertenece, que recibe un elemento y una lista y me devuelve un bool, depende lo que corresponda--
--Observar que al pensar modularmente los problemas de listas salen en 2 patadas...--



---AGAIN mismosELementos(metodo guardas):--
mismosElementoss :: (Eq t) => [t] -> [t] -> Bool
mismosElementoss xs ts | contenida xs ts  && contenida ts xs = True
                       | otherwise                            = False

contenida :: (Eq t) => [t] -> [t] -> Bool
contenida [] _ = True
contenida (x : xs) ts | pertenece x ts = contenida xs ts
                      | otherwise      = False


{-EJERCICIO 2.9 -}
capicuaString :: (Eq t) => [t] -> Bool
capicuaString xs | reverso xs == xs = True
                 | otherwise        = False
                

reverso :: (Eq t) => [t] -> [t] 
reverso [] = []
reverso (x:xs) = reverso xs ++ [x] 



{-EJERCICIO 3-}
--dada una lista, devuelve la suma de sus elementos--
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = sumatoria xs + x 


--3.2--
--Productoria, dada una lista devuelve el producto de sus componentes--
productoria :: [Integer] -> Integer 
productoria (x:xs) | (x:xs) == [x] = x
productoria (x:xs) | (x:xs) /= []  = x * productoria xs 


--3.3--
maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x : xs) | x > maximo xs = x
                | otherwise     = maximo xs


--3.4--
sumarN :: Integer -> [Integer] -> [Integer] 
sumarN n [x] = [n + x]
sumarN n [] = []
sumarN n (x:xs) = (n + x) : sumarN n xs

--3.5--
sumarElprimero :: [Integer] -> [Integer]
sumarElprimero (s:xs) = (s+s) : sumarN s xs

--3.6--
{--
SUTIL DIFERENCIA EN LA ESPECIFICACIÓN DE UN ELEMENTO DE LA LISTA: SI DIGO EL ELEMENTO EN POSICIÓN X => e[x]. 
Si quiero mencionar el ultimo elemento perteneciente a un conjunto "e", entonces digo e[|e|-1] ya que todo lo que esta entre corchetes hace referencia a una posición en formato "indice(0=1, 1=2 y etc)", y siempre que tengamos |s| o |x| hace referencia a la longitud con lo que estamos trabajando, es importante a considerar cuando trabajamos con especificaciones mas complejas.--}

sumarElultimo :: [Integer] -> [Integer]
sumarElultimo xs = sumarN (ultimoElemento xs) xs 

ultimoElemento :: [Integer] -> Integer 
ultimoElemento [x] = x 
ultimoElemento (x:xs) = ultimoElemento xs
 
--3.7--
--recibe una lista, y devuelve los elementos que son pares--
pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | esPar x   = x : pares xs
             | otherwise = pares xs


esPar :: Integer -> Bool
esPar n | mod n 2 == 0 = True
        | otherwise    = False


--3.8-- 
--recibe una lista y me devuelve otra lista con todos los elemenentos que son multiplos de n y pertenece a la primer lista.
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN n [] = []
multiplosDeN n (primerElemento : xs) | esMultiplode primerElemento n = primerElemento : multiplosDeN n xs
                                     | otherwise                     = multiplosDeN n xs


esMultiplode :: Integer -> Integer -> Bool
esMultiplode x n | n == 0       = False
                 | mod x n == 0 = True
                 | otherwise    = False



--3.9--
--ordenar, recibe una lista, y devuelve la lista ordenada de forma creciente 
ordenar :: [Integer] -> [Integer]
ordenar [x] = [x]
ordenar xs = ordenar (quitar (maximo xs) xs) ++ [maximo xs ] 

--


--Sacar blancosRepetidos
{--EJERCICIO 4.A--}
sacarBlancosRepetidos ::  String -> String 
sacarBlancosRepetidos []  = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (cabeza: elementopostcabeza : cola) | cabeza == ' ' && elementopostcabeza == ' ' = sacarBlancosRepetidos (elementopostcabeza : cola)
                                                          | otherwise                                  = cabeza : sacarBlancosRepetidos (elementopostcabeza : cola)



{--EJERCICIO 4.B--}
--contar Palabras--
contarPalabras :: String ->  Integer 
contarPalabras [] = 0
contarPalabras texto = contarPalabrasLimpias (limpiartexto texto)

---hay que limpiar los espacios del principio o finales, tambien los espacios dobles "_,_" (suponiendo que los guiones bajos son espacios).
limpiartexto :: String -> String 
limpiartexto (x : xs) = sacarExtremosVacios (sacarBlancosRepetidos (x : xs))

sacarInicio :: String -> String 
sacarInicio (' ': xs) = xs
sacarInicio (x  : xs) = (x:xs)

sacarUltimoElementoVacio :: String -> String 
sacarUltimoElementoVacio [x] = [x]
sacarUltimoElementoVacio (x:xs) = reverso( sacarInicio (reverso(x : xs)) )

sacarExtremosVacios :: String -> String 
sacarExtremosVacios (x : xs) = sacarUltimoElementoVacio (sacarInicio (x:xs))

--basta de auxiliares pfv
contarPalabrasLimpias :: String -> Integer 
contarPalabrasLimpias [x] | x /=' '   = 1
                          | otherwise = 0
contarPalabrasLimpias (x:xs) | x == ' '  = 1 + contarPalabrasLimpias xs
                             | otherwise = contarPalabrasLimpias xs


---
{-4.c-}
--dada una lista devuelve otra lista de listas con las palbras originales, por ejemplo recibe "mateo fulano mengano" devuelve ["mateo", "fulano", "mengano"]


--
palabras :: String -> [String] 
palabras [] = []
palabras (x:xs) = [primeraPalabra (x : xs)] ++ palabras (eliminaPrimerPalabra (x:xs))
 

primeraPalabra :: String -> String
{-- primeraPalabra (x:xs) | (x:xs) == [] = [] ESTO ES INCORRECTO, NUNCA SE LLEGA A EJECUTAR, DADO QUE POR DEFINICION (X:XS) TIENE ALMENOS UN ELEMENTO POR LO TANTO NUNCA VA  A PASAR QUE (X:XS) == [] DADO QUE YA ENTRA CON ALMENOS UN ELMENTO, Y TU RECURSIVIDAD SE LA PASA POR LOS HUEVOS.--}
primeraPalabra [] = []                     
primeraPalabra (x:xs) | x/=' '       = x : primeraPalabra xs
                      | otherwise    = []


eliminaPrimerPalabra :: String -> String
eliminaPrimerPalabra [] = []
eliminaPrimerPalabra (x:xs) | x == ' '     = xs
                            | otherwise    = eliminaPrimerPalabra xs


--4.D PALABRA MAS LARGA--

palabraMasLarga :: String -> String
palabraMasLarga [] = []
palabraMasLarga [primera] = [primera]
palabraMasLarga texto
        | longitudDelString primeraP > longitudDelString mejorDelResto = primeraP
        | otherwise = palabraMasLarga restoDeP
        where 
        primeraP      = primeraPalabra texto
        restoDeP      = eliminaPrimerPalabra texto
        mejorDelResto = palabraMasLarga restoDeP


longitudDelString :: String -> Integer 
longitudDelString [] = 0 
longitudDelString (x:xs) | x /= ' '  = 1 + longitudDelString xs
                         | otherwise = 0


{-4.e-}

aplanar :: [String] -> String
aplanar [x] 
        | [x] /= [" "] = x
        | otherwise    = []
aplanar (x:xs) 
        | x /= " "   = x ++ aplanar xs
        | otherwise  = aplanar xs


{-4.F-}
aplanarConBlancos1 :: [String] -> String 
aplanarConBlancos1 []  = []
aplanarConBlancos1 [x] = x 
aplanarConBlancos1 (x:xs) = x ++ " " ++ aplanarConBlancos1 xs --Basicamente "x" representa el primer string


{--
aplanarConBlancos2 :: [[Char]] -> [Char]
aplanarConBlancos2 []       = []
aplanarConBlancos2 [p]      = p
aplanarConBlancos2 (p : ps) = p ++ " " ++ aplanarConBlancos ps 
--}
--Basicamente "p" representa la primer lista de char y le suma un espacio y lo concatena con la cola aplicando la misma logica


{-4.g-}

f7 :: [[Char]] -> Integer -> [Char]
f7 [] _        = []
f7 [x] _       = x   --Donde x representa el primer elemento, pero quien seria el primer elemento? la primer lista de caracteres, que basicamente seria la primer palabra/string
f7 (x : xs) 0  = aplanar (x:xs)
f7 (x : xs) n  = x ++ nBlancos n ++ f7 xs n


nBlancos :: Integer -> [Char]
nBlancos 1 = " "
nBlancos n = " " ++ nBlancos (n-1)
           
{-EJERCICIO 5.1-} 
--SumaAcumulada
        
sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada (x:xs) = x : sumadePosteriores x xs 


sumadePosteriores :: (Num t) => t -> [t] -> [t]
sumadePosteriores x [] = []
sumadePosteriores x (y:xs) = x + y : sumadePosteriores numAcumulado xs
        where 
        numAcumulado = (x + y)


{-EJERCICIO 5.2-} 
descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs)
         | x == 2            = [[2]] ++ descomponerEnPrimos xs 
descomponerEnPrimos (x : xs) = [[2] ++ segundoElementoPrimobis 1 x] ++ descomponerEnPrimos xs


--La idea es arrancar desde primo = 1
segundoElementoPrimo :: Integer -> Integer -> Integer
segundoElementoPrimo primo n | n == 3 = 3
                             | 2 * primo == n = primo
                             | otherwise = segundoElementoPrimo (primo + 1) n

segundoElementoPrimobis :: Integer -> Integer -> [Integer]
segundoElementoPrimobis primo n | n == 2 = [2]
                                | n == 3 = [3]
                                | 2 * primo == n = [primo]
                                | otherwise      = segundoElementoPrimobis (primo + 1) n





{--EJERCICIO 6--}

type Texto = [Char]
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]


--6.a correcto
enLoscontactos :: Nombre -> ContactosTel -> Bool
enLoscontactos _ [] = False 
enLoscontactos nombre (x:xs) 
                | nombre == fst x = True
                | otherwise       = enLoscontactos nombre xs 

--6.b
agregarContacto :: Contacto -> ContactosTel -> ContactosTel --ContactosTel es una lista de tuplas
agregarContacto (nombre, telefono) (x:xs)
                | enLoscontactos nombre (x:xs) = actualizaTelefono sinrepetidos (nombre, telefono)  
                | otherwise = [(nombre, telefono)] ++ (x:xs) 
        where
        sinrepetidos = eliminarRepetidoss (x:xs) (nombre,telefono)

            
--aux
actualizaTelefono :: ContactosTel -> Contacto -> ContactosTel
actualizaTelefono (x:xs) (elNombre, elNumero) 
                | enLoscontactos elNombre (x:xs) = [(elNombre, elNumero)] ++ (x:xs) 
                | otherwise                      = [(elNombre, elNumero)] ++ (x:xs)

--aux
eliminarRepetidoss :: ContactosTel -> Contacto -> ContactosTel 
eliminarRepetidoss [] _           = []
eliminarRepetidoss (x:xs) (nombre, telefono)
                | nombre == fst x = xs
                | otherwise       = x : eliminarRepetidoss xs (nombre, telefono) 

--6.c-- Pa ksa
eliminarContacto :: Nombre -> ContactosTel -> ContactosTel 
eliminarContacto _ []       = []
eliminarContacto nombre (x:xs)
                | nombre == fst x = xs
                | otherwise       = x : eliminarContacto nombre xs







{--EJERCICIO7--}

type Identificacion = Integer
type Ubicacion = Texto --Texto seria un String basicamente--
type Estado = (Disponibilidad, Ubicacion)
type Locker = (Identificacion, Estado)
type MapaDeLockers = [Locker]
type Disponibilidad = Bool    


--7.1 Existencia--
existeLocker :: Identificacion -> MapaDeLockers -> Bool
existeLocker _ [] = False
existeLocker numeroDeLocker (lockers : xs) 
                | numeroDeLocker == fst lockers = True
                | otherwise                     = existeLocker numeroDeLocker xs


--7.2 Ubicacion del locker--
ubicacionDelLocker :: Identificacion -> MapaDeLockers -> Ubicacion 
ubicacionDelLocker numeroDeLocker (x:xs)
                | existeLocker numeroDeLocker (x:xs) = posicionDelLocker numeroDeLocker (x:xs)                    ---que tiene que ser un string
                | otherwise                          = "No existe ubicación para ese locker"


--AUX Posición del locker
posicionDelLocker :: Identificacion -> MapaDeLockers -> Ubicacion --Ya que lo que llega a esta funcion auxiliar son identificadores de lockers que existen.
posicionDelLocker numeroDeLocker ((identificacion, (disponibilidad, ubicacion)): xs) 
                | numeroDeLocker == identificacion = ubicacion
                | otherwise                        = posicionDelLocker numeroDeLocker xs


--7.3 Disponibilidad del Locker--
estaDisponibleElLocker :: Identificacion -> MapaDeLockers -> Bool
estaDisponibleElLocker numeroDeLocker (x:xs)
                | existeLocker numeroDeLocker (x:xs) = disponibleLocker numeroDeLocker (x:xs)
                | otherwise                          = False


--AUX disponibilidad de lockers
disponibleLocker :: Identificacion -> MapaDeLockers -> Bool
disponibleLocker numeroDeLocker ((identificacion, (disponibilidad, ubicacion)): xs) 
                | numeroDeLocker == identificacion = disponibilidad
                | otherwise                        = disponibleLocker numeroDeLocker xs


--7.4 Ocupar Locker, basicamente la cambia el estado de disponibilidad
ocuparLocker :: Identificacion -> MapaDeLockers -> MapaDeLockers
ocuparLocker numeroDeLocker (x:xs)
                | existeLocker numeroDeLocker (x:xs) && estaDisponibleElLocker numeroDeLocker (x:xs) = cambiaDisponibilidad numeroDeLocker (x:xs)
                | otherwise                                                                          = (x:xs)

--AUX, recibe el identificador y la lista de lockers, y me devuelve la lista modificada
cambiaDisponibilidad :: Identificacion -> MapaDeLockers -> MapaDeLockers --AUX: En esta auxiliar ya esta laburando con lockers existentes y "disponibles"
cambiaDisponibilidad numeroDeLocker ((identificacion,(disponibilidad, ubicacion)) : xs)
                | numeroDeLocker == identificacion = ((numeroDeLocker, (False, ubicacion)) : xs ) --Basicamente estoy rescribiendo el estado de disponibilidad
                | otherwise                        = (identificacion, (disponibilidad, ubicacion)) : cambiaDisponibilidad numeroDeLocker xs

---
---

{-EJERCICIO 8 MATRICES EN HASKELL-}
--8.1 SUMA TOTAL

sumaTotal :: [[Integer]] -> Integer 
sumaTotal []     = 0
sumaTotal (f:fs) = sumaDeLaFila f + sumaTotal fs

sumaDeLaFila :: [Integer] -> Integer 
sumaDeLaFila [] = 0
sumaDeLaFila (x:xs) = x + sumaDeLaFila xs
--LO QUE HICE BASICAMENTE FUE SOMAR LOS ELEMENTOS DE LA PRIMER FILA, E IR RECORRIENDO RECURSIVAMENTE EL RESTO DE LAS FILAS CON UNA AUXILIAR


--8.2 CANTIDAD DE APARICIONES --

cantidadDeAparicionesMatrices :: Integer -> [[Integer]] -> Integer 
cantidadDeAparicionesMatrices e [] = 0
cantidadDeAparicionesMatrices e (f:fs) = cantidadDeVecesss e f + cantidadDeAparicionesMatrices e fs


cantidadDeVecesss :: Integer -> [Integer] -> Integer 
cantidadDeVecesss _ [] = 0
cantidadDeVecesss e (x:xs)
        | e == x    = 1 + cantidadDeVecesss e xs
        | otherwise = cantidadDeVecesss e xs


--8.3--CANTIDAD DE APARICIONES DE LAS PALABRAS;
contarPalabrasBis :: String ->  [[String]] -> Int
contarPalabrasBis _ [] = 0
contarPalabrasBis palabra (x:xs) = comparaPalabrasPorFilas palabra x + contarPalabrasBis palabra xs


--AUX RECORRE POR FILAS
comparaPalabrasPorFilas :: String -> [String] -> Int
comparaPalabrasPorFilas _ [] = 0
comparaPalabrasPorFilas palabra (x:xs) 
                | comparaPalabras palabra (primeraPalabraBiss (x:xs)) = 1 + comparaPalabrasPorFilas palabra xs
                | otherwise                                           = comparaPalabrasPorFilas palabra xs



--aux recibe 2 strings, y devuelve true si son iguales
comparaPalabras :: String -> String -> Bool
comparaPalabras [] [] = True
comparaPalabras [] _  = False
comparaPalabras _ []  = False
comparaPalabras (x:xs) (y:ys) 
                | x == y = comparaPalabras xs ys
                | otherwise = False

--aux recibe una lista de strings, y me devuelve la pri9mer palabra, es decir el primer string
primeraPalabraBiss :: [String] -> String 
primeraPalabraBiss [] = []
primeraPalabraBiss (x:xs)      
                | x /=" "  && x/="" = x --DONDE X REPRESENTA EL PRIMER STRING, ES DECIR LA PRIMER PALABRA, " "PARA GARANTIZAR NO AGARRAR UN ESPACIO Y "" PARA GARANTIZAR NO AGARRAR EL VACIO
                | otherwise = primeraPalabraBiss xs

--8.4--
cantidadDeApariciones2 :: (Eq t) => t -> [[t]] -> Integer 
cantidadDeApariciones2 t [] = 0
cantidadDeApariciones2 t (f:fs) = cantidadDeVecesss2 t f + cantidadDeApariciones2 t fs

cantidadDeVecesss2 ::(Eq t) => t -> [t] -> Integer 
cantidadDeVecesss2 _ [] = 0
cantidadDeVecesss2 t (x:xs)
        | t == x    = 1 + cantidadDeVecesss2 t xs
        | otherwise = cantidadDeVecesss2 t xs


--8.5--
--funco en 12 mins"
multiplicarPorEscalar :: Integer -> [[Integer]] -> [[Integer]]  
multiplicarPorEscalar _ [] = []
multiplicarPorEscalar lambda (f:fs) = [lambdaPorFila lambda f] ++ multiplicarPorEscalar lambda fs


lambdaPorFila  :: Integer ->  [Integer] -> [Integer]
lambdaPorFila _ [] = []
lambdaPorFila lambda (x:xs) = lambda * x : lambdaPorFila lambda xs