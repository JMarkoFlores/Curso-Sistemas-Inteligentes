'''
ATRIBUTOS PUBLICOS
1) Crear una clase Rectangulo con atributos lado1,lado2 y metodos para calcular el area y el perimetro. 
'''
class Rectangulo:
        def __init__(self, l1 = 1, l2 = 2):
                self.lado1 = l1
                self.lado2= l2
        
        #Se puede hacer que retorne el valor calculado y que afuera pongas el print()
        def calcularArea (self):
                area = self.lado1 * self.lado2
                print(f"Área: {area}")
                
        def calcularPerimetro (self):
                perimetro = 2 * (self.lado1 + self.lado2)
                print(f"Perímetro: {perimetro}")
        
        def __str__(self):
                return f"Retangulo de lados: {self.lado1} y {self.lado2}"

        def __repr__(self):
                return f"Rectangulo(l1={self.lado1}, l2={self.lado2})"
        
prueba = Rectangulo(2, 3)
prueba.calcularArea()
prueba.calcularPerimetro()
print(prueba)
print(repr(prueba))
'''
Consideraciones:
1)print("hola") -> muestra hola y devuelve None.
2)def __str__(self): debe return "..." una cadena, no print.
3)Usa return cuando una función/método debe dar un valor; usa print solo para mostrarlo.
4)Si quieres tanto el valor como imprimirlo, haz que el método devuelva el valor y luego imprime desde fuera. Entonces manejar asociados return y print 
'''