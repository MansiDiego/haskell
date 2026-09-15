--OPERACIONES CON LISTAS--
--head :: [a] Devuelve el primer elemento de una lista
--tail :: [a] Devuelve la lista sin el primer elemento
-- (:) :: a -> [a] Une listas, el lado izquiero debe ser un elemento y el derecho una lista 

--OBSERVACIÓN DE "DIV" vs "/", div labura solo con cocientes enteros, y el "/" labura con cocientes reales

--fromInteger → específicamente desde Integer.
--fromIntegral → desde cualquier tipo entero (Int, Integer, etc.).
--EJEMPLO DE USO, UN F(X) QUE RECIBE COMO PARAMETROS DE ENTRADA DOS INTEGER Y QUEREMOS CALCULAR LA DIVISION EXACTA ==>
--fromIntegral a / fromIntegral b (NOTAR QUE ACA SE PODRIA HABER USADO TAMBIEN fromInteger)