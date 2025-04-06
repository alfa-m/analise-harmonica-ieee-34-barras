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

# Adiciona dados de coordenadas das barras
dss.text("Buscoords IEEE34_BusXY.csv")

dss.text("Solve")

dss.text("Plot type=circuit quantity=power")
