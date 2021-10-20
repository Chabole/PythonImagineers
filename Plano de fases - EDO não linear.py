# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 16:01:37 2021

@author: Arthur chabole
"""

#

import os
import numpy as np
import matplotlib.pyplot as plt
from control.phaseplot import phase_plot
from numpy import pi
import random 

def model(z, t, Y=0):
    y1, y2 = z
    dy1dt = y2
    dy2dt = -y1*(1 + Y*(y1**2))
    return [dy1dt, dy2dt]

plt.figure()

k = []
j = 5
for i in range(300):
    a = random.randrange(-j, j) + random.random()
    b = random.randrange(-j, j) + random.random()
    k.append((a, b))

phase_plot(
    model,
    X0=k,
    T=np.linspace(0, 10, 1000),
    logtime=(3, 0.7)
)











