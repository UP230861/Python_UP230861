
# Exercises: Level 1

# Declarar una variable de primer nombre y asignar un valor
name = input("¿Cuál es tu nombre?: ")

# Declarar una variable de apellido y asignar un valor
las_name = input("¿Cuál es tu apellido?: ")

# Declarar una variable de nombre completo y asignar un valor
complete_name = input("Escribe tu nombre completo: ")

# Declarar una variable de país y asignar un valor
country = input("¿Cuál es tu país?: ")

# Declarar una variable de ciudad y asignar un valor
city = input("¿Cuál es tu ciudad?: ")

# Declarar una variable de edad y asignar un valor
age = input("Escribe tu edad: ")

# Declarar una variable is_married y asignar un valor
is_married = input("¿Estás casado?: ")

# Verificación de estado civil con condicionales
if is_married == "si":
    print("Estás casado")
elif is_married == "no":
    print("Qué solo estás")

# Imprimir todos los datos en una lista

lista = [["tu nombre es",name],[ "tu apeido es:",las_name],
[ "tu nombre completo:",complete_name], ["tu pais",country],
["tu ciudad:",city],["tu edad es",age],[" estas casado:",is_married]]
print(lista)

# Declarar una variable is_true y asignar un valor
is_true = True

# Declarar una variable is_light_on y asignar un valor
is_light_on = False

# Declarar múltiples variables en una línea
a, b, c = 1, 2, 3


# Exercises: Level 2

# Verificar el tipo de dato de todas tus variables
print(type(name))
print(type(las_name))
print(type(complete_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_married))

# Usar len() para encontrar la longitud del primer nombre
print(len(name))

# Comparar la longitud del primer nombre y el apellido
if len(name) > len(las_name):
    print("Tu nombre es más largo que tu apellido")
elif len(name) < len(las_name):
    print("Tu apellido es más largo que tu nombre")
else:
    print("Tu nombre y apellido tienen la misma longitud")

# Declarar 5 como num_one y 4 como num_two
num1 = 5
num2 = 4

# Sumar num_one y num_two y asignar el valor a la variable total
sum = num1 + num2

# Restar num_two de num_one y asignar el valor a la variable diff
resta = num1 - num2

# Multiplicar num_two y num_one y asignar a product
mult = num1 * num2

# Dividir num_one por num_two y asignar a division
division = num1 / num2

# Usar módulo para encontrar el resto y asignarlo a remainder
remainder = num1 % num2

# Calcular la potencia de num_one a num_two y asignarlo a exp
exp = num1 ** num2

# Calcular la división entera de num_one entre num_two y asignarlo a floor_division
floor_division = num1 // num2

# Imprimir los resultados
print("Total:", sum)
print("Diferencia:", resta)
print("Producto:", mult)
print("División:", division)
print("Resto:", remainder)
print("Potencia:", exp)
print("División entera:", floor_division)

# El radio de un círculo es 30 metros
rad = 30
pi = 3.14

# Calcular el área del círculo
area_circle = pi * rad ** 2

# Calcular la circunferencia del círculo
circum_of_circle = 2 * pi * rad

# Imprimir área y circunferencia
print("Área del círculo:", area_circle)
print("Circunferencia del círculo:", circum_of_circle)

# Tomar el radio como entrada del usuario y calcular el área
radius_user = float(input("Ingrese el radio: "))
area_user = pi * radius_user ** 2
print("El área del círculo con el radio ingresado es:", area_user)

# Usar input() para obtener nombre, apellido, país y edad del usuario
first_name = input("Ingrese su nombre: ")
last_name = input("Ingrese su apellido: ")
country_user = input("Ingrese su país: ")
age_user = input("Ingrese su edad: ")

# Imprimir los valores
print("Nombre:", first_name)
print("Apellido:", last_name)
print("País:", country_user)
print("Edad:", age_user)



