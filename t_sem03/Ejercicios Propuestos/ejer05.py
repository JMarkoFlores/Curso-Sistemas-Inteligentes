'''
Ejercicio 5:  Análisis de datos climáticos 
• Diseña una clase Clima que lea un archivo CSV con datos diarios de temperatura y humedad (usando pandas). 
• Implementa métodos para: 
o calcular la temperatura media y la desviación estándar (con numpy), 
o detectar valores atípicos (outliers). 
• Maneja excepciones si el archivo no existe o tiene datos corruptos. 
• Grafica las temperaturas en el tiempo con matplotlib.
'''

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

class Clima:
        def __init__(self, archivo_csv=None):
                self.archivo_csv = archivo_csv
                self.datoslectura = None

        def leerCSV(self):
                try:
                        self.datoslectura = pd.read_csv(self.archivo_csv)
                        if not {"Fecha", "Temperatura", "Humedad"}.issubset(self.datoslectura.columns):
                                raise ValueError("El archivo no contiene las columnas necesarias: Fecha, Temperatura, Humedad")
                        print(self.datoslectura.to_string(index=False)) 
                except FileNotFoundError as e:
                        print(f"Error: No existe el archivo CSV: ' {self.archivo_csv} ' ")
                except ValueError as e:
                        print(f"Error: {e}")
                except Exception as e:
                        print(f"Ocurrió un error inesperado: {e}")
                        
        def calculosTemperaturaMedia(self):
                temperaturas = self.datoslectura["Temperatura"].to_numpy()
                media = np.mean(temperaturas)
                desviacion = np.std(temperaturas)
                return media, desviacion
        
        def detectarOutliers(self):
                """Detecta valores atípicos usando el método IQR"""
                try:
                        if self.datoslectura is None:
                                print("Error: Primero debe leer el archivo CSV")
                                return
                        
                        temperaturas = self.datoslectura["Temperatura"]
                        
                        # Método IQR (Rango Intercuartílico)
                        Q1 = np.percentile(temperaturas, 25)
                        Q3 = np.percentile(temperaturas, 75)
                        IQR = Q3 - Q1
                        
                        limite_inferior = Q1 - 1.5 * IQR
                        limite_superior = Q3 + 1.5 * IQR
                        
                        outliers = temperaturas[(temperaturas < limite_inferior) | (temperaturas > limite_superior)]
                        
                        if len(outliers) > 0:
                                print(f"\nOutliers detectados: {len(outliers)} valores")
                                print(f"Valores atípicos: {outliers.tolist()}")
                        else:
                                print("\nNo se detectaron outliers en los datos")
                        return outliers
                        
                except Exception as e:
                        print(f"Error al detectar outliers: {e}")
        
        
        def graficar(self):
                try:
                        fechas = self.datoslectura["Fecha"].tolist()
                        temperaturas = self.datoslectura["Temperatura"].tolist()
                        
                        plt.figure(figsize=(8,5), dpi=70)

                        plt.bar(fechas, temperaturas, color = 'blue', alpha=0.7)
                        # plt.plot(fechas, temperaturas, marker="o", linestyle="-", color="b", label="Temperatura")
                        
                        plt.title("Gráfico de las temperaturas en el tiempo")
                        plt.xlabel("Tiempo")
                        plt.ylabel("Temperaturas")
                        plt.show()
                        
                        return fechas, temperaturas
                except Exception:
                        print(f"Error: {Exception}")

#Pone la ruta donde está el archivo CSV
prueba = Clima("C:\\Users\\jeanm\\Desktop\\Python\\Ejercicios\\Ejercicios-Martes\\Testeo-Ejer05.csv")
prueba.leerCSV()
media, desviacion = prueba.calculosTemperaturaMedia()
print(f"\nMedia: {media}\nDesviación:{desviacion}")
prueba.detectarOutliers()
print("\nDatos a graficar: ")
fechas, temperaturas = prueba.graficar()
print(f"Fechas: {fechas}\nTemperaturas: {temperaturas}")
