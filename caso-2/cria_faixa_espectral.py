import pandas as pd
import numpy as np

frequencia_inicial = 60
frequencia_final = 3000
delta_frequencia = 0.5

harmonicos_pd = pd.DataFrame()
harmonicos_pd["harmonico"] = np.arange(frequencia_inicial, frequencia_final + 1, delta_frequencia).tolist()
harmonicos_pd["harmonico"] = harmonicos_pd["harmonico"].apply(lambda h : round((h/60), 6))
harmonicos_pd["amplitude"] = 100
harmonicos_pd["angulo"] = 0

harmonicos_pd.to_csv("./espectro_harmonico_header.csv")
harmonicos_pd.to_csv("./espectro_harmonico.csv", header=False, index=0)

print("Arquivo .csv com faixa espectral criado")
