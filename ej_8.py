'''
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la clase creada en el punto 7. 
Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. 
Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, 
por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
mayor de edad pero menor de 25 años y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta
'''

class CuentaJoven():

    def __init__(self, titular="",edad=0, cantidad=0.0, bonificacion=0):
        self.__titular = titular
        self.__edad = edad
        self.__cantidad = cantidad
        self.__bonificacion = bonificacion

    # Getter

    def get_titular(self):
        return self.__titular
    
    def get_cantidad(self):
        return self.__cantidad

    def get_bonificacion(self):
        bonificado = self.__cantidad-(self.__cantidad*(self.__bonificacion/100))
        return bonificado
    
    def get_bonificacion_en_porcentaje(self):
        return self.__bonificacion
    
    # Setter

    def set_titular(self, titular):
        self.__titular = titular

    def set_bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    # Verificar si el tituar es valido

    def es_titular_valido(self):
        if self.__edad >= 18 and self.__edad < 25:
            print("Es mayor de edad y tiene menos de 25")
        else:
            print("No se encuentra en el rango etario adecuado")

    # Ingresar y Retirar Dinero        
    
    def ingresar(self, cantidad):
        if cantidad >= 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        if self.es_titular_valido == True:
            self.__cantidad -= cantidad
        else:
            print("El titular no puede modificar esta cuenta")

    # Mostrar
    
    def mostrar(self):
        print("Cuenta Joven:")
        print(f"Con la bonificacion del {self.get_bonificacion_en_porcentaje()}% el saldo de su cuenta quedaria en {self.get_bonificacion()}")
        return self.__titular, self.__cantidad
    
# Pruebas

titular1 = CuentaJoven("Esteban Quito",18,555.5,10)
print(titular1.es_titular_valido())
print(titular1.get_bonificacion())
print(titular1.mostrar())





                
    