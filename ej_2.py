'''
2 - Escribir una función que calcule el mínimo común múltiplo entre dos números.
'''

def maximo_comun_divisor_euclides(a, b):
    
    while b:
        a, b = b, a % b
    return a

def minimo_comun_multiplo(a, b):
    return (a * b) // maximo_comun_divisor_euclides(a, b)

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

resultado = minimo_comun_multiplo(num1, num2)
print(f"El MCM de {num1} y {num2} es: {resultado}")
