### Listas ###

mi_lista = list()
mi_otra_lista = []

print(len(mi_lista))

mi_lista = [35, 24, 62, 52, 12]
print(len(mi_lista))

mi_otra_lista = [20, 1.90, "Tomas", "Alvarez"]
print(mi_otra_lista)

print(mi_otra_lista[2])
print(mi_otra_lista.count("Tomas"))

age, height, name, last_name = mi_otra_lista
print(age)

print (mi_lista + mi_otra_lista)

mi_lista.append(15)
print(mi_lista)

mi_lista.insert(3, 24)
print(mi_lista)

mi_lista[1] = 25
print(mi_lista)

mi_lista.remove(24)
print(mi_lista)

del mi_lista[2]
print(mi_lista)

print(mi_lista.pop(2))
mi_elemento_pop = mi_lista.pop(2)
print(mi_elemento_pop)

mi_lista_copy = mi_lista.copy()


mi_lista.clear()
print(mi_lista)
print(mi_lista_copy)

mi_lista_copy.reverse()
print(mi_lista_copy)

mi_lista_copy.sort()
print(mi_lista_copy)

print(mi_lista_copy[0:2])


### Tipado dinamico ###
mi_lista = "Hola python"
print(type(mi_lista))