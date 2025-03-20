import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dados = pd.read_csv('./vmag_caso1_node_832.1.csv', index_col = 0)
dados_sem_harmonico_1 = dados.iloc[:,2:]
dados_transpostos = dados_sem_harmonico_1.T
harmonicos = np.arange(61,3000.5,0.5)
plt.plot(harmonicos, dados_transpostos)
plt.xlabel("Frequência (Hz)")
plt.xlim(0,3000)
plt.ylabel("Impedância (V)")
plt.ylim(0,1000)
plt.title("Fonte harmônica no nó 832.1")
plt.grid()
plt.savefig("./vmag_caso1_no_832_sem_harmonico_1_com_eixo.png")
plt.show()
plt.close()

dados_transpostos.plot()
plt.xlabel("Frequência (Hz)")
plt.ylabel("Impedância (V)")
plt.title("Fonte harmônica no nó 832.1")
plt.grid()
plt.savefig("./vmag_caso1_no_832_sem_harmonico_1_sem_eixo.png")
plt.show()
plt.close()
