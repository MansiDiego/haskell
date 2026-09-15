--Consideraciones para laburar con Listas--
--Operaciones--
-- ==========================================================
-- 1. LONGITUD: Caso base vacío y conteo recursivo
-- ==========================================================
-- Si la lista está vacía, mide 0.
-- Si tiene la forma (x:xs), ignoramos x con _ y sumamos 1 al resto.

longitud :: [t] -> Integer
longitud []     = 0
longitud (_:xs) = 1 + longitud xs

-- Pruebas en terminal:
-- longitud []        --> 0
-- longitud [1, 2, 3] --> 3

{-POR EJEMPLO:-}

longitud :: [Integer] -> Integer 
longitud [] {-ACA ESTOY DICIENDO SI LA LISTA ES VACIA ENTONCES... (ESTOY USANDO PATTERN MATCHING)-} = 0
longitud (_ :xs) = 1 + longitud xs 













-- ==========================================================
-- 2. SUMATORIA: Operar sobre cada elemento
-- ==========================================================
-- Acumula sumando la cabeza 'x' con el llamado recursivo sobre la cola 'xs'.

sumatoria :: [Integer] -> Integer
sumatoria []     = 0
sumatoria (x:xs) = x + sumatoria xs

-- Pruebas:
-- sumatoria [1, 2, 3, 4] --> 10


-- ==========================================================
-- 3. PERTENECE: Recursión con Guardas (reemplazo de if-then-else)
-- ==========================================================
-- En una lista vacía ningún elemento pertenece (False).
-- Con elementos, comparamos si la cabeza 'x' es igual a 'e'.
-- Si no, seguimos buscando en la cola 'xs'.

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x:xs)
    | e == x    = True
    | otherwise = pertenece e xs

-- Pruebas:
-- pertenece 3 [1, 2, 3] --> True
-- pertenece 5 [1, 2, 3] --> False


-- ==========================================================
-- 4. FILTRAR PARES: Construir una nueva lista usando cons (:)
-- ==========================================================
-- Usa 'mod' permitido. Si es par, lo agregamos con ':' al resultado recursivo;
-- si es impar, lo descartamos y continuamos con la cola.

soloPares :: [Integer] -> [Integer]
soloPares [] = []
soloPares (x:xs)
    | mod x 2 == 0 = x : soloPares xs
    | otherwise    = soloPares xs

-- Pruebas:
-- soloPares [1, 2, 3, 4, 5, 6] --> [2, 4, 6]


-- ==========================================================
-- 5. REVERSO: Usando concatenación (++)
-- ==========================================================
-- Da vuelta la lista pegando la cabeza al final de la cola ya invertida.
-- Notá que [x] equivale a (x:[]).

reverso :: [t] -> [t]
reverso []     = []
reverso (x:xs) = reverso xs ++ [x]

-- Pruebas:
-- reverso [1, 2, 3] --> [3, 2, 1]


-- ==========================================================
-- 6. ÚLTIMO: Desestructurar listas con al menos un elemento
-- ==========================================================
-- Cuando queda un solo elemento [x], ese es el último.
-- Si hay más (_:xs), descartamos el primero y seguimos.

ultimo :: [t] -> t
ultimo [x]    = x
ultimo (_:xs) = ultimo xs

-- Pruebas:
-- ultimo [10, 20, 30] --> 30