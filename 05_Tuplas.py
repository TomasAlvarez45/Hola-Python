### Tuplas ###

mi_tupla = tuple((35, 24, 62, 52, 12))
mi_otra_tupla = (20, 1.90, "Tomas", "Alvarez")

print(mi_tupla)
print(type(mi_tupla))

print(mi_tupla[2])
print(mi_tupla[-1])

print(mi_tupla.count(24))
print(mi_tupla.index(52))

mi_suma_de_tuplas = mi_tupla + mi_otra_tupla
print(mi_suma_de_tuplas)

print(mi_suma_de_tuplas[3:6])

### Como editar una tupla ###

mi_tupla = list(mi_tupla) 
print(type(mi_tupla))

mi_tupla[3] = 65
mi_tupla.insert(2, 21)
mi_tupla = tuple(mi_tupla)
print(mi_tupla)
print(type(mi_tupla))

###Borrar tupla ###

#del mi_tupla
#print(mi_tupla) NameError: name 'mi_tupla' is not defined


### Las tuplas son inmutables, no se pueden modificar sus elementos ###

#mi_tupla[1] = 180 TypeError: 'tuple' object does not support item assignment
#print(mi_tupla)

