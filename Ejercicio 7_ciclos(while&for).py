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

numbers = [0, 16, 25, 3, 40, 5]
num = int(input("Ingrese un numero:"))
for number in numbers:
    if number == num:
        print("Ganaste")
        break
else:
    print("Perdiste")
