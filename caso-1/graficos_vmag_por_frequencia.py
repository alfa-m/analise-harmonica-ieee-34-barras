import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dados = pd.read_csv('./vmag_caso1_node_832.1.csv', index_col = 0)
dados_sem_harmonico_1 = dados.iloc[:,2:]
dados_transpostos = dados_sem_harmonico_1.T
dados_transpostos.plot()
plt.xlabel("Frequência (Hz)")
plt.ylabel("Impedância (V)")
plt.title("Fonte harmônica no nó 832.1")
plt.show()
