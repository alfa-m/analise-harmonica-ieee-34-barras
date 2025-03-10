import py_dss_interface
import pandas as pd
import numpy as np
import os
import pathlib

# Inicializa o objeto DSS
dss = py_dss_interface.DSS(r"C:\Program Files\OpenDSS")

# Adiciona o path e compila o arquivo .dss
script_path = os.path.dirname(os.path.abspath(__file__))
dss_file = pathlib.Path(script_path).joinpath("./ieee34Mod1.dss")
dss.text("Compile [{}]".format(dss_file))
dss.dssinterface.allow_forms = 0

# Cria variaveis contendo o nome das linhas, barras e nós
nomesLinhas = dss.lines.names
nomesBarras = dss.circuit.buses_names
nomesNos = dss.circuit.nodes_names

# Realiza a solução do fluxo de potência para obter os valores de magnitude e fase das tensões e correntes
dss.solution.solve()

# Remove demais fontes harmonicas
dss.text("Spectrum.DefaultLoad.NumHarm=1")

# Adiciona um monitor em cada linha
for i in range(len(nomesLinhas)):
    linha = nomesLinhas[i]
    dss.text("New Monitor.MonitorLine{} Line.{} 1 mode=0".format(linha, linha))

# Salva nomes dos monitores
nomesMonitores = dss.monitors.names

# Define o espectro de frequências a serem analisadas
harmonicos = np.arange(1,50.001,(0.5/60)).tolist()
dss.text("New spectrum.espectroharmonico numharm={} csvfile=espectro_harmonico.csv".format(str(len(harmonicos))))

# Cria loop de fonte de corrente harmônica
for j in range(len(nomesNos)):
    #  Adiciona a fonte de corrente harmônica de sequência positiva
    node = nomesNos[j]
    barra = node.split(".")
    barra = barra[0]
    scansource = "Isource.scansource{}".format(node)
    dss.text("New {} bus1={} amps=1 spectrum=espectroharmonico".format(scansource,node))

    dss.solution.solve()

    # Seleciona o modo de solução harmonic
    dss.text("Set mode=harmonic")
    matrixV = pd.DataFrame()

    # Realiza a solução harmônica iterada
    for h in range(len(harmonicos)):
        dss.text("Set harmonic={}".format(harmonicos[h]))
        dss.solution.solve()
        frequencia = str(round(harmonicos[h]*60,1))
        indice = "node_" + str(node) + "_frequencia_" + frequencia
        matrixV[indice] = dss.circuit.buses_vmag
        dss.monitors.reset_all()
        print("Nó " + node + " Frequência " + frequencia)

    matrixV.to_csv("./vmag_caso1_node_{}.csv".format(node))
    print("Matriz Vmag do nó {} exportada".format(node))

    # Desabilita a fonte de corrente atual
    fontesCorrente = dss.isources.names
    ultimaFonteCorrente = fontesCorrente[(len(fontesCorrente)-1)]
    dss.text("Disable Isource.{}".format(ultimaFonteCorrente))

print("Análise harmônica finalizada. Matrizes Vmag salvas")
