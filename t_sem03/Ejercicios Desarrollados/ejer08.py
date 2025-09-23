'''
'''
import matplotlib.pyplot as plt

x = [1, 2, 3,4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 2, 1, 2, 1]

plt.figure(figsize=(8,5), dpi=70)

#Crear el grafico de lienas
plt.plot(x, y1, label = "Serie A", marker = 'o', color = "blue", markersize=10)
plt.plot(x, y2, label = "Serie B", linestyle = '--' ,marker = 'x', color = "red", markersize=10)

#Personalizar el grafico
plt.title("Grafico de lineas", fontweight="bold")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()            #Mostrar leyenda (serie A y serie B)
plt.grid(True)          #Activar grillas de fondo


#mostrar el gráfico
plt.show()