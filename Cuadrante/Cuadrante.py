
# Proyecto 2: Fundamentos de Python - Módulo 2
# Autor: Roberto Reyes De Hoyos
# Fecha: 20/08 al 06/09 del  2025
# Descripción:
#   Este archivo contiene dos programas:
#   1.- Verificador de cantidad de palabra.
#   2.- Identificador del cuadrante en un punto en el plano cartesiano.

# PROGRAMA 1: Ancho de palabra

# Pedimos al usuario que introduzca una palabra
palabra = input("Ingresa una palabra: ")

# Se calcula la longitud de la palabra con la función len()
longitud = len(palabra)

# Se Revisa la longitud usando condicionales
if 4 <= longitud <= 8:
    print("✅ La palabra es correcta.")
elif longitud < 4:
    print(f"⚠️ Hacen falta letras. Solo tiene {longitud} letras.")
else:
    print(f"⚠️ Sobran letras. Tiene {longitud} letras.")

# Extra: Se muestra la palabra para reforzar manipulación de strings
print("Tu palabra en mayúsculas es:", palabra.upper())

# PROGRAMA 2: Encuentra el cuadrante

# Pedimos al usuario introducir dos números (coordenadas X y Y)
coordenada_x = int(input("\nIngrese la coordenada X: "))
coordenada_y = int(input("Ingrese la coordenada Y: "))

# Creamos un diccionario para almacenar los cuadrantes.
# La clave será una tupla de valores booleanos (x > 0, y > 0).
cuadrantes = {
    (True, True): "I",
    (False, True): "II",
    (False, False): "III",
    (True, False): "IV"
}

# Se revisa que las coordenadas sean diferentes o mayores a cero
if coordenada_x == 0 and coordenada_y == 0:
    print("⚠️ El punto está en el origen (0,0).")
elif coordenada_x == 0:
    print("⚠️ El punto está sobre el eje Y.")
elif coordenada_y == 0:
    print("⚠️ El punto está sobre el eje X.")
else:
    # Usamos el diccionario para identificar el cuadrante
    cuadrante = cuadrantes[(coordenada_x > 0, coordenada_y > 0)]
    print(f"✅ El punto ({coordenada_x}, {coordenada_y}) se encuentra en el cuadrante {cuadrante}")
