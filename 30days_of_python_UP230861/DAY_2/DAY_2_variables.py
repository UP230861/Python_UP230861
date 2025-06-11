
name= input("cual es tu nombre:")
las_name=input("cual es tu apeido:")
complete_name=input("escribe tu nombre completo:")
country= input("cual es tu pais:")
city=input("cual es tu ciudad:")
age=input("escribe tu edad:")
is_married=input("estas casado?")

if is_married == "si":
    print("estas cadado")
elif is_married == "no":
    print("que solo estas")
lista = [["tu nombre es",name],[ "tu apeido es:",las_name],
[ "tu nombre completo:",complete_name], ["tu pais",country],
["tu ciudad:",city],["tu edad es",age],[" estas casado:",is_married]]
print(lista)

is_true = True
is_light_on = False
a, b, c = 1, 2, 3
# Level 2 exercises

print(type(name))
print(type(las_name))
print(type(complete_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_married))

print(len(name))

if len(name) > len(las_name):
    print("tu nombre es más largo que tu apellido")
elif len(name) < len(las_name):
    print("tu apellido es más largo que tu nombre")
else:
    print("tu nombre y apellido tienen la misma longitud")

num1 = 5
num2 = 4

sum = num1 + num2
resta = num1 - num2
mult = num1 * num2
division = num1 / num2
remainder = num1 % num2
exp = num1 ** num2
floor_division = num1 // num2

print("total:", sum)
print("diferencia:", resta)
print("producto:", mult)
print("division:", division)
print("resto:", remainder)
print("potencia:", exp)
print("division entera:", floor_division)

rad = 30
pi = 3.14
area_circle = pi * rad ** 2
circum_of_circle = 2 * pi * rad

print("area del circulo:", area_circle)
print("circunferencia del circulo:", circum_of_circle)

radius_user = float(input("Ingrese el radio: "))
area_user = pi * radius_user ** 2
print("El area del circulo con radio ingresado es:", area_user)

first_name = input("Ingrese su nombre: ")
last_name = input("Ingrese su apellido: ")
country_user = input("Ingrese su pais: ")
age_user = input("Ingrese su edad: ")

print("Nombre:", first_name)
print("Apellido:", last_name)
print("Pais:", country_user)
print("Edad:", age_user)

