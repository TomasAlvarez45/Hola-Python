### Sets ###

mi_set = set()
mi_otro_set = {}

print(type(mi_set))
print(type(mi_otro_set)) #Indica que es un diccionario

mi_otro_set = {"manzana", "banana", "cereza"}

print(type(mi_otro_set)) #Ahora es un set

print(len(mi_otro_set))
#print(mi_otro_set[1]) TypeError: 'set' object is not subscriptable

### Agregar elementos a un set ###
mi_otro_set.add("naranja")
print(mi_otro_set) #Un set no tiene un orden definido

mi_otro_set.add("naranja")
print(mi_otro_set) #Los sets no permiten elementos duplicados


### Como comprobar si un elemento esta en un set ###
print("banana" in mi_otro_set) #True
print("kiwi" in mi_otro_set)   #False

### Eliminar elementos de un set ###
mi_otro_set.remove("banana")
print(mi_otro_set)

### Agregar varios elementos a un set ###
mi_otro_set.update(["pera", "mango", "uva"])
print(mi_otro_set)

### Limpiar un set ###
mi_otro_set.clear()
print(mi_otro_set)

### Convertir un set a una lista ###
#No se puede conocer el orden en que se va a generar la lista
mi_set = {"manzana", "banana", "cereza"}
mi_lista = list(mi_set)
print(mi_lista)
print(mi_lista[0]) #Ahora si se puede acceder por indice

### Unir dos sets ###
mi_otro_set = {"Python", "Java", "C++"}
mi_nuevo_set = mi_set.union(mi_otro_set)
print(mi_nuevo_set)
print(mi_nuevo_set.union(mi_set)) #No se repiten elementos
print(mi_nuevo_set.union({"Ruby", "JavaScript", "Go"}))


### Diferencia entre dos sets ###
print(mi_nuevo_set.difference(mi_set)) #Elementos que estan en mi_nuevo_set pero no en mi_set
print(mi_nuevo_set.difference(mi_otro_set)) #Elementos que estan en mi_nuevo_set pero no en mi_otro_set


### Eliminar un set ###
del mi_otro_set
#print(mi_otro_set) NameError: name 'mi_otro_set' is not defined