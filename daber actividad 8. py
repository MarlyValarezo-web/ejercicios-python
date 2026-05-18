# EJERCICIO LISTAS
notas = [8.5, 6.0, 9.0, 7.0, 5.5]
suma = 0
aprobados = 0
reprobados = 0
for nota in notas:
suma += nota
if nota >= 7:
aprobados += 1
else:
reprobados += 1
promedio = suma / len(notas)
print("Suma total de las notas:", suma)
print("Promedio del curso:", promedio)
print("Estudiantes que aprobaron:", aprobados)
print("Estudiantes que reprobaron:", reprobados)

# EJERCICIOS STRING
contrasena = "Python2026"
letras = 0
numeros = 0
cont_o = 0
for char in contrasena:
if char.isalpha():
letras += 1
elif char.isdigit():
numeros += 1
if char == 'o':
cont_o += 1
print("Letras en la contraseña:", letras)
print("Números en la contraseña:", numeros)
print("Veces que aparece 'o':", cont_o)

# EJERCICIOS CON SET
productos = {"teclado", "mouse", "monitor", "mouse", "impresora"}
unicos = 0
mas_6_letras = 0
for producto in productos:
unicos += 1
contador_letras = 0
for letra in producto:
contador_letras += 1
if contador_letras > 6:
mas_6_letras += 1
print("Productos únicos:", unicos)
print("Productos con más de 6 letras:", mas_6_letras)

# EJERCICIO CON BREAK
correo = input("Ingresa tu correo electrónico: ")
usuario = ""
for char in correo:
if char == '@':
break
usuario += char
print("Nombre de usuario:", usuario)

# EJERICIO CON CONTINUE
telefono = input("Ingresa un número de teléfono: ")
telefono_limpio = ""
for char in telefono:
if char == ' ' or char == '-':
continue
telefono_limpio += char
print("Teléfono limpio:", telefono_limpio)