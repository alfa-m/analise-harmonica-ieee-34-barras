import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plota_vmag(dados_barra, nome_barra):
    harmonicos = np.arange(60,3000.5,0.5)
    plt.plot(harmonicos, dados_barra)
    plt.xlabel("Frequência")
    plt.ylabel("Impedância")
    plt.title("Medição na barra {} com fonte harmônica no nó 832.1".format(nome_barra))
    plt.grid()
    #plt.savefig("./figuras/zmodal_barra_{}.png".format(nome_barra))
    plt.show()
    plt.close()
    plt.pause(1)


dados = pd.read_csv("./caso-1/impedancia_modal_caso1_total.csv")
dados = dados.rename(columns={'Unnamed: 0': 'Frequência'})
dados.sort_values(by="Frequência", inplace=True)
dados = dados.iloc[:, 1:]

plota_vmag(dados, "total")

barra_0 = "sourcebus"
dados_barra_0 = dados.iloc[:,0:3]
plota_vmag(dados_barra_0, barra_0)

barra_1 = "800"
dados_barra_1 = dados.iloc[:,4:7]
plota_vmag(dados_barra_1, barra_1)

barra_2 = "802"
dados_barra_2 = dados.iloc[:,7:10]
plota_vmag(dados_barra_2, barra_2)

barra_3 = "806"
dados_barra_3 = dados.iloc[:,9:12]
plota_vmag(dados_barra_3, barra_3)


barra_4 = "808"
dados_barra_4 = dados.iloc[:,12:15]
plota_vmag(dados_barra_4, barra_4)

barra_5 = "810"
dados_barra_5 = dados.iloc[:,15]
plota_vmag(dados_barra_5, barra_5)

barra_6 = "812"
dados_barra_6 = dados.iloc[:,16:19]
plota_vmag(dados_barra_6, barra_6)

barra_7 = "814"
dados_barra_7 = dados.iloc[:,19:22]
plota_vmag(dados_barra_7, barra_7)

barra_7r = "814r"
dados_barra_7r = dados.iloc[:,22:25]
plota_vmag(dados_barra_7r, barra_7r)

barra_8 = "850"
dados_barra_8 = dados.iloc[:,25:28]
plota_vmag(dados_barra_8, barra_8)

barra_9 = "816"
dados_barra_9 = dados.iloc[:,28:31]
plota_vmag(dados_barra_9, barra_9)

barra_10 = "818"
dados_barra_10 = dados.iloc[:,31]
plota_vmag(dados_barra_10, barra_10)

barra_11 = "824"
dados_barra_11 = dados.iloc[:,32:35]
plota_vmag(dados_barra_11, barra_11)

barra_12 = "820"
dados_barra_12 = dados.iloc[:,35]
plota_vmag(dados_barra_12, barra_12)

barra_13 = "822"
dados_barra_13 = dados.iloc[:,36]
plota_vmag(dados_barra_13, barra_13)

barra_14 = "826"
dados_barra_14 = dados.iloc[:,37]
plota_vmag(dados_barra_14, barra_14)

barra_15 = "828"
dados_barra_15 = dados.iloc[:,38:41]
plota_vmag(dados_barra_15, barra_15)

barra_16 = "830"
dados_barra_16 = dados.iloc[:,41:44]
plota_vmag(dados_barra_16, barra_16)

barra_17 = "854"
dados_barra_17 = dados.iloc[:,44:47]
plota_vmag(dados_barra_17, barra_17)

barra_18 = "832"
dados_barra_18 = dados.iloc[:,47:50]
plota_vmag(dados_barra_18, barra_18)

barra_19 = "858"
dados_barra_19 = dados.iloc[:,50:53]
plota_vmag(dados_barra_19, barra_19)

barra_20 = "834"
dados_barra_20 = dados.iloc[:,53:56]
plota_vmag(dados_barra_20, barra_20)

barra_21 = "860"
dados_barra_21 = dados.iloc[:,56:59]
plota_vmag(dados_barra_21, barra_21)

barra_22 = "842"
dados_barra_22 = dados.iloc[:,59:62]
plota_vmag(dados_barra_22, barra_22)

barra_23 = "836"
dados_barra_23 = dados.iloc[:,62]
plota_vmag(dados_barra_23, barra_23)

barra_24 = "840"
dados_barra_24 = dados.iloc[:,65:68]
plota_vmag(dados_barra_24, barra_24)

barra_25 = "862"
dados_barra_25 = dados.iloc[:,68:71]
plota_vmag(dados_barra_25, barra_25)

barra_26 = "844"
dados_barra_26 = dados.iloc[:,71:74]
plota_vmag(dados_barra_26, barra_26)

barra_27 = "846"
dados_barra_27 = dados.iloc[:,74:77]
plota_vmag(dados_barra_27, barra_27)

barra_28 = "848"
dados_barra_28 = dados.iloc[:,77:80]
plota_vmag(dados_barra_28, barra_28)

barra_31r = "852r"
dados_barra_31r = dados.iloc[:,80:83]
plota_vmag(dados_barra_31r, barra_31r)

barra_29 = "888"
dados_barra_29 = dados.iloc[:,83:86]
plota_vmag(dados_barra_29, barra_29)

barra_30 = "856"
dados_barra_30 = dados.iloc[:,86]
plota_vmag(dados_barra_30, barra_30)

barra_31 = "852"
dados_barra_31 = dados.iloc[:,87:90]
plota_vmag(dados_barra_31, barra_31)

barra_32 = "864"
dados_barra_32 = dados.iloc[:,90]
plota_vmag(dados_barra_32, barra_32)

barra_33 = "838"
dados_barra_33 = dados.iloc[:,91]
plota_vmag(dados_barra_33, barra_33)

barra_34 = "890"
dados_barra_34 = dados.iloc[:,92:]
plota_vmag(dados_barra_34, barra_34)

