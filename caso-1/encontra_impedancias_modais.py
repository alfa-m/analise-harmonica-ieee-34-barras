import pandas as pd
import numpy as np
from procura_arquivos import procura

arquivos_impedancia = procura("z_modal_*.csv","./")
impedancias_modais = pd.DataFrame()

for arquivo in arquivos_impedancia:
    print("Arquivo atual: {}".format(arquivo))
    frequencia_atual = arquivo.split("_")[-1].rpartition(".")[0]
    arquivo_df = pd.read_csv("./{}".format(arquivo), index_col=0)
    impedancias_modais[frequencia_atual] = arquivo_df.iloc[:,0]

impedancias_modais_df = impedancias_modais.T
impedancias_modais_df.reset_index(inplace=True)
impedancias_modais_df = impedancias_modais_df.rename(columns={'index': 'Frequencia'})
impedancias_modais_df["Frequencia"] = impedancias_modais_df["Frequencia"].apply(lambda x: float(x))
impedancias_modais_df = impedancias_modais_df.sort_values(by="Frequencia")
impedancias_modais_df.reset_index(inplace=True, drop=True)
impedancias_modais_df.to_csv("impedancia_modal_caso1_total.csv")
