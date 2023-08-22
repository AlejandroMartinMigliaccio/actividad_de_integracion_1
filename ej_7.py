'''
Crea una clase llamada Cuenta que tendrá los siguientes atributos: 
titular (que es una persona) y cantidad (puede tener decimales). 
El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase: 
 Un constructor, donde los datos pueden estar vacíos. 
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero. 
 mostrar(): Muestra los datos de la cuenta. 
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada. 
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos. 
'''

class Cuenta():

    def __init__(self, titular="", cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad

    # Getter

    def get_titular(self):
        return self.__titular
    
    def get_cantidad(self):
        return self.__cantidad
    
    # Setter

    def set_titular(self, titular):
        self.__titular = titular

    

    def mostrar(self):
        return self.__titular, self.__cantidad
    
    def ingresar(self, cantidad):
        if cantidad >= 0:
            self.__cantidad += cantidad

    def retirar(self,cantidad):
        self.__cantidad -= cantidad

titular1 = Cuenta("Lola Mento", 150.5)
print(titular1.mostrar())
titular1.ingresar(150.3)
print(titular1.mostrar())
titular1.retirar(300.0)
print(titular1.mostrar())

