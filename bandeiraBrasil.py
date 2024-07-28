import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patch

fig, ax = plt.subplots(figsize=(10, 6), dpi=150)

# Retângulo verde
retangulo = patch.Rectangle((0, 0), width=20, height=14, facecolor='green', zorder=0)
ax.add_patch(retangulo)

# Losango amarelo
ax.fill([10, 18.3, 10, 1.7], [1.7, 7, 12.3, 7], color='yellow')

# Círculo azul
circulo = patch.Circle((10, 7), radius=3.5, facecolor='blue', zorder=1)
ax.add_patch(circulo)

# Funções para a faixa central branca
def y(x):
    raiz2 = 2**0.5
    raiz = (-125_000*x**2 + 1_802_000*x + 8_000_217)**0.5
    return (2*raiz2*raiz-2913)/1000

def y2(x):
    raiz = 8*(-15_625*x**2 + 225_250*x + 1_219_449)**0.5
    return (raiz-2_913)/1000

x = np.arange(6.55, 13.55, 0.1)  # limites da faixa
y_x = y(x)
y2_x = y2(x)
ax.plot(x, y_x, c='w', zorder=2)
ax.plot(x, y2_x, c='w', zorder=2)
ax.fill_between(x, y_x, y2_x, color='w', zorder=2)  # preenche entre topo e base na cor branca

# Arco amarelo
arco = patch.Arc((10, 7), 7.5, 7.5, lw=10, color='yellow', alpha=1, zorder=3)
ax.add_patch(arco)

# Texto da faixa central
texto = 'ORDEM E PROGRESSO amanda'
xvals = np.linspace(x[5], x[65], len(texto)+1)
yvals = y(xvals)
angulos = np.rad2deg(np.arctan((yvals[1:]-yvals[:-1])/(xvals[1:]-xvals[:-1])))  # ângulos das letras

# Exibe cada letra da frase em sua devida posição
for counter in range(len(xvals) - 1):
    xcoord = (xvals[counter] + xvals[counter + 1]) / 2
    ycoord = (yvals[counter] + yvals[counter + 1]) / 2
    ax.text(xcoord, ycoord + 0.25, texto[counter], fontweight='bold',
            fontsize=10, rotation=angulos[counter], color='g',
            horizontalalignment='center', verticalalignment='center')

# Estrelas da bandeira
n = 8  # tamanho de referência
estrelas = [
    (11, 8.2, n / 1),
    (10.6, 7, n / 3),
    (7, 7.5, n / 1),
    (8.7, 6.5, n / 2),
    (7.7, 6, n / 4),
    (7.5, 5.7, n / 1),
    (7.2, 5.4, n / 2),
    (8, 5.4, n / 2),
    (7.8, 5.2, n / 3),
    (8.6, 5, n / 1),
    (10, 6, n / 2),
    (9.6, 5.6, n / 3),
    (9.8, 5.4, n / 4),
    (10.4, 5.6, n / 2),
    (10, 5, n / 1),
    (10, 4, n / 5),
    (10.6, 4.7, n / 3),
    (10.8, 4.4, n / 2),
    (11, 4.7, n / 3),
    (11.5, 4, n / 3),
    (11.5, 4.4, n / 2),
    (11.5, 4.8, n / 3),
    (11.8, 4.8, n / 3),
    (12.1, 5.1, n / 2),
    (12.4, 5.4, n / 2),
    (12.8, 5.8, n / 2),
    (12.4, 5.8, n / 1)
]

for estrela in estrelas:
    plt.plot(estrela[0], estrela[1], 'w*', ms=estrela[2])

plt.axis('equal')
plt.show()
