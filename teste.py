import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dados = pd.read_csv('./caso-1/vmag_caso1_node_832.1.csv', index_col = 0)
dados_barra_0 = dados.iloc[0:3,2:]
dados_barra_1 = dados.iloc[3:6,2:]
dados_barra_2 = dados.iloc[6:9,2:]
dados_barra_3 = dados.iloc[9:12,2:]
dados_barra_4 = dados.iloc[12:15,2:]
dados_barra_5 = dados.iloc[15,2:]
dados_barra_34 = dados.iloc[92:,2:]
dados_transpostos_0 = dados_barra_0.T
dados_transpostos_1 = dados_barra_1.T
plt.plot(dados_transpostos_0)
plt.xlabel("Frequência (Hz)")
plt.ylabel("Impedância (V)")
plt.title("Fonte harmônica no nó 832.1")
plt.show()