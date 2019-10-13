import matplotlib.pyplot as plt

#valores das barras
x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 0]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]

#titulo do gráfico
titulo = "comparando gráfico de barras"

#eixos
eixox = "Eixo X"
eixoy = "Eixo Y"

#legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)


plt.bar(x1, y1, label = "Grupo 1")
plt.bar(x2, y2, label = "Grupo 2")
plt.legend()
plt.show()