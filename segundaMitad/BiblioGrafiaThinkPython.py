#TIPS PARA EL INTERPRETE, COMO EN HASKELL USABAMOS EL COMPILADOR"GHCI" EN PYTHON USAMOS EL INTERPRETE, PARA PROBAR COSAS POR CONSOLA TIRAMOS PY O PYTHON Y AHI PROBAMOS RAPIDAMENTE COSAS
#TIPADO PARA LA SIGNATURA;

# Tipos básicos más comunes en Python:
# int: enteros.                                                  EJ; def suma (x:int) -> int:...
# float: números con coma / reales ($\mathbb{R}$).               EJ; def raizdex(x:int) -> float....
# str: cadenas de texto.                                         EJ; def cancnio(letra: str) -> str...                                    
# bool: booleanos (True / False).                                EJ; def esverdadque (x:str) -> bool
# None: cuando la función es un procedimiento y no tiene return. EJ; def imprimir_hola_mundo() -> None:


#OPERACIONES ARITMETICAS;
# "/" => puede trabajar con enteros y con floats, pero el resultado siempre es un float, importante "la salida siempre es un float" ej; 10/2 = 5.0
# "*" => multiplicador, labura como siempre, pero ademas tambien multiplica datos del tipo "str", es decir "mateo" * 3 = "mateo mateo mateo"
# "or" => Basicamente seria un p v q, si una de las 2 proposiciones es true devuelve true, si ambas proposiciones son falsas devuelve false.
# "and" => basicamente me indica si ambas proposiciones son true, es decir (p ^ q) seria.
# "len" => me devuelve la longitud del str que le pase por argumento, por ejemplo: len("mateo") = 5

#OPERACIONES DADAS POR EL MODULO(O LIBRERIA)math
#funcion aportada por el modulo math; "ceil" me redondea un float para arriba, por ejemplo math.ceil(2.1) =3
#funcion aportada por el modulo math; "round" redondea los decimales que uno quiere, por ejemplo round(x, 3) => si x=2.8989 => 2.899
#funcion aportada por el modulo math; "sqrt" me devuelve la raiz cuadrada del valor que le pase por argumento, por ejemplo: math.sqrt(9) = 3.0 #obs: devuelve un float
#funcion aportada por el modulo math; "floor" redondea para abajo, recibe un valor y redondea a un entero pero "al izquierdo en la recta numerica" ej; math.floor(3.5) = 3 obs; math.floor(-3.5) = -4

