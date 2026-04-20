# ===== PARTE A ===== 
# Respuesta 1:
nombre = "Lucía" 
edad = 16 
promedio = 9.75 
cursos = ["Python", "HTML", "CSS"]
print(type(nombre)) 
print(type(edad)) 
print(type(promedio)) 
print(type(cursos)) 
print(len(nombre)) 
"""a) Indica el tipo de dato de cada variable. """
print(type(nombre))
print(type(edad))
print(type(promedio))
print(type(cursos))
print(type(type(nombre)) )
print(type(type(edad)) )
print(type(type(promedio)) )
print(type(type(cursos)) )
print(type(len(nombre)) )
"""b) Escribe qué mostraría el programa en pantalla: el programa mostraria lo siguiente:
<class 'str'>
<class 'int'>
<class 'float'>
<class 'list'>
5
<class 'str'>
<class 'int'>
<class 'float'>
<class 'list'>
<class 'type'>
<class 'type'>
<class 'type'>
<class 'type'>
<class 'int'>
c) Explica qué hace len(nombre): este código muestra la cantidad de caracteres que tiene la variable nombre, en este caso, el resultado sería 5, ya que "Lucía" tiene 5 caracteres."""
# Respuesta 2:
"""a)  ¿Qué diferencia hay entre print() e input()?: print() se utiliza para mostrar información en la pantalla, mientras que input() se utiliza para recibir
información del usuario a través del teclado.
b) ¿Por qué un dato ingresado con input() puede dar error si se usa directamente en un cálculo?:
Un dato ingresado con input() se considera una cadena de texto (string) por defecto. Si intentamos usarlo directamente en un cálculo sin convertirlo al tipo de dato adecuado puede generar un error, ya que no se pueden realizar operaciones matemáticas con cadenas de texto
c) Explica la diferencia entre /, // y % : / es el operador de división normal que devuelve un resultado con decimales, incluso si ambos operandos son enteros. // es el operador de divisiónque devuelve el resultado redondeado hacia abajo al entero más cercano. % es el operador de módulo que devuelve el resto de la división entre dos números.
d) Escribe una instrucción que permita comprobar la versión de Python que se está usando: 
import sys
print(sys.version)
e) Escribe una instrucción que permita consultar las palabras reservadas de Python:
import keyword
print(keyword.kwlist)"""

# ===== PARTE B ===== 
# Código corregido 
ancho = float(input("Ingrese el ancho del terreno: "))
largo = float(input("Ingrese el largo del terreno: "))
precio = float(input("Ingrese el precio por metro cuadrado: "))
area = ancho * largo
costo = area * precio
print("Área total: " + str(area))
print("Costo estimado: " + str(costo))

"""a) ¿Cuáles eran los errores principales?:
Los errores principales eran:
- No se estaba convirtiendo la entrada del usuario a un tipo de dato numérico, lo que causaba errores al intentar realizar cálculos.
- No se estaban utilizando variables para almacenar los valores ingresados por el usuario, lo que dificultaba la realización de cálculos posteriores.
b) ¿Por qué tu corrección sí permite obtener resultados válidos?:
Mi corrección permite obtener resultados válidos porque:
- He convertido las entradas del usuario a tipo float para asegurarme de que se puedan realizar cálculos matemáticos correctamente.
- He utilizado variables para almacenar los valores ingresados por el usuario, lo que facilita la realización de cálculos posteriores y la presentación de resultados."""