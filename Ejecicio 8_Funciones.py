"""def generate_full_name():
first_name = "Marly"
last_name = "Valarezo"
space = " "
full_name = first_name + space+ last_name
print full_name

def mostrar_estudiante(nombre, curso):
    print("=== DATOS DEL ESTUDIANTE ===")
    print(f"Nombre: {nombre}")
    print(f"Curso: {curso}")

nombre_usuario = input("Ingrese el nombre del estudiante: ")
curso_usuario = input('Ingrese el curso del estudiante: ')
mostrar_estudiante(nombre_usuario, curso_usuario)

Ejercicio: registrar varios estudiantes usando funciones y while.

def mostrar_estudiante(nombre, curso):
    print("=== DATOS DEL ESTUDIANTE ===")
    print(f"Nombre: {nombre}")
    print(f"Curso: {curso}")


def mensaje_final():
    print("Fin del programa")


def main():
    while True:
        try:
            total = int(input("¿Cuántos estudiantes desea ingresar?: "))
            if total < 0:
                print("Ingrese un número cero o positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número entero.")

    contador = 0
    while contador < total:
        contador += 1
        nombre_usuario = input(f"Ingrese el nombre del estudiante #{contador}: ")
        curso_usuario = input(f"Ingrese el curso del estudiante #{contador}: ")
        mostrar_estudiante(nombre_usuario, curso_usuario)

    mensaje_final()


if __name__ == "__main__":
    main()


def obtener_mensaje():
    mensaje = "Bienvenido al sistema"
    return mensaje
def generar_nombre_completo():
    nombre = "Santiago"
    apellido = "Moreno"
    espacio = " "
    nombre_completo = nombre + espacio + apellido
    return nombre_completo
print(obtener_mensaje())
print(generar_nombre_completo())"""

def obtener_mensaje():
    return mensaje

def generar_nombre_completo():
    nombre_completo = nombre + espacio + apellido
    return nombre_completo
mensaje =(input("Que mensaje desea poner"))
nombre = (input("Ingrese su nombre"))
apellido = (input("Ingrese su apellido"))

print(f"{obtener_mensaje()}, {generar_nombre_completo()}")