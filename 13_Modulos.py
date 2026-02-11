### Modulos ###

### Modulos creados localmente ###

#El nombre del fichero a importar no puede empezar por un numero

import module #Importamos un modulo
from module import sum_two_values #Importamos la funcion concreta a utilizar

module.suma_aleatoria(2, 5) #Para acceder a la funcion es necesario citar al modulo
sum_two_values(10, 15) #Al importar la funcion concreta no es necesario citar al modulo


### Modulos creados externamente ###
import math
print(math.tan(123))
print(math.pow(2, 8))

import random

print(random.randint(1, 10))