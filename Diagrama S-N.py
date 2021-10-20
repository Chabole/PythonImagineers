# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 10:44:51 2021

@author: Arthur Chabole
"""

import numpy as np 
import matplotlib.pyplot as plt
import Classe_fadiga as fd

#Valores de ciclos e tipo de acabamento
Superficies = ['usinado', 'retificado', 'forjado', 'laminado']
ciclos = np.array((1, 10, 100, 1E3, 1E4, 1E5, 1E6, 1E7, 1E8))

#Gráfico - cosméticos
fig, ax = plt.subplots(figsize=(10,7))
ax.set(title='Diagrama S-N', 
       xlabel=r'Ciclos [$N$]', ylabel=r'Tensão $\sigma$')

#Plotando pra diferentes acabamentos

#Com correção de resistência a fadiga
for superf in (Superficies):
    
    Mat = fd.S_fadiga('aço', Sult=500,
                kind='flexão', acabamento=superf,
                c='90', d=25)
    
    sigma = Mat.diagrama_SN(ciclos)
    
    ax.scatter(ciclos, sigma)
    ax.plot(ciclos, sigma, label=f'{Mat.acabamento} e '  + r"$S_f'$=" + f'{Mat.S_f:.0f}Mpa')

#Sem correção de resistência a fadiga
sigma = Mat.diagrama_SN(ciclos, correção=False)
ax.scatter(ciclos, sigma)
ax.plot(ciclos, sigma, '--', label='sem correção')

#Deixando bonito
ax.set_xscale('log')
ax.set_yscale('log')
#ax.set_ylim(4E2, 1E3)
ax.set_xlim(1E+3, 1E8)
ax.legend()
ax.grid(linestyle='dotted')

fig.savefig('D:/UNESP/PythonImagineers/diagrama_SN.pdf')