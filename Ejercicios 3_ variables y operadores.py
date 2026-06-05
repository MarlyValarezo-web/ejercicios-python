# Ejercicios de variables, operadores y entrada de usuario

# 1. Declara tu edad como una variable de tipo entero.
edad = 16
print("Edad (int):", edad, type(edad))

# 2. Declara tu estatura como una variable de tipo decimal (float).
estatura = 1.75
print("Estatura (float):", estatura, type(estatura))

# 3. Área de un triángulo
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area_triangulo = 0.5 * base * altura
print("Área del triángulo:", area_triangulo)

# 5. Perímetro de un triángulo
a = float(input("Ingrese el lado a del triángulo: "))
b = float(input("Ingrese el lado b del triángulo: "))
c = float(input("Ingrese el lado c del triángulo: "))
perimetro_triangulo = a + b + c
print("Perímetro del triángulo:", perimetro_triangulo)

# 6. Área y perímetro de un rectángulo
longitud = float(input("Ingrese la longitud del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))
area_rectangulo = longitud * ancho
perimetro_rectangulo = 2 * (longitud + ancho)
print("Área del rectángulo:", area_rectangulo)
print("Perímetro del rectángulo:", perimetro_rectangulo)

# 7. Área y circunferencia de un círculo
r = float(input("Ingrese el radio del círculo: "))
pi = 3.14
area_circulo = pi * r * r
circunferencia = 2 * pi * r
print("Área del círculo:", area_circulo)
print("Circunferencia del círculo:", circunferencia)

# 9. Pendiente y distancia euclidiana entre (2,2) y (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
m = (y2 - y1) / (x2 - x1)
print("Pendiente entre (2,2) y (6,10):", m)
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Distancia euclidiana entre (2,2) y (6,10):", distancia)

# 11. Valor de y para la función y = x^2 + 6x + 9
def evaluar_funcion(x):
    return x ** 2 + 6 * x + 9

valores_x = [-5, -3, -1, 0, 1, 2, 3]
for x in valores_x:
    y = evaluar_funcion(x)
    print(f"x = {x}, y = {y}")

print("La función es igual a 0 cuando x = -3, porque y = (x + 3)^2.")

# 12. Longitud de las palabras y comparación booleana
long_python = len("python")
long_dragon = len("dragón")
print("Longitud de 'python':", long_python)
print("Longitud de 'dragón':", long_dragon)
print("¿Longitudes iguales?", long_python == long_dragon)

# 13. Usar operador and para verificar si "on" está en ambas palabras
contiene_on_python = "on" in "python"
contiene_on_dragon = "on" in "dragón"
print("'on' está en 'python' y en 'dragón'?:", contiene_on_python and contiene_on_dragon)

# 14. Verificar si 'jerga' está en la oración dada
oracion = "Espero que este curso no esté lleno de jerga."
print("¿La palabra 'jerga' está en la oración?", "jerga" in oracion)

# 15. Verificar si 'on' está en 'python' y en 'dragon'
print("'on' está en 'python' y en 'dragon'?:", ("on" in "python") and ("on" in "dragon"))

# 16. Convertir la longitud de 'python' a float y a string
long_python_float = float(long_python)
long_python_str = str(long_python_float)
print("Longitud de 'python' como float:", long_python_float)
print("Longitud de 'python' como string:", long_python_str)
print("Tipo final:", type(long_python_str))

# 18. Verificar división entera de 7 entre 3 e int(2.7)
division_entera = 7 // 3
int_2_7 = int(2.7)
print("7 // 3 == int(2.7)?", division_entera == int_2_7)

# 19. Verificar tipos de '10' y 10
print("Tipo de '10' igual al tipo de 10?:", type("10") == type(10))

# 20. Verificar int('9.8') == 10
try:
    comparacion_9_8 = int('9.8') == 10
except ValueError as error:
    comparacion_9_8 = False
    print("int('9.8') lanza un ValueError:", error)
print("int('9.8') == 10?:", comparacion_9_8)

# 21. Pago total por horas trabajadas
tasas_hora = float(input("Ingrese la tarifa por hora: "))
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
pago_total = horas_trabajadas * tasas_hora
print("Pago total:", pago_total)

# 22. Segundos vividos a partir de los años ingresados
anios_vividos = float(input("Ingrese los años que ha vivido: "))
segundos_por_anio = 365 * 24 * 60 * 60
segundos_vividos = anios_vividos * segundos_por_anio
print("Segundos vividos (aprox.):", segundos_vividos)

# 23. Mostrar la tabla solicitada
print("\nTabla:")
for i in range(1, 6):
    fila = [str(i), "1", str(i), str(i ** 2), str(i ** 3)]
    print(" ".join(fila))