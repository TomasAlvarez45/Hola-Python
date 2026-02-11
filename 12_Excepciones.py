### Exception Handling ### 

number_one, number_two = 5, 1
number_two = "1"

### try except ###

try:
    print(number_one + number_two)
    print("La operacion se ha realizado exitosamente")
except:
    #Se ejecuta si se produce una excepcion
    print("Se ha producido un error")


### try except else ###

try:
    print(number_one + number_two)
    print("La operacion se ha realizado exitosamente")
except:
    #Se ejecuta si se produce una excepcion
    print("Se ha producido un error")
else:#Opcional
    #Se ejecuta si no se produce una excepcion
    print("La ejecucion continua correctamente")

### try except else finally ###

try:
    print(number_one + number_two)
    print("La operacion se ha realizado exitosamente")
except:
    #Se ejecuta si se produce una excepcion
    print("Se ha producido un error")
else:#Opcional
    #Se ejecuta si no se produce una excepcion
    print("La ejecucion continua correctamente")
finally:#Opcional
    #Se ejecuta siempre
    print("La ejecucion continua")

### Captura de excepciones por tipo ###

try:
    print(number_one + number_two)
    print("La operacion se ha realizado exitosamente")
except TypeError:
    #Se ejecuta si se produce una excepcion
    print("Se ha producido un error")
except ValueError:
    #Se ejecuta si se produce una excepcion
    print("Se ha producido un error")


### Captura de la informacion de la excepcion ###

try:
    print(number_one + number_two)
    print("La operacion se ha realizado exitosamente")
except ValueError as error:
    #Se ejecuta si se produce una excepcion
    print("Se ha producido un error")
    print(error)
except Exception as error:
    print("Se ha producido un error")
    print(error)


