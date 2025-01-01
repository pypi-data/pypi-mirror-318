import pandas as pd

def filtrar_dados(df, coluna, valor):
    """
    Filtra o DataFrame com base em uma coluna e um valor.
    """
    return df[df[coluna] == valor]

def calcular_media(df, coluna):
    """
    Calcula a média de uma coluna numérica.
    """
    return df[coluna].mean()
