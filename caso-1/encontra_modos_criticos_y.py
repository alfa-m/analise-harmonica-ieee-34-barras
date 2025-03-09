import pandas as pd
import numpy as np
from procura_arquivos import procura

matrizes_diagonais = procura("matriz_diagonal_real*.csv", "./")
lista_de_nos = pd.read_csv("./lista_de_nos.csv", index_col=0)
lista_de_nos = lista_de_nos.reset_index(drop=True)
lista_de_nos_numpy = lista_de_nos.to_numpy()
modos_criticos = pd.DataFrame(columns=["local","magnitude"])

for matriz in matrizes_diagonais:
    matriz_diagonal = pd.read_csv("./{}".format(matriz), index_col=0)
    matriz_diagonal_inversa = np.linalg.inv(matriz_diagonal)
    matriz_diagonal_inversa_df = pd.DataFrame(matriz_diagonal_inversa)
    matriz_diagonal_inversa_df.index = lista_de_nos
    matriz_diagonal_inversa_df.columns = lista_de_nos
    matriz_diagonal_inversa_df.to_csv("./inversa_{}".format(matriz))
    valores_diagonais = np.linalg.diagonal(matriz_diagonal_inversa)
    valores_maximos = pd.DataFrame(valores_diagonais, index=lista_de_nos, columns=["autovalores"])
    valores_maximos_ordenados = valores_maximos.sort_values(by=["autovalores"], ascending=False)
    valores_maximos_ordenados.to_csv("./valores_maximos_ordenados_{}".format(matriz))
    modo_critico = valores_maximos_ordenados.iloc[0,0]
    indice_modo_critico = valores_maximos_ordenados[valores_maximos_ordenados["autovalores"] == modo_critico].index[0]
    modos_criticos.loc[matriz] = indice_modo_critico, modo_critico

modos_criticos.to_csv('./modos_criticos_y.csv')
print("Modos críticos encontrados e salvos no arquivo 'modos_criticos_y.csv'")
