# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 20:40:07 2021

@author: Arthur Chabole
==========================

"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import ZebraLib as zb
from scipy import stats

df = pd.read_excel('D:/UNESP/7 semestre - Eng/Lab. TCM I/Dados_exp4_Latinha.xlsx',
                    sheet_name='Planilha2')
tempo = df['Tempo(min) ']
temperature = df['Temperaura']         

slope, intercept, r_value, p_value, std_err = stats.linregress(tempo, temperature)
 
fig, ax = plt.subplots()
ax.set(xlabel='Tempo[min]', ylabel='Temperatura[°C]')

ax.scatter(tempo, temperature, label='Dados')
zb.setup(ax)      
fig.savefig('D:/fig_TCM.pdf', bbox_inches='tight')