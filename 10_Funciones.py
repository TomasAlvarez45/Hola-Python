### Funciones ###

def mi_funcion ():
    print("Esto es una funcion")


mi_funcion ()

### Funcion sin retorno ###

def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(5.3, 7.2)

### Funciones con retorno ###

def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value

my_result = sum_two_values_with_return(10, 5)

print(my_result)


def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values_with_return(10, 5)

print(my_result)


def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname = "Alvarez", name = "Tomas")

def print_name_with_default (name, surname, alias = "Sin Alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Tomas", "Alvarez")

def print_texts(*texts):
    for text in texts:
        print(text)

print_texts("hola", "que tal", "python")

def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())

print_upper_texts("hola", "que tal", "python")