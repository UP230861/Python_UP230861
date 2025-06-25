# Ejercicios - Día 5

# Nivel 1

# 1. Lista vacía
lista = []
print('1.', lista)

# 2. Lista con más de 5 elementos
lista_frutas = ['manzana', 'banana', 'naranja', 'mango', 'uva', 'pera']
print('2.', lista_frutas)

# 3. Longitud lista_frutas
print('3.', len(lista_frutas))

# 4. Primer, medio y último
print('4.', lista_frutas[0], lista_frutas[len(lista_frutas)//2], lista_frutas[-1])

# 5. Lista con datos mixtos
datos = ['Juan', 25, 1.75, 'soltero', 'Calle Falsa 123']
print('5.', datos)

# 6. Lista de empresas
empresas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print('6.', empresas)

# 7. Longitud empresas
print('7.', len(empresas))

# 8. Primer, medio y último empresa
print('8.', empresas[0], empresas[len(empresas)//2], empresas[-1])

# 9. Modificar primera empresa
empresas[0] = 'Meta'
print('9.', empresas)

# 10. Añadir empresa
empresas.append('Twitter')
print('10.', empresas)

# 11. Insertar empresa
empresas.insert(len(empresas)//2, 'Spotify')
print('11.', empresas)

# 12. Poner una empresa en mayúsculas
empresas[1] = empresas[1].upper()
print('12.', empresas)

# 13. Unir empresas con separador
empresas_juntas = '#; '.join(empresas)
print('13.', empresas_juntas)

# 14. Existe empresa?
existe_google = 'Google' in empresas
print('14.', existe_google)

# 15. Ordenar empresas
empresas.sort()
print('15.', empresas)

# 16. Invertir empresas
empresas.reverse()
print('16.', empresas)

# 17. Primeras 3 empresas
print('17.', empresas[0:3])

# 18. Últimas 3 empresas
print('18.', empresas[-3:])

# 19. Empresa del medio
print('19.', empresas[len(empresas)//2:len(empresas)//2+1])

# 20. Quitar primera empresa
empresas.pop(0)
print('20.', empresas)

# 21. Quitar empresa del medio
empresas.pop(len(empresas)//2)
print('21.', empresas)

# 22. Quitar última empresa
empresas.pop(-1)
print('22.', empresas)

# 23. Vaciar lista
empresas.clear()
print('23.', empresas)

# 24. Borrar lista
del empresas

# 25. Unir dos listas
front = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back = ['Node', 'Express', 'MongoDB']
full = front + back
print('25.', full)

# 26. Insertar Python y SQL
pos_redux = full.index('Redux')
full.insert(pos_redux+1, 'Python')
full.insert(pos_redux+2, 'SQL')
print('26.', full)


# Nivel 2
# 27. Edades
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Ordenar
edades.sort()
print('27. Edades ordenadas:', edades)

# Min y max
min_edad = min(edades)
max_edad = max(edades)
print('27. Min:', min_edad, '| Max:', max_edad)

# Añadir min y max
edades.append(min_edad)
edades.append(max_edad)
print('27. Edades con min y max:', edades)

# Mediana
n = len(edades)
if n % 2 == 0:
    mediana = (edades[n//2 - 1] + edades[n//2]) / 2
else:
    mediana = edades[n//2]
print('27. Mediana:', mediana)

# Promedio
promedio = sum(edades)/len(edades)
print('27. Promedio:', promedio)

# Rango
rango = max(edades)-min(edades)
print('27. Rango:', rango)

# Comparar diferencias
diff_min = abs(min(edades)-promedio)
diff_max = abs(max(edades)-promedio)
print('27. abs(min-prom):', diff_min, '| abs(max-prom):', diff_max)

# 28. Países
paises = ['China', 'Rusia', 'USA', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']

# País del medio
mitad = len(paises)//2
print('28. País del medio:', paises[mitad:mitad+1])

# Dividir países
if len(paises) % 2 == 0:
    parte1 = paises[:mitad]
    parte2 = paises[mitad:]
else:
    parte1 = paises[:mitad+1]
    parte2 = paises[mitad+1:]
print('28. Primera parte:', parte1)
print('28. Segunda parte:', parte2)

# Desempacar países
c1, c2, c3, *otros = paises
print('28. Primero:', c1, '| Segundo:', c2, '| Tercero:', c3, '| Otros:', otros)
