'''
ATRIBUTOS PRIVADOS
3)Crear una clase circulo con atributo privado radio y calcule el area y la longitud de la circunferencia.
'''

from math import pi
class Circulo:
        #aver cual es la diferencia de hacer self.radio y self.__radio
        def __init__(self, r ):
                self.__radio = r
        
        def getRadio(self):
                return f"Radio: {self.__radio}"
        
        def setRadio(self, rad):
                self.__radio = rad
                return self.__radio
        
        def calcularArea(self):
                area = pi * self.__radio ** 2
                return area
        
        def calcularLongitud(self):
                perimetro = 2 * pi * self.__radio
                return perimetro
        
        def __str__(self):
                cad1 = f"Circulo \nÁrea: {self.calcularArea()} \nPerímetro: {self.calcularLongitud()}"
                return cad1
        
prueba = Circulo(1)
prueba.setRadio(10)
print(prueba.getRadio())
print(prueba.calcularLongitud())
print(prueba.calcularArea())
print(prueba)

'''
Consideraciones:
1)Como en el constructor se tiene un valor de radio por defecto, entonces cuando si se puede hacer Circulo() y despues setRadio(). Ahora si no tuviera eso, tendrias que hacer "prueba = Circulo(x)".
2)Cuando el atributo es privado para cambiarlo es apenas con set(). Si es publico: prueba.radio = xxx
'''