### Classes ###

class Person:
    pass 

print(Person)
print(Person())

class Eduardo:
    def __init__(self):
        self.name = "Eduardo"
        self.surname = "Lopez"
    
mi_persona = Eduardo()

print(f"{mi_persona.name} {mi_persona.surname}")

class Fernando:
    def __init__(self, name, surname, alias = "Sin Alias Conocido"):
        self.full_name = f"{name} {surname} ({alias})" #propiedad publica
        self.__name = name #Propiedad privada

    def get_name (self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} esta caminando")
    
Persona_Fernando = Fernando("Fernando", "Nisme")



print(Persona_Fernando.full_name)

Persona_Fernando.walk()

mi_otra_persona = Fernando("Joaquin", "Lopez", "el flaco")

print (Persona_Fernando.get_name())

print(mi_otra_persona.full_name)
mi_otra_persona.walk()
mi_otra_persona.full_name = "Arnalo gomez (El Clavadista)"
