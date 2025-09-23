'''
Ejercicio 2:  Manejo de datos con pandas 
• Diseña una clase Curso que contenga una lista de estudiantes. 
• Implementa un método que exporte la información de los estudiantes (nombre y 
promedio) a un DataFrame de pandas. 
• Añade un método que lea el DataFrame y grafique un histograma de promedios 
usando matplotlib. 
• Controla con excepciones si se intenta leer un DataFrame vacío. 
'''
import validaciones as v
from matplotlib import pyplot as plt
import pandas as pd

class Curso:
        def __init__(self):
                self.__lista = []
                
        def ingresoDatos(self):
                n = v.validacionesInt("Ingrese la cantidad de estudiantes: ")
                for i in range(n):
                        print(f"\nDatos del Estudiante {i + 1}")
                        nombre = input("Nombre: ")
                        promedio = v.validacionesFloat("Promedio: ")
                        alumno = (nombre, promedio)
                        self.__lista.append(alumno)
                return self.__lista
                
        def exportDataToDataFrame(self):
                if not self.__lista:  
                        raise ValueError("No hay datos de estudiantes para exportar")
                
                df = pd.DataFrame(self.__lista, columns=["Nombre", "Promedio"])
                return df
        
        def readDataFrameAndCreateGrafiph(self):
                try:
                        #La excepcion si se intenta leer un DataFrame vacío
                        df = self.exportDataToDataFrame()
                        print("\n LISTA DE ESTUDIANTES")
                        print(df.to_string(index=False))
                except ValueError as e:
                        print(f"Error: {e}")
                except Exception as e:
                        print(f"Ocurrió un error inesperado: {e}")

                plt.figure(figsize=(8,5), dpi=70)

                plt.hist(df["Promedio"], bins=5, color = "blue",edgecolor="black", alpha=0.7)
                # plt.plot(df["Nombre"], df["Promedio"], label = "Notas", marker = 'o', color = "blue", markersize=10)
                plt.title("Histograma - Distribución de notas", fontweight="bold")
                plt.xlabel("Rango de promedios")
                plt.ylabel("Frecuencia")
                #plt.legend()            
                plt.grid(True) 
                plt.show()


prueba = Curso()
print(prueba.ingresoDatos())
prueba.readDataFrameAndCreateGrafiph()