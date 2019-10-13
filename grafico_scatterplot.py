import matplotlib.pyplot as plt

#valores das barras
x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]

#tamanho dos pontos
z = [200, 250, 400, 3000, 100]

#titulo do gráfico
titulo = "Scatterplot: Gráfico de dispersão"

#eixos
eixox = "Eixo X"
eixoy = "Eixo Y"

#legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#ligando os pontos do gráfico
plt.plot(x, y, color="#000000", linestyle="--")

#pontos do gráfico
plt.scatter(x, y, label="Meus pontos", color="k", marker=".", s = z)

plt.legend()

#mostra o gráfico
#plt.show()

#salva o grafico
plt.savefig("scatterplot.png", dpi=300)

