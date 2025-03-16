import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plota_vmag(dados_barra, nome_barra):
    harmonicos = np.arange(61,3000.5,0.5)
    plt.plot(harmonicos, dados_barra)
    plt.xlabel("Frequência")
    plt.ylabel("Impedância")
    plt.title("Medição na barra {} com fonte harmônica no nó 832.1".format(nome_barra))
    plt.grid()
    plt.savefig("../figuras/vmag_caso2_no_832_1_barra_{}.png".format(nome_barra))
    plt.show()
    plt.close()
    plt.pause(1)

dados = pd.read_csv('./vmag_caso2_node_832.1.csv', index_col = 0)

barra_0 = "sourcebus"
dados_barra_0 = dados.iloc[0:3,2:]
dados_transpostos_0 = dados_barra_0.T
plota_vmag(dados_transpostos_0, barra_0)

barra_1 = "800"
dados_barra_1 = dados.iloc[3:6,2:]
dados_transpostos_1 = dados_barra_1.T
plota_vmag(dados_transpostos_1, barra_1)

barra_2 = "802"
dados_barra_2 = dados.iloc[6:9,2:]
dados_transpostos_2 = dados_barra_2.T
plota_vmag(dados_transpostos_2, barra_2)

barra_3 = "806"
dados_barra_3 = dados.iloc[9:12,2:]
dados_transpostos_3 = dados_barra_3.T
plota_vmag(dados_transpostos_3, barra_3)

barra_4 = "808"
dados_barra_4 = dados.iloc[12:15,2:]
dados_transpostos_4 = dados_barra_4.T
plota_vmag(dados_transpostos_4, barra_4)

barra_5 = "810"
dados_barra_5 = dados.iloc[15,2:]
dados_transpostos_5 = dados_barra_5.T
plota_vmag(dados_transpostos_5, barra_5)

barra_6 = "812"
dados_barra_6 = dados.iloc[16:19,2:]
dados_transpostos_6 = dados_barra_6.T
plota_vmag(dados_transpostos_6, barra_6)

barra_7 = "814"
dados_barra_7 = dados.iloc[19:22,2:]
dados_transpostos_7 = dados_barra_7.T
plota_vmag(dados_transpostos_7, barra_7)

barra_7r = "814r"
dados_barra_7r = dados.iloc[22:25,2:]
dados_transpostos_7r = dados_barra_7r.T
plota_vmag(dados_transpostos_7r, barra_7r)

barra_8 = "850"
dados_barra_8 = dados.iloc[25:28,2:]
dados_transpostos_8 = dados_barra_8.T
plota_vmag(dados_transpostos_8, barra_8)

barra_9 = "816"
dados_barra_9 = dados.iloc[28:31,2:]
dados_transpostos_9 = dados_barra_9.T
plota_vmag(dados_transpostos_9, barra_9)

barra_10 = "818"
dados_barra_10 = dados.iloc[31,2:]
dados_transpostos_10 = dados_barra_10.T
plota_vmag(dados_transpostos_10, barra_10)

barra_11 = "824"
dados_barra_11 = dados.iloc[32:35,2:]
dados_transpostos_11 = dados_barra_11.T
plota_vmag(dados_transpostos_11, barra_11)

barra_12 = "820"
dados_barra_12 = dados.iloc[35,2:]
dados_transpostos_12 = dados_barra_12.T
plota_vmag(dados_transpostos_12, barra_12)

barra_13 = "822"
dados_barra_13 = dados.iloc[36,2:]
dados_transpostos_13 = dados_barra_13.T
plota_vmag(dados_transpostos_13, barra_13)

barra_14 = "826"
dados_barra_14 = dados.iloc[37,2:]
dados_transpostos_14 = dados_barra_14.T
plota_vmag(dados_transpostos_14, barra_14)

barra_15 = "828"
dados_barra_15 = dados.iloc[38:41,2:]
dados_transpostos_15 = dados_barra_15.T
plota_vmag(dados_transpostos_15, barra_15)

