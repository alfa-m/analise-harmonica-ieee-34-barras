import pandas as pd
import numpy as np
from procura_arquivos import procura

matrizes_diagonais = procura("matriz_diagonal_complexa*.csv", "./")
lista_de_nos = pd.read_csv("./lista_de_nos.csv", index_col=0)
modos_criticos = pd.DataFrame(columns=["frequência","local","magnitude"])
indice_atual = 0

for matriz in matrizes_diagonais:
    print("Arquivo atual: {}".format(matriz))
    frequencia_atual = matriz.split("_")[-1]
    matriz_diagonal = pd.read_csv("./{}".format(matriz), index_col=0)
    matriz_diagonal = matriz_diagonal.astype(complex)
    matriz_diagonal_inversa = np.linalg.inv(matriz_diagonal)
    matriz_diagonal_inversa_df = pd.DataFrame(matriz_diagonal_inversa)
    matriz_diagonal_inversa_df.index = lista_de_nos.values
    matriz_diagonal_inversa_df.columns = lista_de_nos.values
    matriz_diagonal_inversa_df.to_csv("./inversa_{}".format(matriz))
    valores_diagonais = np.linalg.diagonal(matriz_diagonal_inversa)
    magnitude_valores_diagonais = abs(valores_diagonais)
    valores_maximos = pd.DataFrame(magnitude_valores_diagonais, index=lista_de_nos.values, columns=["autovalores"])
    valores_maximos.to_csv("./z_complexa_modal_caso2_frequencia_{}".format(frequencia_atual))
    valores_maximos_ordenados = valores_maximos.sort_values(by=["autovalores"], ascending=False)
    valores_maximos_ordenados.to_csv("./valores_maximos_ordenados_{}".format(matriz))
    modo_critico = valores_maximos_ordenados.iloc[0,0]
    indice_modo_critico = valores_maximos_ordenados[valores_maximos_ordenados["autovalores"] == modo_critico].index[0][0]
    frequencia_modo_critico = matriz.split("_")[-1].rpartition(".")[0]
    modos_criticos.loc[indice_atual] = frequencia_modo_critico, indice_modo_critico, modo_critico
    indice_atual = indice_atual + 1

modos_criticos.to_csv('./modos_criticos_y_complexa_caso2.csv')
print("Modos críticos encontrados e salvos no arquivo 'modos_criticos_y_complexa_caso2.csv'")
