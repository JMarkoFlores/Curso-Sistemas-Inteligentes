from matplotlib import pyplot as plt

notas = [18, 10, 16, 14, 12, 18, 20, 15, 16, 17, 10, 12]

plt.figure(figsize=(8,5), dpi=70)

plt.hist(notas, bins=5, color = "blue",edgecolor="black", alpha=0.7)
plt.title("Distribución de Notas", fontweight="bold")
plt.xlabel("Rango de notas")
plt.ylabel("Frecuencia")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.show()