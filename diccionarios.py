#son pares claves valor, que estan ordenados basicamente
#por ejemplo;
auto = {
    "marca" : "ford",
    "modelo" : "2012, 10 puntos",
    "año"    : "2010 de fabrica"
}
print(auto["marca"])
print(len(auto)) #me devuelve 3, ya que el diccionario auto tiene 3 elemeentos, es decir cada elemento es un par clave valor
print(type(auto))



#VALORES:#
###los valores de un diccionario pueden ser de cualquier tipo de datos, es decir podemos tener una tupla como valor, o tener una lista como valor, por ejemplo
# auto ={
#   "marca" : ["ford", "toyota", "chevrolette"],
#   "modelo" : ["coupe", "camioneta", "descapotable"] 
#  }   

##TIPO DE DATO DICCIONARIO(tipo de dato y clase son lo mismo, definen el conjunto de operaciones que definen al tipo de dato en cuestion)##; Se definie como tipo de dato "dict"



#El constructuro dict()
#sirve basicamente para asignarle a una variable un diccionario, por ejemplo;
#paises = dict("pais1": "argentina", "pais2":"peru", "pais3":"bolivia")


##ACCEDER A ELEMENTOS##
#x = nombre_del_diccionario["clave"] y esto me asignaria en x el valor de la clave de dicho diccionario

##ACCEDER AL ELEMENTO USANDO GET Y LA CLAVE
x = auto.get("marca")
print(x) #me imprime la marca(por mas de que se llama get como el metodo que usamos con pilas y las colas, no me elimina el elemento que esta almacenado en esa clave)


#EL CONSTRUCTOR, Basicamente es la forma de instanciar al objeto de dicha clase, en python los constructores se forma de la siguiente manera; nombre_de_clase() es decir nombre de la clase/tipo seguido de un parentesis


#OBTENER CLAVES
#x = nombre_del_diccionario.keys()



##agregar elementos al diccionario;
#nombre_del_diccionario["clave"] = "valor"


