'''
Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
'''

class Persona:
    
    def __init__(self, nombre="", edad=0, DNI=0):
        self.__nombre = nombre
        self.__edad = edad
        self.__DNI = DNI

    # Getters

    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    def get_DNI(self):
        return self.__DNI
    
    # Setters

    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print("La edad debe ser un valor positivo.")

    def set_DNI(self, DNI):
        if len(DNI) == 8:  
            self.__DNI = DNI
        else:
            print("El DNI debe tener 8 caracteres.")

    def mostrar(self):
        return self.__nombre, self.__edad, self.__DNI
    
    def es_mayor_de_edad(self):
        if self.__edad >= 18:
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")

persona1 = Persona("Juan B. Justo", 38, 12345678)
print(persona1.get_DNI())
print(persona1.get_edad())
persona1.set_edad(40)
print(persona1.get_edad())
print(persona1.mostrar())
print(persona1.es_mayor_de_edad())