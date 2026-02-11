### Loops ###

### While Loop ###

mi_condicion = 0

while mi_condicion < 10:
    print(mi_condicion)
    mi_condicion += 1
else: # Este else es opcional
    print("La condición es mayor o igual a 10")
    
print("Fin del programa")

while mi_condicion < 20:
    mi_condicion += 1
    print("Mi condicion es menor que 20")
    if mi_condicion == 15:
        print("Se llegó al valor 15, se salta esa iteración")
        continue # Salta a la siguiente iteración del loop
        #break hubiera concluido el loop
    print(mi_condicion)


### For Loop ###

mi_lista = [1, 2, 3, 4, 5]
mi_set = {10, 20, 30, 40, 50}
mi_tupla = (100, 200, 300, 400, 500)
mi_diccionario = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}


for elemento in mi_lista:
    print(elemento)
for elemento in mi_set:
    print(elemento)
    if elemento == 20:
        print("Se llegó al valor 30, se salta esa iteración")
        continue  # Salta a la siguiente iteración del loop
for elemento in mi_tupla:
    print(elemento)
    if elemento == 300:
        print("Se llegó al valor 300, se sale del loop")
        break  # Sale del loop cuando el elemento es 300
for elemento in mi_diccionario:
    print(elemento)  # Imprime las claves del diccionario
else:
    print("Se terminaron los elementos de la colección")