# Ejercicio 2: Menú de calificaciones
# Cada operación está separada en una función diferente.

def calcular_promedio(cal1, cal2, cal3):
    return (cal1 + cal2 + cal3) / 3


def obtener_nota_mayor(cal1, cal2, cal3):
    return max(cal1, cal2, cal3)


def obtener_nota_menor(cal1, cal2, cal3):
    return min(cal1, cal2, cal3)


def determinar_aprobacion(cal1, cal2, cal3, minimo_aprobado=60):
    promedio = calcular_promedio(cal1, cal2, cal3)
    return promedio >= minimo_aprobado


def solicitar_calificacion(numero):
    while True:
        try:
            valor = float(input(f"Ingrese la calificación {numero}: "))
            if 0 <= valor <= 100:
                return valor
            print("Por favor ingrese un valor entre 0 y 100.")
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.")


def solicitar_calificaciones():
    cal1 = solicitar_calificacion(1)
    cal2 = solicitar_calificacion(2)
    cal3 = solicitar_calificacion(3)
    return cal1, cal2, cal3


def mostrar_menu():
    print("\nMenú de operaciones:")
    print("1. Calcular el promedio")
    print("2. Mostrar la nota mayor")
    print("3. Mostrar la nota menor")
    print("4. Determinar si el estudiante aprueba o reprueba")
    print("5. Salir")


def ejecutar_opcion(opcion, cal1, cal2, cal3):
    if opcion == "1":
        return calcular_promedio(cal1, cal2, cal3)
    if opcion == "2":
        return obtener_nota_mayor(cal1, cal2, cal3)
    if opcion == "3":
        return obtener_nota_menor(cal1, cal2, cal3)
    if opcion == "4":
        return determinar_aprobacion(cal1, cal2, cal3)
    return None


def main():
    print("Programa de calificaciones")
    cal1, cal2, cal3 = solicitar_calificaciones()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        resultado = ejecutar_opcion(opcion, cal1, cal2, cal3)

        if opcion == "1":
            print(f"Promedio: {resultado:.2f}")
        elif opcion == "2":
            print(f"Nota mayor: {resultado}")
        elif opcion == "3":
            print(f"Nota menor: {resultado}")
        elif opcion == "4":
            estado = "aprueba" if resultado else "reprueba"
            print(f"El estudiante {estado}.")
        elif opcion == "5":
            print("Saliendo del programa. Hasta luego.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
