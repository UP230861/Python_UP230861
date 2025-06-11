

#  Exercises - Day 3

# Declare your age as integer variable
numeroedad = input("¿Cuál es tu edad?")

# Declare your height as a float variable
higth = input(float("¿Cuál es tu altura?"))

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h)
print('Coloca valores de base y altura de un triángulo')
base = input(float("¿Cuál es la base?"))
altura = input(float("¿Cuál es la altura?"))
area_total = (0.5 * base * altura)
print('El área total es de:', area_total)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c)
print('Coloca valores de los lados de un triángulo')
a = input(float("Valor de a:"))
b = input(float("Valor de b:"))
c = input(float("Valor de c:"))
perimetro_total = (a + b + c)
print('El perímetro es de:', perimetro_total)

# Get length and width of a rectangle using prompt. Calculate its area and perimeter
print('Coloca valores de los lados de un rectángulo')
largo = input(float("Largo"))
ancho = input(float("Ancho"))
area_rectangulo = (largo * ancho)
print('El área es de:', area_rectangulo)
perimetro_rectangulo = (2 * (largo + ancho))
print('El perímetro es de:', perimetro_rectangulo)

# Get radius of a circle using prompt. Calculate the area and circumference
print('Coloca valores de los lados de un círculo')
r = input(float("Radio"))
pi = 3.14
area_circulo = (pi(r * r))
cir = (2(pi * r))
print('El perímetro es de:', cir)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# Compare the slopes in tasks 8 and 9
print('Calcula la pendiente y la distancia entre los puntos (2, 2) y (6, 10)')
x1 = 2
y1 = 2
x2 = 6
y2 = 10
m2 = (y2 - y1) / (x2 - x1)
print('La pendiente es:', m2)
d = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print('La distancia euclidiana es:', d)
m1 = 2
print('Comparando con la pendiente de y = 2x - 2:')
if m1 == m2:
    print('Las pendientes son iguales')
else:
    print('Las pendientes son diferentes')

# Calculate the value of y (y = x^2 + 6x + 9). Try different x values and find where y = 0
print("Buscando x donde y = 0 en y = x^2 + 6x + 9")
for x in range(-10, 1):
    y = x**2 + 6*x + 9
    print("x = {x}, y = {y}")
    if y == 0:
        print("y es 0 cuando x es:", x)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement
python = len('python')
dragon = len('dragon')
print('Longitud de python:', python)
print('Longitud de dragon:', dragon)
print(python != dragon)

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

# Check if jargon is in the sentence
result = 'resultado'
print('jargon' in result)

# There is no 'on' in both dragon and python
print('on' not in 'dragon' and 'on' not in 'python')

# Find the length of the text python and convert the value to float and then to string
length = len('python')
length_float = float(length)
length_str = str(length_float)
print('Longitud como float:', length_float)
print('Longitud como string:', length_str)

# Even numbers are divisible by 2 and the remainder is zero
num = 8
is_even = num % 2 == 0
print("{num} es par?", is_even)

# Check if the floor division of 7 by 3 is equal to int(2.7)
print(7 // 3 == int(2.7))

# Check if type of '10' is equal to type of 10
print(type('10') == type(10))

# Check if int('9.8') == 10 (con manejo de error)
try:
    print(int('9.8') == 10)
except ValueError as e:
    print("Error al convertir '9.8' a entero:", e)

# Prompt user to enter hours and rate per hour and calculate pay
hr = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
pago = hr * rate
print('Pago semanal es de ', pago)

# Prompt user to enter number of years and calculate seconds lived
years = int(input("Coloca tu año de nacimiento"))
segundos = years * 365 * 24 * 60 * 60
print("Tienes de vida un total de ", segundos, "segundos.")

# Write a Python script that displays the following table
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")

