import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plota_vmag(dados_barra, nome_barra):
    harmonicos = np.arange(61,3000.5,0.5)
    plt.plot(harmonicos, dados_barra)
    plt.xlabel("Frequência")
    plt.xlim(0,3000)
    plt.ylabel("Impedância")
    plt.ylim(0,1000)
    plt.title("Medição na barra {} com fonte harmônica no nó 832.1".format(nome_barra))
    plt.grid()
    plt.show()
    plt.close()
    plt.pause(1)

dados = pd.read_csv('./vmag_caso2_node_832.1.csv', index_col = 0)

barra_2 = "802"
dados_barra_2 = dados.iloc[6,2:]
dados_transpostos_2 = dados_barra_2.T
plota_vmag(dados_transpostos_2, barra_2)

barra_2 = "802"
dados_barra_2 = dados.iloc[7,2:]
dados_transpostos_2 = dados_barra_2.T
plota_vmag(dados_transpostos_2, barra_2)

barra_2 = "802"
dados_barra_2 = dados.iloc[8,2:]
dados_transpostos_2 = dados_barra_2.T
plota_vmag(dados_transpostos_2, barra_2)


barra_6 = "812"
dados_barra_6 = dados.iloc[16,2:]
dados_transpostos_6 = dados_barra_6.T
plota_vmag(dados_transpostos_6, barra_6)

barra_6 = "812"
dados_barra_6 = dados.iloc[17,2:]
dados_transpostos_6 = dados_barra_6.T
plota_vmag(dados_transpostos_6, barra_6)

barra_6 = "812"
dados_barra_6 = dados.iloc[18,2:]
dados_transpostos_6 = dados_barra_6.T
plota_vmag(dados_transpostos_6, barra_6)


barra_8 = "850"
dados_barra_8 = dados.iloc[25,2:]
dados_transpostos_8 = dados_barra_8.T
plota_vmag(dados_transpostos_8, barra_8)

barra_8 = "850"
dados_barra_8 = dados.iloc[26,2:]
dados_transpostos_8 = dados_barra_8.T
plota_vmag(dados_transpostos_8, barra_8)

barra_8 = "850"
dados_barra_8 = dados.iloc[27,2:]
dados_transpostos_8 = dados_barra_8.T
plota_vmag(dados_transpostos_8, barra_8)


barra_18 = "832"
dados_barra_18 = dados.iloc[47,2:]
dados_transpostos_18 = dados_barra_18.T
plota_vmag(dados_transpostos_18, barra_18)

barra_18 = "832"
dados_barra_18 = dados.iloc[48,2:]
dados_transpostos_18 = dados_barra_18.T
plota_vmag(dados_transpostos_18, barra_18)

barra_18 = "832"
dados_barra_18 = dados.iloc[49,2:]
dados_transpostos_18 = dados_barra_18.T
plota_vmag(dados_transpostos_18, barra_18)


barra_26 = "844"
dados_barra_26 = dados.iloc[71,2:]
dados_transpostos_26 = dados_barra_26.T
plota_vmag(dados_transpostos_26, barra_26)

barra_26 = "844"
dados_barra_26 = dados.iloc[72,2:]
dados_transpostos_26 = dados_barra_26.T
plota_vmag(dados_transpostos_26, barra_26)

barra_26 = "844"
dados_barra_26 = dados.iloc[73,2:]
dados_transpostos_26 = dados_barra_26.T
plota_vmag(dados_transpostos_26, barra_26)


barra_28 = "848"
dados_barra_28 = dados.iloc[77,2:]
dados_transpostos_28 = dados_barra_28.T
plota_vmag(dados_transpostos_28, barra_28)

barra_28 = "848"
dados_barra_28 = dados.iloc[78,2:]
dados_transpostos_28 = dados_barra_28.T
plota_vmag(dados_transpostos_28, barra_28)

barra_28 = "848"
dados_barra_28 = dados.iloc[79,2:]
dados_transpostos_28 = dados_barra_28.T
plota_vmag(dados_transpostos_28, barra_28)

