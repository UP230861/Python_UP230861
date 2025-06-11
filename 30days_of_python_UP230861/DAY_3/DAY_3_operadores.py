
#dia 3
numeroedad=input("cuales tu edad?")
higth=input(float("cuales tu altura?"))
print('coloca valores de base y altura de un triangulo')
base=input(float("cuales la base"))
altura=input(float("cuales la altura"))
area_total=(0.5*base*altura)
print('el area total es de:',area_total)
print('coloca valores de los lados de un triangulo')
a=input(float("valor de a:"))
b=input(float("valor de b:"))
c=input(float("valor de c:"))
perimetro_total=(a+b+c)
print('el perimetro es de:',perimetro_total)
#Calcula su área (área = largo x ancho) y perímetro (perímetro = 2 x (largo + ancho)).
print('coloca valores de los lados de un recutangulo')
largo=input(float("largo"))
ancho=input(float("ancho"))
area_rectangulo=(largo*ancho)
print('el area es de:',area_rectangulo)
perimetro_rectangulo=(2*(largo+ancho))
print('el perimetro es de:',perimetro_rectangulo)

#Calcula el radio de un círculo usando las instrucciones. Calcula el área (área = pi x r x r) y la circunferencia (c = 2 x pi x r) donde pi = 3,14.
print('coloca valores de los lados de un circulo')
r=input(float("radio"))
pi=3.14
area_circulo=(pi(r*r))
cir=(2(pi*r))
print('el perimetro es de:',cir)
#Calcula la pendiente, la intersección con el eje x y la intersección con el eje y de y = 2x -2.
#La pendiente es (m = y² - y¹/x² - x¹). Halla la pendiente y la distancia euclidiana entre los puntos (2, 2) y (6, 10).
#compara las pendientes de las tareas 8 y 9.
print('Calcula la pendiente y la distancia entre los puntos (2, 2) y (6, 10)')
x1 = 2
y1 = 2
x2 = 6
y2 = 10
m2 = (y2 - y1) / (x2 - x1)
print('la pendiente es:', m2)
d = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print('la distancia euclidiana es:', d)
m1 = 2
print('comparando con la pendiente de y = 2x - 2:')
if m1 == m2:
    print('las pendientes son iguales')
else:
    print('las pendientes son diferentes')



print("Buscando x donde y = 0 en y = x^2 + 6x + 9")
for x in range(-10, 1):
    y = x**2 + 6*x + 9
    print("x = {x}, y = {y}")
    if y == 0:
        print("y es 0 cuando x es:", x)

python = len('python')
dragon = len('dragon')
print('longitud de python:', python)
print('longitud de dragon:', dragon)
print(python != dragon)

print('on' in 'python' and 'on' in 'dragon')

result = 'resultado'
print('jargon' in result)

print('on' not in 'dragon' and 'on' not in 'python')

length = len('python')
length_float = float(length)
length_str = str(length_float)
print('longitud como float:', length_float)
print('longitud como string:', length_str)

num = 8
is_even = num % 2 == 0
#Para definir un diccionario, que almacena pares clave:valor.
print("{num} es par?", is_even)

print(7 // 3 == int(2.7))

print(type('10') == type(10))
#para evitar errores en el codigo
try:
    print(int('9.8') == 10)
except ValueError as e:
    print("Error al convertir '9.8' a entero:", e)


hr = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
pago = hr * rate
print('pago semanal es de ', pago)

years = int(input("coloca tu año de naicmiesto"))
segundos = years * 365 * 24 * 60 * 60
print("tienes de vida un total de ", segundos, "segundos.")

print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
