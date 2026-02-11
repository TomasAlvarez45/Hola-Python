'''Operadores en python'''
### Operadores Aritmeticos ###
print(3 + 2) #suma
print(3 - 2) #resta
print(3 * 2) #multiplicacion
print(3 / 2) #division
print(3 ** 2) #potencia
print(9 // 2) #division entera
print(3 % 2) #modulo (resto de la division)
print(3 * 2 + 5 - 4 // 2) #orden de operaciones

### Operadores de Comparacion ###
print(3 > 2) #mayor que
print(3 < 2) #menor que
print(3 >= 2) #mayor o igual que
print(3 <= 2) #menor o igual que
print(3 == 2) #igual que
print(3 != 2) #distinto que



### Operaciones con Texto ###
print("hola " + "mundo") #concatenacion de cadenas de texto
print("hola " * 3) #repeticion de cadenas de texto
print("hola " * (3 * 2 + 5 - 4 // 2)) #repeticion con orden de operaciones
print("hola " + str(3)) #concatenacion de cadena de texto y numero (se debe convertir el numero a cadena)

mi_float = 2.5 * 2
print("hola " * int(mi_float)) #repeticion de cadena de texto con un float convertido a entero


### Operaciones Comparativas con Texto ###
# Las operaciones comparativas con texto se basan en el orden alfabetico (ASCII)
print("hola" > "mundo") 
print("hola" < "mundo") 
print("hola" >= "mundo") 
print("hola" <= "mundo") 
print("hola" == "mundo")
print("hola" != "mundo")

# Comparacion de longitudes de cadenas de texto
print(len("hola") > len("mundo"))


### Operadores Logicos ###

print(3 > 4 and "hola" > "mundo")
print(3 > 4 or "hola" > "mundo")
print(3 < 4 and "hola" < "mundo")
print(3 < 4 or "hola" > "mundo")
print(not(3 > 4))