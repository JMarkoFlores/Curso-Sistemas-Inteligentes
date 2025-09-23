'''
Ejercicio 3: Simulación de dados con numpy 
• Crea una clase SimuladorDados que permita lanzar N dados de 6 caras (usando numpy.random.randint). 
• Implementa métodos para calcular la media, varianza y distribución de frecuencias de los resultados. 
• Maneja excepciones si N ≤ 0. 
• Grafica la distribución de frecuencias con matplotlib. 
'''
import validaciones as v
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

class SimuladorDatos:
        def __init__(self):
                #Las excepciones están en validaciones
                self.__dados = v.validacionesInt("Cuandos dados deseas lanzar: ")
                self.__valores = None
                
        def lanzarDados(self):
                self.__valores = np.random.randint(1, 7, size=self.__dados)
                print(self.__valores)
                return self.__valores
        
        def calcularMedia(self):
                return np.mean(self.__valores)
                
        def calcularVarianza(self):
                return np.var(self.__valores)
        
        def calcularDistribuicionDeFrecuencias(self):
                return pd.Series(self.__valores).value_counts().sort_index()
        
        def graficar(self):
                numeros = self.calcularDistribuicionDeFrecuencias().index.tolist()
                counts = self.calcularDistribuicionDeFrecuencias().values.tolist()
                
                plt.figure(figsize=(8,5), dpi=70)

                plt.bar(numeros, counts, color = 'blue', alpha=0.7)

                plt.title("Gráfico de barras")
                plt.xlabel("Caras de los lados")
                plt.ylabel("Frecuencias")
                plt.show()
                
prueba = SimuladorDatos()
prueba.lanzarDados()
print(f"Media: {prueba.calcularMedia()}")
print(f"Varianza: {prueba.calcularVarianza()}")
print(f"Distribuición de Frecuencia:\n{prueba.calcularDistribuicionDeFrecuencias()}")
prueba.graficar()