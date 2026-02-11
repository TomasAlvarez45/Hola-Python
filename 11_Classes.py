### Classes ###

class Person:
    pass 

print(Person)
print(Person())

class Epstein:
    def __init__(self):
        self.name = "Jeffrey"
        self.surname = "Epstein"
    
mi_persona = Epstein()

print(f"{mi_persona.name} {mi_persona.surname}")

class Diddy:
    def __init__(self, name, surname, alias = "Sin Alias Conocido"):
        self.full_name = f"{name} {surname} ({alias})" #propiedad publica
        self.__name = name #Propiedad privada

    def get_name (self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} esta caminando")
    
nice_try_diddy = Diddy("P", "Diddy")



print(nice_try_diddy.full_name)

nice_try_diddy.walk()

mi_otra_persona = Diddy("Justin", "Bieber", "Elgay")

print (nice_try_diddy.get_name())

print(mi_otra_persona.full_name)
mi_otra_persona.walk()
mi_otra_persona.full_name = "Juan domingo peron (el Violador)"

