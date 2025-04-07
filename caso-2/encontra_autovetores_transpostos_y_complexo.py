import pandas as pd
import numpy as np
from procura_arquivos import procura

lista_de_autovetores = procura("autovetores_complexa_y*.csv", './')

for autovetor in lista_de_autovetores:
    print("Arquivo atual: {}".format(autovetor))
    caminho = "./{}".format(autovetor)
    autovetor_df = pd.read_csv(caminho, index_col=0)
    autovetor_complexa = autovetor_df.astype(complex)
    autovetor_complexa = autovetor_complexa.values
    autovetor_transposto = autovetor_complexa.transpose()
    autovetor_transposto_df = pd.DataFrame(autovetor_transposto)
    autovetor_transposto_df.to_csv("./transposto_{}".format(autovetor))
    fator_participacao = np.matmul(autovetor_complexa, autovetor_transposto)
    fator_participacaoo_df = pd.DataFrame(fator_participacao)
    fator_participacaoo_df.to_csv("./fator_participacao_{}".format(autovetor))

print("Matrizes de autovetores transpostos e de fator de participação obtidas")
