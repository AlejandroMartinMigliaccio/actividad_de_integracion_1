'''
Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada 
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función 
que reciba el diccionario generado con la función anterior y devuelva una tupla con la 
palabra más repetida y su frecuencia.
'''

def contador_de_palabras(cadena):

    cadena_dividida = cadena.split(" ")

    diccionario_de_palabras = {}

    for palabra in cadena_dividida:

        if not palabra in diccionario_de_palabras:
            diccionario_de_palabras[palabra] = 1
        else:
            diccionario_de_palabras[palabra] += 1

    return diccionario_de_palabras

''''''

def palabra_mas_usada(diccionario):

    palabra_mas_repetida = max(diccionario, key=diccionario.get)
    cantidad_de_repeticiones = diccionario[palabra_mas_repetida]
    diccionario_palabras = (palabra_mas_repetida, cantidad_de_repeticiones)
    return diccionario_palabras

''''''

cadena = "HOLA HOLA UNO DOS DOS TRES TRES TRES"

palabrasDelTexto = contador_de_palabras(cadena)
print(palabrasDelTexto)

palabraMasRepetida = palabra_mas_usada(palabrasDelTexto)

# Tupla

print(palabraMasRepetida) 
print(f"La palabra mas repetida es {palabraMasRepetida[0]} y su frecuencia es {palabraMasRepetida[1]}")




