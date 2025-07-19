# DAY_4

# 1. Concatenar cadenas
palabra1 = 'Treinta'
palabra2 = 'Días'
palabra3 = 'De'
palabra4 = 'Python'
print('1.', palabra1 + ' ' + palabra2 + ' ' + palabra3 + ' ' + palabra4)

# 2. Concatenar otras cadenas
texto1 = 'Programando'
texto2 = 'Para'
texto3 = 'Todos'
print('2.', texto1 + ' ' + texto2 + ' ' + texto3)

# 3. Declarar variable empresa
empresa = "Programando Para Todos"
print('3.', empresa)

# 4. Imprimir empresa
print('4.', empresa)

# 5. Longitud de empresa
longitud_empresa = len(empresa)
print('5.', longitud_empresa)

# 6. Empresa en mayúsculas
empresa_mayusculas = empresa.upper()
print('6.', empresa_mayusculas)

# 7. Empresa en minúsculas
empresa_minusculas = empresa.lower()
print('7.', empresa_minusculas)

# 8. Formatear empresa
print('8. Capitalize:', empresa.capitalize())
print('   Title:', empresa.title())
print('   Swapcase:', empresa.swapcase())

# 9. Primer palabra
palabras_empresa = empresa.split()
print('9.', palabras_empresa[0])

# 10. ¿Contiene la palabra?
contiene_programando = 'Programando' in empresa
print('10.', contiene_programando)

# 11. Reemplazar palabra
empresa_nueva = empresa.replace('Programando', 'Python')
print('11.', empresa_nueva)

# 12. Reemplazar "Todos" por "Todos/as"
texto_py = 'Python para Todos'
texto_py_modificado = texto_py.replace('Todos', 'Todos/as')
print('12.', texto_py_modificado)

# 13. Separar empresa
empresa_dividida = empresa.split()
print('13.', empresa_dividida)

# 14. Separar compañías
companias = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
companias_divididas = companias.split(', ')
print('14.', companias_divididas)

# 15. Carácter en índice 0
print('15.', empresa[0])

# 16. Último índice
ultimo_indice = len(empresa)-1
print('16.', ultimo_indice)

# 17. Carácter en índice 10
print('17.', empresa[10])

# 18. Acrónimo "Python para Todos"
frase_py = "Python para Todos"
acronimo_py = ''.join([letra[0] for letra in frase_py.split()])
print('18.', acronimo_py)

# 19. Acrónimo "Programando Para Todos"
acronimo_empresa = ''.join([letra[0] for letra in empresa.split()])
print('19.', acronimo_empresa)

# 20. Índice primera 'P'
indice_P = empresa.index('P')
print('20.', indice_P)

# 21. Índice primera 'T'
indice_T = empresa.index('T')
print('21.', indice_T)

# 22. Última 'a' en texto largo
texto_largo = "Programando Para Todos Personas"
ultima_a = texto_largo.rfind('a')
print('22.', ultima_a)

# 23. Índice primera 'porque'
frase = "No puedes terminar una frase con porque porque porque es una conjunción"
indice_porque = frase.find('porque')
print('23.', indice_porque)

# 24. Índice última 'porque'
indice_ultima_porque = frase.rfind('porque')
print('24.', indice_ultima_porque)

# 25. Cortar "porque porque porque"
inicio = frase.find('porque')
fin = frase.rfind('porque') + len('porque')
print('25.', frase[inicio:fin])

# 26. Índice primera 'porque'
print('26.', frase.index('porque'))

# 27. Cortar "porque porque porque"
print('27.', frase[inicio:fin])

# 28. ¿Empieza con "Programando"?
print('28.', empresa.startswith('Programando'))

# 29. ¿Termina con "todos"?
print('29.', empresa.endswith('todos'))

# 30. Quitar espacios
texto_con_espacios = "   Programando Para Todos      "
texto_limpio = texto_con_espacios.strip()
print('30.', texto_limpio)

# 31. Identificadores válidos
identificador_1 = '30DiasDePython'.isidentifier()
identificador_2 = 'treinta_dias_de_python'.isidentifier()
print('31.', identificador_1)
print('    ', identificador_2)

# 32. Unir lista con hash
bibliotecas = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
bibliotecas_unidas = ' # '.join(bibliotecas)
print('32.', bibliotecas_unidas)

# 33. Salto de línea
print('33. Me gusta este desafío.\n¿Qué sigue?')

# 34. Tabulador
print('34. Nombre\tEdad\tPaís\tCiudad')
print('    Asabeneh\t250\tFinlandia\tHelsinki')

# 35. Área del círculo
radio = 10
area_circulo = 3.14 * radio ** 2
print('35. El área de un círculo con radio', radio, 'es', area_circulo, 'metros cuadrados.')

# 36. Operaciones
num1 = 8
num2 = 6
print('36.', num1, '+', num2, '=', num1 + num2)
print('    ', num1, '-', num2, '=', num1 - num2)
print('    ', num1, '*', num2, '=', num1 * num2)
print('    ', num1, '/', num2, '=', round(num1 / num2, 2))
print('    ', num1, '%', num2, '=', num1 % num2)
print('    ', num1, '//', num2, '=', num1 // num2)
print('    ', num1, '**', num2, '=', num1 ** num2)
