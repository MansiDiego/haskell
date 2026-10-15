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

##TUPLAS:
#SU SIGNATURA SE DEFINE DE LA SIGUIENTE MANERA; "tupla_random: tuple[tipo de dato, tipo de dato]" para seleccionar un elemento de la tupla lo mas practico es renombrar las posiciones de la tupla de la siguiente forma:
# peso, nombre = tupla_random (entonces lo que hicimos ahí fue decirle a la tupla, okey el primer tipo de dato de la tupla es peso, y el segundo es nombre, entonces cuando use sus nombres voy a hacer referencia a esos valores almacenados en esas posiciones)




#Capitulo 4;
#encapsulación: es basicamente envolver codigo en una funcion, para luego usar ese bloque de codigo llamando solamente a la funcion.
#refactorización; es cuando tenes un bloque de codigo que se repite, entonces lo refactorizamos en una sola funcion para no repetir codigo.
#docstring: basicamente explican la signatura(o en python llamado interfaz) de la funcion al inicio, y el comportamiento de dicha funcion sin entrar en detalles... por ejemplo: 
# 
# """ recibe una lista de frutas y devuelve true si es que la fruta pasada por argumento pertenece a la lista de frutas.     #              s: una lista que contiene frutas, e: un str que es una fruta"""

#precondiciones y postcondiciones(es como un contrato):
#Las precondiciones son responsabilidad de quien llama. Si quien llama viola una precondición y la función no funciona correctamente, el bug está en quien llama, no en la función.

#Si las precondiciones se satisfacen y las postcondiciones no, el bug está en la función. Si tus precondiciones y postcondiciones están claras, pueden ayudar con la depuración.




#Capitulo 5;
#observación de la operación modulo, puede hacer aritmetica de reloj, por ejemplo;
#start = 11 (11 am)
#duracion = 3(3 horas)
#fin_evento = (start + duracion) % 12 (el resto de sumar el inicio mas la duracion dividido 12, es equivalente a la hroa final )
inicio = 11 #expresamos el horario por convención 11 am y 12pm
duracion = 3 #expresamos en horas
final = (inicio + duracion) % 12
print(final)
#observacion al usar casting de tipos, recordar que cuando usamos la funcion input, para pedirle al usuario que escriba algo de modo tal que luego nosotros lo modifiquemos, la fun input() es un str => deberiamos castearla int(input()) ahora el str ingresado es un numero, pero si lo que ingresa el usuario no es un int, va a arrojar un error en el momento de su ejecución.


#cap6