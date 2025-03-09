import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

vmag_df = pd.read_csv("./vmag_node_828.1.csv", index_col=0)
tensao_1 = vmag_df.iloc[6,:]
tensao_2 = vmag_df.iloc[7,:]
tensao_3 = vmag_df.iloc[8,:]
harmonico = np.arange(1,50.001,(0.5/60)).tolist()
fig, ax = plt.subplots()
ax.plot(harmonico, tensao_1, label='V1')
ax.plot(harmonico, tensao_2, label='V2')
ax.plot(harmonico, tensao_3, label='V3')
ax.legend()
ax.grid()
plt.show()
