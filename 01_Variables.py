'''Variables en Python'''

mi_variable = "Mi Variable String"
print (mi_variable)

mi_variable_int = 16
print (mi_variable_int)

mi_variable_bool = True
print (mi_variable_bool)

#transformar una variable de un tipo a string
mi_int_a_str = str(mi_variable_int)
print (mi_int_a_str)
print (type(mi_int_a_str))

#concatenacion de variables en un print
print(mi_variable, mi_variable_int, 'es', mi_variable_bool)

'''Algunas funciones del sistema'''
print(len(mi_variable))  #funcion len() para obtener la longitud de una cadena de texto

'''Variables en una sola linea'''
#ojo con usar esta sintaxis en exceso, puede dificultar la lectura del codigo
name, surname, alias, age = "Tomas", "Alvarez", "Rompo", 20
print (age, name, surname, alias)
print ("Mi nombre es", name, surname, ", pero me dicen", alias, "y tengo", age, " ños.")

'''Inputs'''
#name = input("Ingrese su nombre: ")
#age = input("Ingrese su edad: ")

print ("Hola", name, ", tienes", age, "años.")

'''Forzar tipo de dato en una variable (no se puede)'''
address: str = "Mi direccion"
address = 31
print (address)#no mantuvo el tipo de dato forzado