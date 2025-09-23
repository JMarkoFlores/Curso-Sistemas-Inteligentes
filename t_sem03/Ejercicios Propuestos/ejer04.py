'''
Ejercicio 4: Análisis de ventas 
• Crea una clase Tienda con un método para registrar ventas en un DataFrame de pandas (producto, cantidad, precio). 
• Implementa métodos para calcular: 
o total vendido, 
o producto más vendido, 
o promedio de ventas por transacción (usando numpy). 
• Controla errores si se intenta operar sobre una tienda sin ventas. 
• Genera un gráfico de barras con matplotlib mostrando ventas por producto. 
'''
import validaciones as v
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

class Tienda:
#Me dio a entender que solo requiere DataFrame para desarrollar el ejercicio
        def __init__(self):
                self.__cantidad = v.validacionesInt("Ingrese cantidad de ventas: ")
                self.__ventas = pd.DataFrame(columns=["Producto", "Cantidad", "Precio"])

        def registrarVenta(self):
                for i in range(self.__cantidad):
                        print(f"\nVENTA Nº {i + 1}")
                        producto = input("Producto: ")
                        cantidad = v.validacionesInt("Cantidad: ")
                        precio = v.validacionesFloat("Precio: ")
                        nuevaFila = pd.DataFrame(
                                {"Producto": [producto], "Cantidad": [cantidad], "Precio": [precio]}
                        )
                        self.__ventas.loc[len(self.__ventas)] = [producto, cantidad, precio]
                print(f"\n{self.__ventas.to_string(index=False)}")
        
        def totalVendido(self):
                if self.__ventas.empty:
                        print("No hay ventas registradas.\nTotal de ventas: 0.0")
                        return None
                self.__ventas["Total"] = self.__ventas["Cantidad"] * self.__ventas["Precio"]
                total_general = self.__ventas["Total"].sum()
                #print(self.__ventas.to_string(index=False)) 
                return total_general
        
        def productoMasVendido(self):
                if self.__ventas.empty:
                        print("No hay ventas registradas.")
                        return None
                
                agrupado = self.__ventas.groupby("Producto")["Cantidad"].sum()
                producto_max = agrupado.idxmax()
                cantidad_max = agrupado.max()
                return producto_max, cantidad_max

        def promedioTransacciones(self):
                if self.__ventas.empty:
                        print("No hay ventas registradas.")
                        return None

                montos = self.__ventas["Cantidad"] * self.__ventas["Precio"]
                promedio = np.mean(montos)
                return promedio
        
        def graficaVentaPorProducto(self):
                if self.__ventas.empty:
                        print("No hay ventas registradas.")
                        return None

                ventas_por_producto = self.__ventas.groupby("Producto")["Cantidad"].sum()
                productos = ventas_por_producto.index.tolist()
                cantidades = ventas_por_producto.values.tolist()
                plt.figure(figsize=(8,5), dpi=70)

                plt.bar(productos, cantidades, color = 'blue', alpha=0.7)

                plt.title("Gráfico de venta por producto")
                plt.xlabel("Producto")
                plt.ylabel("Cantidades")
                plt.show()

prueba = Tienda()
prueba.registrarVenta()
prueba.totalVendido()
print(f"\nTOTAL VENDIDO:{prueba.totalVendido()}")
producto_max, cantidad_max = prueba.productoMasVendido()
print(f"\nPRODUCTO MÁS VENDIDO: {producto_max} -> Cantidad: {cantidad_max}")
print(f"Promedio de ventas por transacción: {prueba.promedioTransacciones()}")
prueba.graficaVentaPorProducto()
'''
Consideraciones:
1)Si en el metodo registrarVenta() utilizas "self.__ventas = pd.concat([self.__ventas, nuevaFila], ignore_index=True)" aparece warning, pero no es un error. Para evitar ese warning se emplea "loc"
'''