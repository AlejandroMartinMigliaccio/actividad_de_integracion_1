'''
Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una 
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero 
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el 
ejercicio tanto de manera iterativa como recursiva. 
'''

# Modo iterativo

def get_int_iterativo():
    
    cadena_ingresada = input("Ingrese un valor entero: ")
    valor = str.isdigit(cadena_ingresada)

    while valor == True:
        print(f"El valor ingresado es {cadena_ingresada}")
        break

    else:
        print(f"El valor '{cadena_ingresada}' no es un numero entero")

# Modo recursivo

def get_int_recursivo():

    cadena_ingresada = input("Ingrese un valor entero: ")
    valor = str.isdigit(cadena_ingresada)

    if valor == True:
        print(f"El valor ingresado es {cadena_ingresada}")

    else:
        print(f"El valor '{cadena_ingresada}' no es un numero entero")

''''''

funcionDePrueba = get_int_iterativo()
print(funcionDePrueba)