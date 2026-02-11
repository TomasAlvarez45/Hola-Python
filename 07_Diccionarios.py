### Diccionarios ###

mi_diccionario = dict()
mi_otro_diccionario = {}

print(type(mi_diccionario))
print(type(mi_otro_diccionario))

mi_otro_diccionario = {"nombre": "Tomas", "edad": 20, "ciudad": "C.A.B.A.", 1:"Swift"}#Clave:Valor
print(mi_otro_diccionario)
print(mi_otro_diccionario["nombre"])#Acceder a un valor por su clave
print(mi_otro_diccionario[1])#Acceder a un valor por su clave numérica

mi_diccionario = {
    "Nombre": "Tomas",
    "Apellido": "Alvarez",
    "Edad": 20,
    "Lenguajes": {"Python", "Java", "C++"},
    1:100
}

print(mi_diccionario)

print(len(mi_otro_diccionario)) #Cantidad de elementos en el diccionario
print(len(mi_diccionario)) #Cantidad de elementos en el diccionario

print (mi_diccionario["Lenguajes"])

mi_diccionario["Edad"] = 21 #Modificar un valor
print(mi_diccionario["Edad"])

mi_diccionario["Ciudad"] = "C.A.B.A." #Agregar un nuevo par clave:valor
print(mi_diccionario)

del mi_diccionario["Ciudad"] #Eliminar un par clave:valor
print(mi_diccionario)

print("Nombre" in mi_diccionario) #True ya que "Nombre" es una clave del diccionario
print("Tomas" in mi_diccionario)   #False ya que "Tomas" no es una clave del diccionario, sino un valor
print(1 in mi_diccionario)         #True ya que 1 es una clave del diccionario


print(mi_diccionario.items())
print(mi_diccionario.keys())
print(mi_diccionario.values())

mi_nuevo_diccionario = dict.fromkeys(("Nombre", "Apellido", "Edad"))
print(mi_nuevo_diccionario)

### Crear un diccionario a partir de una lista ###

mi_lista = ["Nombre", "Apellido", "Edad"]
mi_nuevo_diccionario = dict.fromkeys(mi_lista)
print(mi_nuevo_diccionario)

### crear un diccionario a partir de otro diccionario ###

mi_nuevo_diccionario = dict.fromkeys(mi_diccionario)
print(mi_nuevo_diccionario)

### Crear un diccionario con un diccionario y un valor por defecto ###
mi_nuevo_diccionario = dict.fromkeys(mi_diccionario, "Valor por defecto")
print(mi_nuevo_diccionario)

### Convertir las claves de un diccionario en una lista ###
print(list(mi_diccionario)) 

### Convertir los valores de un diccionario en una lista ###
print(list(mi_diccionario.values()))
