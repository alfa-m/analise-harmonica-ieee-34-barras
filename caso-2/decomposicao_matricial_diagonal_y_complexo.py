import pandas as pd
import numpy as np
from procura_arquivos import procura

lista_de_matrizes_y = procura("complexa_y*.csv", './')

for matriz_y in lista_de_matrizes_y:
    print("Arquivo atual: {}".format(matriz_y))
    caminho = "./{}".format(matriz_y)
    matriz_y_df = pd.read_csv(caminho, index_col=0)
    matriz_y_complexa = matriz_y_df.astype(complex)
    autovalores_matriz_y, autovetores_matriz_y = np.linalg.eig(matriz_y_complexa)
    #magnitude_matriz_y_complexa = abs(matriz_y_complexa)
    #autovalores_matriz_y, autovetores_matriz_y = np.linalg.eig(magnitude_matriz_y_complexa)
    matriz_y_diagonal = np.diag(autovalores_matriz_y)
    matriz_y_diagonal_df = pd.DataFrame(matriz_y_diagonal)
    matriz_y_diagonal_df.to_csv("./matriz_diagonal_{}".format(matriz_y))
    autovetores_matriz_y_df = pd.DataFrame(autovetores_matriz_y)
    autovetores_matriz_y_df.to_csv("./autovetores_{}".format(matriz_y))

print("Matrizes Y complexas decompostas diagonalmente e matrizes de autovetores obtidas")
