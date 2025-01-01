import matplotlib.pyplot as plt

def plotar_histograma(df, coluna, bins=10):
    """
    Plota um histograma para uma coluna numérica.
    """
    plt.hist(df[coluna], bins=bins, alpha=0.7, color='blue')
    plt.title(f'Histograma de {coluna}')
    plt.xlabel(coluna)
    plt.ylabel('Frequência')
    plt.show()

def plotar_dispersao(df, x_coluna, y_coluna):
    """
    Plota um gráfico de dispersão entre duas colunas.
    """
    plt.scatter(df[x_coluna], df[y_coluna], alpha=0.7, color='green')
    plt.title(f'Dispersão: {x_coluna} x {y_coluna}')
    plt.xlabel(x_coluna)
    plt.ylabel(y_coluna)
    plt.show()
