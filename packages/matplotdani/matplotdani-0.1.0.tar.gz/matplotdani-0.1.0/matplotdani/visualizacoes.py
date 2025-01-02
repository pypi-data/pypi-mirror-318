import matplotlib.pyplot as plt

def plotar_histograma(df, coluna):
    df[coluna].plot(kind='hist')
    plt.title(f"Histograma da coluna {coluna}")
    plt.show()