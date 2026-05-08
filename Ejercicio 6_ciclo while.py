
"""# 1. Variable de control
variableControl = 1

#2. Condición
while variableControl < 5:
    
    #3. Codigo que se repite
    print(variableControl)

    #.4 Actualización de la variable
    variableControl += 1

else:
    print(f"Se dieron {variableControl} repeticiones y finalizó el ciclo.")"""


"""clave = ""
while clave != "python":
    clave = input("Ingrese la clave: ")
if clave != "python":
    print("Acceso denegado")
else:
    print("Acceso permitido")

clave = input("Ingrese la clave: ")

while clave != "python":
    clave = input("Ingrese la clave: ")
if clave != "python":
    print("Acceso denegado")
else:
    print("Acceso permitido")"""

"""opción = ""
while opción != "3":
    print("=== MENÚ ===")
    print("1. Saludar")
    print("2. Mostrar mensaje")
    print("3. Salir")
    opción = input("Selecciona una opción: ")

    if opción == "1":
        print("Hola, bienvenido")
    elif opción == "2":
        print("Estamos aprendiendo ciclos while")
    elif opción == "3":
        print("Saliendo del programa")
    else:
        print("Opción no válida")"""

"""count = 1
while count < 4:
    print("Contador:", count)
    count += 1
    if count == 3:
        break
    print("El ciclo se detuvo")"""

intentos = 0
clave_correcta == "python123"
while intentos < 4:
    clave = input("Ingrese la contraseña: ")
    if clave == "python123":
        print("Contraseña correcta, acceso permitido")
        break
    intentos = intentos + 1
    print("Contraseña incorrecta")
else:
    print("Cuenta bloqueada")