barra_16 = "830"
dados_barra_16 = dados.iloc[41:44,2:]
dados_transpostos_16 = dados_barra_16.T
plota_vmag(dados_transpostos_16, barra_16)

barra_17 = "854"
dados_barra_17 = dados.iloc[44:47,2:]
dados_transpostos_17 = dados_barra_17.T
plota_vmag(dados_transpostos_17, barra_17)

barra_18 = "832"
dados_barra_18 = dados.iloc[47:50,2:]
dados_transpostos_18 = dados_barra_18.T
plota_vmag(dados_transpostos_18, barra_18)

barra_19 = "858"
dados_barra_19 = dados.iloc[50:53,2:]
dados_transpostos_19 = dados_barra_19.T
plota_vmag(dados_transpostos_19, barra_19)

barra_20 = "834"
dados_barra_20 = dados.iloc[53:56,2:]
dados_transpostos_20 = dados_barra_20.T
plota_vmag(dados_transpostos_20, barra_20)

barra_21 = "860"
dados_barra_21 = dados.iloc[56:59,2:]
dados_transpostos_21 = dados_barra_21.T
plota_vmag(dados_transpostos_21, barra_21)

barra_22 = "842"
dados_barra_22 = dados.iloc[59:62,2:]
dados_transpostos_22 = dados_barra_22.T
plota_vmag(dados_transpostos_22, barra_22)

barra_23 = "836"
dados_barra_23 = dados.iloc[62,2:]
dados_transpostos_23 = dados_barra_23.T
plota_vmag(dados_transpostos_23, barra_23)

barra_24 = "840"
dados_barra_24 = dados.iloc[65:68,2:]
dados_transpostos_24 = dados_barra_24.T
plota_vmag(dados_transpostos_24, barra_24)

barra_25 = "862"
dados_barra_25 = dados.iloc[68:71,2:]
dados_transpostos_25 = dados_barra_25.T
plota_vmag(dados_transpostos_25, barra_25)

barra_26 = "844"
dados_barra_26 = dados.iloc[71:74,2:]
dados_transpostos_26 = dados_barra_26.T
plota_vmag(dados_transpostos_26, barra_26)

barra_27 = "846"
dados_barra_27 = dados.iloc[74:77,2:]
dados_transpostos_27 = dados_barra_27.T
plota_vmag(dados_transpostos_27, barra_27)

barra_28 = "848"
dados_barra_28 = dados.iloc[77:80,2:]
dados_transpostos_28 = dados_barra_28.T
plota_vmag(dados_transpostos_28, barra_28)

barra_31r = "852r"
dados_barra_31r = dados.iloc[80:83,2:]
dados_transpostos_31r = dados_barra_31r.T
plota_vmag(dados_transpostos_31r, barra_31r)

barra_29 = "888"
dados_barra_29 = dados.iloc[83:86,2:]
dados_transpostos_29 = dados_barra_29.T
plota_vmag(dados_transpostos_29, barra_29)

barra_30 = "856"
dados_barra_30 = dados.iloc[86,2:]
dados_transpostos_30 = dados_barra_30.T
plota_vmag(dados_transpostos_30, barra_30)

barra_31 = "852"
dados_barra_31 = dados.iloc[87:90,2:]
dados_transpostos_31 = dados_barra_31.T
plota_vmag(dados_transpostos_31, barra_31)

barra_32 = "864"
dados_barra_32 = dados.iloc[90,2:]
dados_transpostos_32 = dados_barra_32.T
plota_vmag(dados_transpostos_32, barra_32)

barra_33 = "838"
dados_barra_33 = dados.iloc[91,2:]
dados_transpostos_33 = dados_barra_33.T
plota_vmag(dados_transpostos_33, barra_33)

barra_34 = "890"
dados_barra_34 = dados.iloc[92:,2:]
dados_transpostos_34 = dados_barra_34.T
plota_vmag(dados_transpostos_34, barra_34)
