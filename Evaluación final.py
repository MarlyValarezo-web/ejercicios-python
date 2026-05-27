# Sistema de habilitación
correcta_clave = "python123"
clave = ""
while clave == correcta_clave:
    clave = input("Ingrese la clave de acceso: ")
    if clave != correcta_clave:
        print("Clave incorrecta. Intente de nuevo.")

print("Acceso permitido")
print("Bienvenido al sistema de habilitación para el reto final de Python\n")

temas = ["variables", "cálculos", "input", "print", "f-string", "condicionales", "ciclos"]
print("Temas evaluados en la unidad:")
for tema in temas:
    print("-", tema)

cantidad_estudiantes = int(input("\nIngrese la cantidad de estudiantes a revisar: "))
print()

for i in range(1, cantidad_estudiantes + 1):
    print(f"Registro del estudiante {i}")
    nombre = input("Ingrese el nombre del estudiante: ")
    nota_ejercicios = float(input("Ingrese la nota de ejercicios básicos: "))
    nota_condicionales = float(input("Ingrese la nota de condicionales: "))
    nota_ciclos = float(input("Ingrese la nota de ciclos: "))
    practicas = int(input("Ingrese la cantidad de prácticas completadas: "))

    promedio_final = (nota_ejercicios + nota_condicionales + nota_ciclos) / 3

    if promedio_final >= 7:
        if promedio_final >= 9 and practicas >= 5:
            estado = "Habilitado con nivel alto"
        elif practicas >= 4:
            estado = "Habilitado"
        else:
            estado = "Pendiente por prácticas"
    else:
        estado = "Requiere refuerzo"

    print("\nReporte del estudiante")
    print(f"Nombre: {nombre}")
    print(f"Promedio final: {promedio_final:.2f}")
    print(f"Prácticas completadas: {practicas}")
    print(f"Estado académico: {estado}\n")

print("Proceso finalizado")
