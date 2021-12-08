import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import ZebraLib as zb

df_0 = pd.read_excel('D:/UNESP/7 semestre - Eng/Lab. Mec. Flu/Relatório 3 - Dados.xlsx', 
sheet_name='Carregamento')

ref_0 = df_0['Referencia']
calib_0 = df_0['Calibrar']

df_1 = pd.read_excel('D:/UNESP/7 semestre - Eng/Lab. Mec. Flu/Relatório 3 - Dados.xlsx', 
sheet_name='Descarrega')

ref_1 = df_1['Referencia']
calib_1 = df_1['Calibrar']


poly_0 = zb.fit(ref_0, calib_0, 1)
p_0 = np.polyfit(ref_0, calib_0, 1)

poly_1 = zb.fit(ref_1, calib_1, 1)
p_1 = np.polyfit(ref_1, calib_1, 1)

fig, ax = plt.subplots()
ax.set(ylabel= 'Calibrar [psi]', xlabel='Referencia [psi]')

ax.scatter(ref_0, calib_0, color='red', label='Dados carga')
ax.scatter(ref_1, calib_1, color='blue', label='Dados descarga')

ax.plot(ref_0, poly_0(ref_0), linestyle=':', color='red', 
    label='Linearização carga' + f'p(x)={p_0[0]:.2f}x + {p_0[1]:.2f}')

ax.plot(ref_1, poly_1(ref_1), linestyle=':', color='blue', 
    label='Linearização descarga '+ f'p(x)={p_1[0]:.2f}x - {abs(p_1[1]):.2f}')

ax.legend()
ax.grid(linestyle='dotted')
ax.set_xlim(0)
ax.set_ylim(0)
plt.show()

fig.savefig('D:/Dados.pdf', bbox_inches='tight')