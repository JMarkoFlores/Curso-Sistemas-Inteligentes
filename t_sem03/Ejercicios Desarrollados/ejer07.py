'''
ATRIBUTOS PRIVADOS, CLASE ABSCTRACTA(ABC, absctractmethod -> pass), CONSTRUCTOR CON SUPER
7- Crear la clase abstracta Empleado con atributos codigo, apellidos y nombre y un metodo abstracto calcularSueldo.  
Crear las clases derivadas: 
EmpleadoPorHora: con atributos adicionales precioHora y horasTrabajadas 
EmpleadoPorComsion : con atributos adicionales salarioBase, montoVentas y porcentajeComision. 
'''

from abc import ABC, abstractmethod

class Empleado(ABC):
        def __init__(self, codigo, apellidos, nombres):
                self.__codigo = codigo
                self.__apellidos = apellidos
                self.__nombres = nombres
                
        @abstractmethod
        def calcularSueldo(self):
                pass

class EmpleadoPorHora(Empleado):
        def __init__(self, codigo, apellidos, nombres, precioHora, horasTrabajadas):
                super().__init__(codigo, apellidos, nombres)
                self.__precioHora = precioHora
                self.__horasTrabajadas = horasTrabajadas
                
        def calcularSueldo(self):
                return self.__precioHora * self.__horasTrabajadas
        
class EmpleadoPorComision(Empleado):
        def __init__(self, codigo, apellidos, nombres, salarioBase, montoVentas, porcentajeComision):
                super().__init__(codigo, apellidos, nombres)
                self.__salarioBase = salarioBase
                self.__montoVentas = montoVentas
                self.__porcentajeComision = porcentajeComision
        
        def calcularSueldo(self):
                return self.__salarioBase + self.__montoVentas * self.__porcentajeComision
        
empleado1 = EmpleadoPorHora('001', 'Flores', 'Jean', 10, 10)
print(f"El sueldo: {empleado1.calcularSueldo()}")
empleado2 = EmpleadoPorComision('002', 'Pacheco', 'Marko', 100, 1000, 0.1)
print(f"El sueldo: {empleado2.calcularSueldo()}")
'''
Consideraciones en clases abstractas:
0)La clase Empleado es una clase abstracta porque hereda de ABC.
1)No puedes crear objetos directamente de Empleado.
2)Solo sirve como molde/base para otras clases.
3)Si tiene métodos marcados con @abstractmethod, las clases hijas están obligadas a implementarlos.
4)abstractmethod → decorador que marca métodos que deben ser implementados obligatoriamente en las clases hijas.
'''