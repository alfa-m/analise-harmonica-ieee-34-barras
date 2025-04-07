import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plota_vmag(dados_barra, nome_barra):
    harmonicos = np.arange(61,3000.5,0.5)
    plt.plot(harmonicos, dados_barra)
    plt.xlabel("Frequência (Hz)")
    plt.ylabel("Tensão (V)")
    plt.title("Medição na barra {} com fonte harmônica no nó 848.1".format(nome_barra))
    plt.grid()
    plt.savefig("../figuras/vmag_caso2_no_848_1_barra_{}_sem_eixo.png".format(nome_barra))
    plt.show()
    plt.close()
    plt.pause(1)

    plt.plot(harmonicos, dados_barra)
    plt.xlabel("Frequência (Hz)")
    plt.xlim(0,3000)
    plt.ylabel("Tensão (V)")
    plt.ylim(0,1000)
    plt.title("Medição na barra {} com fonte harmônica no nó 848.1".format(nome_barra))
    plt.grid()
    plt.savefig("../figuras/vmag_caso2_no_848_1_barra_{}_total.png".format(nome_barra))
    plt.show()
    plt.close()
    plt.pause(1)

    plt.plot(harmonicos, dados_barra)
    plt.xlabel("Frequência (Hz)")
    plt.xlim(0,1000)
    plt.ylabel("Tensão (V)")
    plt.ylim(0,500)
    plt.title("Medição na barra {} com fonte harmônica no nó 848.1".format(nome_barra))
    plt.grid()
    plt.savefig("../figuras/vmag_caso2_no_848_1_barra_{}_harmonico_1.png".format(nome_barra))
    plt.show()
    plt.close()
    plt.pause(1)

    plt.plot(harmonicos, dados_barra)
    plt.xlabel("Frequência (Hz)")
    plt.xlim(1000,3000)
    plt.ylabel("Tensão (V)")
    plt.ylim(0,1000)
    plt.title("Medição na barra {} com fonte harmônica no nó 848.1".format(nome_barra))
    plt.grid()
    plt.savefig("../figuras/vmag_caso2_no_848_1_barra_{}_harmonico_2.png".format(nome_barra))
    plt.show()
    plt.close()
    plt.pause(1)

dados = pd.read_csv('./vmag_caso2_node_848.1.csv', index_col = 0)

barra_2 = "802"
dados_barra_2 = dados.iloc[6:9,2:]
dados_transpostos_2 = dados_barra_2.T
plota_vmag(dados_transpostos_2, barra_2)

barra_6 = "812"
dados_barra_6 = dados.iloc[16:19,2:]
dados_transpostos_6 = dados_barra_6.T
plota_vmag(dados_transpostos_6, barra_6)

barra_8 = "850"
dados_barra_8 = dados.iloc[25:28,2:]
dados_transpostos_8 = dados_barra_8.T
plota_vmag(dados_transpostos_8, barra_8)

barra_18 = "832"
dados_barra_18 = dados.iloc[47:50,2:]
dados_transpostos_18 = dados_barra_18.T
plota_vmag(dados_transpostos_18, barra_18)

barra_26 = "844"
dados_barra_26 = dados.iloc[71:74,2:]
dados_transpostos_26 = dados_barra_26.T
plota_vmag(dados_transpostos_26, barra_26)

barra_28 = "848"
dados_barra_28 = dados.iloc[77:80,2:]
dados_transpostos_28 = dados_barra_28.T
plota_vmag(dados_transpostos_28, barra_28)
