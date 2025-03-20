import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dados = pd.read_csv('./vmag_node_832.1.csv', index_col = 0)
dados_transpostos = dados.T
harmonicos = np.arange(60,3000.5,0.5)
plt.plot(harmonicos, dados_transpostos)
plt.xlabel("Frequência (Hz)")
plt.xlim(0,3000)
plt.ylabel("Impedância (V)")
plt.ylim(0,45000)
plt.title("Fonte harmônica no nó 832.1")
plt.grid()
plt.savefig("./vmag_no_832_total_com_eixo.png")
plt.show()
plt.close()

dados_transpostos.plot()
plt.xlabel("Frequência (Hz)")
plt.ylabel("Impedância (V)")
plt.title("Fonte harmônica no nó 832.1")
plt.grid()
plt.savefig("./vmag_no_832_total_sem_eixo.png")
plt.show()
plt.close()
