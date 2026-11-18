--stocks--
--LEN(RES) = CANTIDAD DE PRODUCTOS DISTINTOS Y RES[1] = CANTIDAD DE ESE PRODUCTO EN MI STOCK
--2puntitos atroden--
---1---
-------
generar_stock :: [String] -> [(String, Int)]
generar_stock [] = []
generar_stock (x:xs) = (x , fromInteger(cantidad_de_apariciones x (x:xs))) : generar_stock (elimina_productos x xs)  

cantidad_de_apariciones :: String -> [String] -> Integer
cantidad_de_apariciones _ [] = 0
cantidad_de_apariciones p (x:xs) 
                            | p == x    = 1 + cantidad_de_apariciones p xs
                            | otherwise = 0 + cantidad_de_apariciones p xs 

elimina_productos :: String -> [String] -> [String]
elimina_productos _ [] = []
elimina_productos p (x:xs) 
                    | p == x    = elimina_productos p xs
                    | otherwise = x : elimina_productos p xs 

---2---
-------
--debo devolver la cantidad de stock del producto en cuestion:
stock_de_producto :: [(String, Integer)] -> String -> Integer
stock_de_producto [] _ = 0
stock_de_producto ((producto,cantidad): xs) producto_buscado
                        | producto_buscado == producto = cantidad
                        | otherwise                    = stock_de_producto xs producto_buscado
--otra changa

---3----
--------
--modularizar 3
dinero_en_stock :: [(String, Integer)] -> [(String, Float)] -> Float
dinero_en_stock [] _ = 0
dinero_en_stock (x:xs) (y:ys) = valor_de_ese_producto_en_stock (x:xs) (y:ys) + dinero_en_stock xs (y:ys)


valor_de_ese_producto_en_stock :: [(String, Integer)] -> [(String, Float)] -> Float
valor_de_ese_producto_en_stock ((prodct_stock, cantidad_stock):xs) ((prodcto_lista, precio):ys)
                                    | prodct_stock == prodcto_lista = (fromInteger cantidad_stock) * precio
                                    | otherwise                     = valor_de_ese_producto_en_stock ((prodct_stock, cantidad_stock):xs) ys


---4---
-------
aplicar_oferta :: [(String, Integer)] -> [(String, Float)] -> [(String, Float)]
aplicar_oferta [] _ = []
aplicar_oferta ((product, cantidad):xs) ((nameproduct, precio):ys) 
                    | condicion_de_oferta (product, cantidad) ((nameproduct, precio):ys) = (product, (descuento (product,cantidad) ((nameproduct, precio):ys))) : aplicar_oferta xs ((nameproduct, precio):ys)
                    | otherwise                                                          = (product, precio) : aplicar_oferta xs ((nameproduct, precio):ys)

condicion_de_oferta :: (String, Integer) -> [(String, Float)] -> Bool
condicion_de_oferta _ [] = False 
condicion_de_oferta (producto, cantidad) ((nameProducto, precio):ys) 
                    | producto == nameProducto && cantidad > 10 = True
                    | producto /= nameProducto                  = condicion_de_oferta (producto, cantidad) ys
                    | otherwise                                 = False


descuento :: (String, Integer) -> [(String, Float)] -> Float
descuento _ [] = 0
descuento (producto, cantidad) ((nameProducto, precio):ys) 
                                            | producto == nameProducto  = precio * 0.80
                                            | otherwise                 = descuento (producto, cantidad) ys

