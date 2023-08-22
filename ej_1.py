'''
1 - Escribir una función que calcule el máximo común divisor entre dos números.
'''

# Forma 1

def maximo_comun_divisor(a, b):

    numero_menor = min(a, b)
    
    mcd = 1
    
    for numero in range(1,numero_menor+1):
        if a % numero == 0 and b % numero == 0:
            mcd = numero
    
    return mcd

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

resultado = maximo_comun_divisor(numero1,numero2)
print(f"El Maximo Comun Divisor entre {numero1} y {numero2} es: {resultado}")

# Forma 2 (Euclides)

def maximo_comun_divisor_euclides(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

mcd = maximo_comun_divisor_euclides(num1,num2)
print(f"El máximo común divisor entre {num1} y {num2} es {mcd}")
