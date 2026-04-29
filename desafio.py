# Solicitar datos del participante
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
puntaje = float(input("Ingrese su puntaje: "))
asistencia = float(input("Ingrese su porcentaje de asistencia: "))
codigo_invitacion = input("Ingrese el código de invitación: ")

nombre_mayus = nombre.upper()
caracteres_sin_espacios = len(nombre.replace(" ", ""))

# Calcular promedio
promedio = (puntaje + asistencia) / 2

if edad >= 14:
    if promedio >= 80:
        if codigo_invitacion == "PYTHON2026":
            resultado = "Acceso VIP"
        else:
            resultado = "Acceso general"
    elif 60 <= promedio < 80:
        resultado = "Acceso con observación"
    else:
        resultado = "No puede ingresar por bajo rendimiento"
else:
    if codigo_invitacion == "PYTHON2026":
        resultado = "Acceso especial con acompañante"
    else:
        resultado = "No cumple la edad mínima"

# Mensaje adicional
mensaje_adicional = ""
if puntaje >= 90 and asistencia >= 90:
    mensaje_adicional = "Candidato destacado"
elif puntaje < 50 or asistencia < 50:
    mensaje_adicional = "Requiere refuerzo previo"

