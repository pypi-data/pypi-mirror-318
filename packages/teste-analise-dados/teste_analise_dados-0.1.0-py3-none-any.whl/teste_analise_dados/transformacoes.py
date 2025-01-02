import pandas as pd

def filtrar_dados(df, coluna, valor):
    return df[df[coluna] == valor]

def calcular_media(df, coluna):
    return df[coluna].mean()