# Nivel 1: Operaciones básicas
texto = "Programación Para Todos"
print("Programación Para Todos")
print("Cantidad de caracteres:", len(texto))

# Nivel 2: Transformación de texto
print("Mayúsculas:", texto.upper())
print("Minúsculas:", texto.lower())
print("Title:", texto.title())
print("Capitalize:", texto.capitalize())

# Nivel 3: Búsqueda y verificación
print("Empieza con 'Programación'?:", texto.startswith("Programación"))
print("Termina con 'Todos'?:", texto.endswith("Todos"))
print("Posición de 'Para':", texto.find("Para"))
print("Contiene 'Python'?:", "Python" in texto)

# Nivel 4: Manipulación
texto_modificado = texto.replace("Programación", "Python")
print("Reemplaza 'Programación' por 'Python':", texto_modificado)
palabras = texto_modificado.split()
print("División en palabras:", palabras)
print("Unión con ' - ':", " - ".join(palabras))

# Índices
print("Primer carácter:", texto[0])
print("Último carácter:", texto[-1])
print("Carácter en la posición 5:", texto[5])

# Nivel 6: Aplicación simple
nombre_completo = "Marly Valarezo"
print("Nombre completo:", nombre_completo)
print(f"Hola, mi nombre es {nombre_completo}")
iniciales = "".join([parte[0].upper() for parte in nombre_completo.split()])
print("Acrónimo:", iniciales)
