#Ejercicio 1
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
    contador += 1 