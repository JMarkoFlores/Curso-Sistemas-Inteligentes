from matplotlib import pyplot as plt

categorias = ['A', 'B', 'C', 'D', 'E']
valores = [4, 7, 1, 5, 8]

plt.figure(figsize=(8,5), dpi=70)

#Crear gráfico de barras
plt.bar(categorias, valores, color = 'blue', alpha=0.7)

for i, valor in enumerate(valores):
        plt.hlines(y=valor, xmin=i-0.4, xmax=i+0.4, colors='red', linestyles='--')

#Personlaización opcional
plt.title("Gráfico de barras")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()