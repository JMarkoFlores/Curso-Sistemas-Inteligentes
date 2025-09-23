'''
ATRIBUTOS PRIVADOS, HERENCIA (SUPER() PARA LLAMAR METODO Y ATRIBUTO), METODOS CON RETURN
6- Crear la clase Circulo con atributo radio y metodos calcularArea y calcularLongitud. Ademas crear una clase Derivada Cilindro que tenga como atributos radio y altura y permita calcular el Area y calcular el Volumen 
'''
from math import pi
class Circulo:
        def __init__(self, radio=1):
                self.__radio = radio
        
        def getRadio(self):
                return f"Radio: {self.__radio}"
        
        def setRadio(self, radio):
                self.__radio = radio
                return f"Nuevo radio: {self.__radio}"
        
        def calcularArea(self):
                return pi * self.__radio ** 2
        
        def calcularLongitud(self):
                return 2 * pi * self.__radio
        
class Cilindro(Circulo):
        def __init__(self, radio=1, altura=1):
                super().__init__(radio)
                self.__altura = altura

        def getAltura(self):
                return self.__altura
        
        def setAltura(self, altura):
                self.__altura = altura
                return self.__altura

        def calcularArea(self):
                # Area = 2 * PI * r ^ 2  +  2 * PI * r * h
                return 2*super().calcularArea() + super().calcularLongitud()*self.__altura
        
        def calcularVolumen(self):
                # Volumen = PI * r ^ 2 * h
                return super().calcularArea()*self.__altura
        
prueba = Circulo(10)
print("Circulo: ")
print(f"Área: {prueba.calcularArea()}")         #314,15
print(f"Perímetro: {prueba.calcularLongitud()}")      #62,28      
print("Cilindro: ")
prueba2 = Cilindro(1, 1)                       
print(f"Área: {prueba2.calcularArea()}")        #12,56
print(f"Volume: {prueba2.calcularVolumen()}")   #3,14