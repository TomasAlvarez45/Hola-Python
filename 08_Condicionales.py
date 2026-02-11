 ### Condicionales ###

mi_condicion = False

if mi_condicion:
    print("La condición es verdadera")

mi_condicion = 57

if mi_condicion == 10:
    print("Es Igual a 10")
elif mi_condicion > 10 and mi_condicion < 20:
    print("Esta entre 10 y 20")
elif mi_condicion > 20:
    print("Es mayor a 20")
elif mi_condicion == 0:
    print("Es igual a 0")
else:
    print("Es menor a 10")

print("Fin del programa")

### Chequear si un string tiene contenido ###

mi_string = ""

if mi_string:
    print("El string tiene contenido")
else:
    print("El string está vacío")

### negacion de una condicion ###

mi_condicion = True

if not mi_condicion:
    print("La condición es falsa")
else:
    print("La condición es verdadera")