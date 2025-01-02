import matplotlib.pyplot as plt

def plotar_histograma(df, coluna, bins=10):
    df[coluna].plot(kind='hist', bins=bins)
    plt.title(f'Histograma da coluna {coluna}')
    plt.show()
    
def plotar_dispersao(df, x_coluna, y_coluna):
    df.plot(x=x_coluna, y=y_coluna, kind='scatter')
    plt.title(f'Dispersão entre {x_coluna} e {y_coluna}')
    plt.show()