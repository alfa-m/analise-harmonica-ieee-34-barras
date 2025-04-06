import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dados = pd.read_csv('./vmag_caso1_node_802.1.csv', index_col = 0)
dados_transpostos = dados.T
harmonicos = np.arange(60,3000.5,0.5)
plt.plot(harmonicos, dados_transpostos)
plt.xlabel("Frequência (Hz)")
plt.xlim(0,3000)
plt.ylabel("Tensão (V)")
plt.ylim(0,45000)
plt.title("Fonte harmônica no nó 802.1")
plt.grid()
plt.savefig("./vmag_caso1_no_802_total_com_eixo.png")
plt.show()
plt.close()

dados_transpostos.plot()
plt.xlabel("Frequência (Hz)")
plt.ylabel("Tensão (V)")
plt.title("Fonte harmônica no nó 802.1")
plt.grid()
plt.savefig("./vmag_caso1_no_802_total_sem_eixo.png")
plt.show()
plt.close()
