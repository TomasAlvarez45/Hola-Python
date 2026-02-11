### Strings ### 

mi_string = "Hola, soy un string"
mi_otro_string = 'Hola, soy otro string'

print(len(mi_string))
print(len(mi_otro_string))

print(mi_string + " " + mi_otro_string)

mi_nuevo_string_con_salto = """Hola, soy un string\ncon salto de linea"""
print(mi_nuevo_string_con_salto)

mi_nuevo_string_con_tabulacion = """\tHola, soy un string con tabulacion"""
print(mi_nuevo_string_con_tabulacion)

mi_string_escapado = """\\tHola, soy un string \\n escapado"""
print(mi_string_escapado)

###  Formateo ###

name = "Tomas"
last_name = "Alvarez"
age = 20

print("Mi nombre es {} {} y mi edad es {}".format(name, last_name, age)) 
print("Mi nombre es %s %s y mi edad es %d" % (name, last_name, age)) 
print(f"Mi nombre es {name} {last_name} y mi edad es {age}") 

### Desempaquetado de Caracteres ###

languaje = "python"
a, b, c, d, e, f = languaje
print(a)
print(f)

### Division ###

languaje_slice = languaje[1:3]
print(languaje_slice)

languaje_slice = languaje[1:]
print(languaje_slice)

languaje_slice = languaje[-2]

languaje_slice = languaje[0:6:2]
print(languaje_slice)

### Reverse ###

languaje_reverse = languaje[::-1]
print(languaje_reverse)

### Funciones de los Strings ###

print(languaje.capitalize())
print(languaje.upper())
print(languaje.count("t"))
print(languaje.isnumeric())
print("1".isnumeric())
print(languaje.lower())
print(languaje.lower().isupper())
print(languaje.startswith("py"))
