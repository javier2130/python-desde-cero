# Programa completo integrando conceptos básicos
# Pedir nombre
nombre = input("¿Cuál es tu nombre?")
# Saludar
print("Hola", nombre)
# Pedir edad y convertir a número
edad = int(input("¿Cuál es tu edad?"))
# Mostrar la edad
print("Tu edad es", edad)
# Mostrar doble de la edad
print("El doble de tu edad es", 2 * edad)
# Preguntar si está suscrito
respuesta = input("¿Estás suscrito al canal?")
# Evaluar respuesta
if respuesta == "si":
    print("Muchas gracias", nombre)
else:
    print("Suscríbete por favor y activa la campanita")
