'''
Ejercicio 1: Clase Estudiante con estadísticas de notas 
• Crea una clase Estudiante con atributos: nombre, lista de notas. 
• Implementa métodos para: 
        o calcular el promedio (usando numpy.mean) 
        o detectar la nota máxima y mínima 
• Implementa manejo de excepciones si la lista de notas está vacía. 
• Genera un gráfico con matplotlib mostrando la distribución de las notas del 
estudiante. 
'''
from numpy import mean
from matplotlib import pyplot as plt
import validaciones as v

class Estudiante:
        def __init__(self):
                self.__nombre = self.ingreseNombre()
                self.__listaNotas = []
        
        def ingreseNombre(self):
                return input("Ingrese nombre: ")
        
        def setNombre(self, nombre):
                self.__nombre=nombre
        
        def getNombre(self):
                return self.__nombre
        
        def ingresoNotas(self):
                print(f"\nEstudiante: {self.__nombre}")
                n = v.validacionesInt("Ingrese la cantidad de notas: ")
                #n = validacionesCantidad("Ingrese la cantidad de notas: ")
                for i in range(n):
                        nota = v.validacionesFloat(f"Nota {i + 1}: ")
                        #nota = validacionesNotas(f"Nota {i + 1}: ")
                        self.__listaNotas.append(nota)
                return self.__listaNotas
        
        def promedio(self):
                try:
                        if not self.__listaNotas:  
                                raise ValueError("No hay notas registradas para calcular el promedio")
                        return mean(self.__listaNotas)
                except Exception as e:
                        print(f"Error al calcular promedio: {e}")
                        return None
        
        def mayorNota(self):
                try:
                        if not self.__listaNotas:
                                raise ValueError("No hay notas registradas")
                        return max(self.__listaNotas)
                except Exception as e:
                        print(f"Error al encontrar nota máxima: {e}")
                        return None

        
        def menorNota(self):
                try:
                        if not self.__listaNotas:
                                raise ValueError("No hay notas registradas")
                        return min(self.__listaNotas)
                except Exception as e:
                        print(f"Error al encontrar nota máxima: {e}")
                        return None

        def crearGrafica(self):
                if not self.__listaNotas:
                        raise ValueError("No hay notas para graficar")
                
                nominaciones =[]
                for i in range(len(self.__listaNotas)):
                        nominaciones.append(f"Nota {i + 1}")
                #print(nominaciones)

                plt.figure(figsize=(8,5), dpi=70)

                plt.plot(nominaciones, self.__listaNotas, label = "Notas", marker = 'o', color = "blue", markersize=10)
                plt.title("Grafico de notas", fontweight="bold")
                plt.xlabel("Eje X")
                plt.ylabel("Eje Y")
                plt.legend()            
                plt.grid(True) 
                plt.show()

prueba = Estudiante()
print(f"Lista de notas: {prueba.ingresoNotas()}")
print(f"\nPromedio de las notas: {prueba.promedio()}")
print(f"\nNota máxima: {prueba.mayorNota()}")
print(f"Nota minima: {prueba.menorNota()}")
prueba.crearGrafica()