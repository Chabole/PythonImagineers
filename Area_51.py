import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import ZebraLib as zb
from scipy import stats

Avião = zb.Airplane()

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

média_calib, média_ref = [], []
for i in range(len(calib_0)):
    média_ref.append((ref_0[i] + ref_1[(len(calib_0)-1)-i])/2)
    média_calib.append((calib_0[i] + calib_1[(len(calib_0)-1)-i])/2)
    
poly_m = zb.fit(média_ref, média_calib, 1)
p_m = np.polyfit(média_ref, média_calib, 1)

slope, intercept, r_value, p_value, std_err = stats.linregress(média_ref, média_calib)

fig, ax = plt.subplots()
ax.set(ylabel= 'Calibrar [psi]', xlabel='Referencia [psi]')

#ax.scatter(ref_0, calib_0, color='red', label='Dados carga')
#ax.scatter(ref_1, calib_1, color='blue', label='Dados descarga')
ax.scatter(média_ref, média_calib, color='red', label='Dados médios')

#ax.plot(ref_0, poly_0(ref_0), linestyle=':', color='red', 
#    label='Linearização carga' + f'p(x)={p_0[0]:.2f}x + {p_0[1]:.2f}')

#ax.plot(ref_1, poly_1(ref_1), linestyle=':', color='blue', 
#    label='Linearização descarga '+ f'p(x)={p_1[0]:.2f}x - {abs(p_1[1]):.2f}')

ax.plot(média_ref, poly_m(média_ref), color='blue', linestyle=':', 
    label='Equação' + f' p(x)={p_m[0]:.2f}x - {abs(p_m[1]):.2f}' + r', $R^{2}=$' + f'{r_value:.3f}')

ax.legend()
ax.grid(linestyle='dotted')
ax.set_xlim(0)
ax.set_ylim(0)
plt.show()

fig.savefig('D:/Dados_2.pdf', bbox_inches='tight')

df = pd.DataFrame()

df['Referencia'] = média_ref
df['Calibrar'] = média_calib

df.to_excel('D:/DATA_PATH.xlsx')
