# Ejercicios de Condicionales - Nivel 1 y Nivel 2

# Nivel 1
# Ejercicio 1: Verificar edad para aprender a conducir
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Tienes la edad suficiente para aprender a conducir.")
else:
    faltan = 18 - edad
    print(f"Necesitas {faltan} años más para aprender a conducir.")

# Ejercicio 2: Comparar edades
my_age = 25
your_age = int(input("Ingrese su edad: "))
diferencia = abs(my_age - your_age)
if your_age > my_age:
    if diferencia == 1:
        print("Eres 1 año mayor que yo.")
    else:
        print(f"Eres {diferencia} años mayor que yo.")
elif your_age < my_age:
    if diferencia == 1:
        print("Soy 1 año mayor que tú.")
    else:
        print(f"Soy {diferencia} años mayor que tú.")
else:
    print("Tenemos la misma edad.")

# Ejercicio 3: Comparar dos números
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual a {b}")

# Nivel 2
# Ejercicio 1: Asignar calificación según puntaje
puntaje = int(input("Ingrese su puntaje: "))
if 90 <= puntaje <= 100:
    print("A")
elif 80 <= puntaje <= 89:
    print("B")
elif 70 <= puntaje <= 79:
    print("C")
elif 60 <= puntaje <= 69:
    print("D")
elif 0 <= puntaje <= 59:
    print("F")
else:
    print("Puntaje inválido")

# Ejercicio 2: Determinar estación del año según mes
mes = input("Ingrese el mes: ").lower()
if mes in ["septiembre", "octubre", "noviembre"]:
    print("Otoño")
elif mes in ["diciembre", "enero", "febrero"]:
    print("Invierno")
elif mes in ["marzo", "abril", "mayo"]:
    print("Primavera")
elif mes in ["junio", "julio", "agosto"]:
    print("Verano")
else:
    print("Mes inválido")

# Ejercicio 3: Verificar fruta en lista
fruits = ['banana', 'orange', 'mango', 'lemon']
fruta = input("Ingrese una fruta: ").lower()
if fruta in fruits:
    print("Esa fruta ya existe en la lista")
else:
    fruits.append(fruta)
    print(f"Fruta agregada. Lista actual: {fruits}")


