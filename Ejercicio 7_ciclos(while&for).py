"""#Ejercicio 1
# Solicitar número
n = int(input("Ingrese un número: "))
# Variables de control
contador = 1
suma = 0
# Condición del ciclo
while n < 0:
    print("Número invalidod; ingrese un número positivo")
    n = int(input("Ingrese un número: "))
while contador <= n:
        suma += contador  
        contador += 1   
# Mostrar el resultado
print(f"La suma de los números enteros desde 1 hasta {n} es: {suma}")


# Ejercicio 2
# Solicitar precio del producto
precio = float(input("Ingrese el precio del producto: "))
# Variable de control
total_compras = 0
cantidad_compras = 0
# Condición del ciclo
while True:
    precio = float(input("Ingrese el precio del producto (0 o negativo para finalizar): "))
    if precio <= 0:
        break
    total_compras += precio
    cantidad_compras += 1
print(f"Cantidad de compras: {cantidad_compras}")
print(f"Suma total de las compras: {total_compras}")
print("Registro de compras finalizado")


#Ejercicio 3
# Solicitar número entero positivo
limiteSuperior = int(input("Ingrese un número entero positivo como límite superior: "))
# Variable de control
contador = 1
# Condición del ciclo
while contador <= limiteSuperior:
    if contador % 5 == 0:
        contador += 1
        continue
    print(contador)
    contador += 1"""

"""#Ciclo For
numbers = [0, 1, 2, 3, 4, 5]
for numbers in numbers:
    print (numbers)

notas = [8, 9, 10, 7, 6]
suma = 0
for nota in notas:
    suma += nota
promedio = suma / len(notas)
print(f"El promedio de las notas es: {promedio}")

language = "Python"
for letter in language:
    print(letter)

palabra = input("Ingrese una palabra: ").lower()
vocales = 0
for letra in palabra:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        vocales += 1
print(f"Las vocales en la palabra son: {vocales}")
consonantes = len(palabra) - vocales
print(f"Las consonantes en la palabra son: {consonantes}")
total = len(palabra)
print(f"La cantidad total de letras es: {total}")

it_conpanies = {"Facebook","Google","Amazon", "Apple", "Facebook" }
for company in it_conpanies:
    print(company)

asistentes = {"Ana", "Luis", "Maria", "Ana", "Carlos", "Luis", "Sofia"}
for estudiante in asistentes:
    print("Generar certificado para:", estudiante)"""

"""numbers = [0, 16, 25, 3, 40, 5]
num = int(input("Ingrese un numero:"))
for number in numbers:
    if number == num:
        print("Ganaste")
        break
else:
    print("Perdiste")"""

"""#For in range
#1)
suma = 0
notas = int(input("Cuantas calificaciones desea ingresar: "))
for n in range(notas):
    nota = float(input(f"Ingresa la nota {n+1}: "))
    suma+=nota
print(f"El promedio de las notas es: {suma/notas}")

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
notas = int(input("Ingrese un número: (1-10)"))
for i in n:
    while notas == i:
        print(f"El número {notas} se encuentra en la lista")
        break
else:
    print(f"El número {notas} no se encuentra en la lista")"""

"""#2)
num = int(input("Ingrese un número: "))
lista = int(input("Ingrese desde que número desea ver la tabla de multiplicar : "))
lis = int(input("Ingrese hasta que número desea ver la tabla de multiplicar : "))
for i in range(lista, lis+1):
    print(f"{i} x {num} = {num*i}")"""

"""#3)
# Lista de notas del estudiante
# LA PRIMERA Y ULTIMA NOTA ES DE PRUEBA DIAGNOSTICA notas = [5, 8, 9, 7, 10]
notas = []
num_notas = int(input("Ingrese el número de notas del estudiante: "))
for i in range(num_notas):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)
promedio = sum(notas) / len(notas)
print(f"El promedio de las notas del estudiante es: {promedio}")"""

"""#4)
#Solo tiene que mostrar los números pares entre el rango que el usuario ingrese
num = int(input("Ingrese un número: "))
lista = int(input("Ingrese desde que número desea ver la tabla de multiplicar : "))
lis = int(input("Ingrese hasta que número desea ver la tabla de multiplicar : "))
for i in range(lista, lis+1):
    if i % 2 == 0:
        print(f"{i} x {num} = {num*i}")"""

"""#5)
# Lista de estudiantes en orden
estudiantes = ["Ana", "Luis", "María", "Carlos", "Sofía", "Mateo"]
# Formar parejas tomando dos estudiantes a la vez
for i in range(0, len(estudiantes), 2):
    print(f"Pareja {i//2+1}: {estudiantes[i]} y {estudiantes[i+1]}")"""

#6)
#Un jugador empieza con 3 vidas
#Cada vez que el jugador pierde, se le resta una vida
for vidas in range(3, 0, -1):
    print(f"Vidas restantes: {vidas}")
        print("Has perdido una vida.")
    
#Ciclo For anidado
#1)
# Asignar estudiantes a los puestos de un laboratorio
# El laboratorio tiene 3 filas y 4 computadoras por cada fila

for fila in range(1, 4):
    for computadora in range(1, 5):
        nombre = input('Ingrese el nombre del estudiante: ')
        
        print(nombre, 'asignado a Fila', fila,
        '- Computadora', computadora)
    print('Fin de la fila', fila)