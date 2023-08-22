'''
Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con 
cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
'''

# cadena = str(input("Ingrese una frase:"))
cadena = "HOLA HOLA UNO DOS DOS TRES TRES TRES"

cadena_dividida = cadena.split(" ")

diccionario_de_palabras = {}

for palabra in cadena_dividida:

    if not palabra in diccionario_de_palabras:
        diccionario_de_palabras[palabra] = 1
    else:
        diccionario_de_palabras[palabra] += 1

print(diccionario_de_palabras)

