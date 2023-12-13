#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 20:12:31 2022

@author: Corbin
"""

import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt


triangle = [[0, 20, 40], [0, 20, 0]]
N = 300000
i = 6
x = 20
y = 10
x_array = np.zeros(N)
y_array = np.zeros(N)
tripoint = 0

x_array[0] = 10
y_array[0] = 0
x_array[1] = 20
y_array[1] = 0
x_array[2] = 5*(2-np.sqrt(2))
y_array[2] = 5*(np.sqrt(2))
x_array[3] = 10
y_array[3] = 10*(np.sqrt(2))
x_array[4] = 20
y_array[4] = 10*(np.sqrt(2))
x_array[5] = 20+5*np.sqrt(2)
y_array[5] = 5*np.sqrt(2)

x_array[i] = x
y_array[i] = y

while i < N-1:
    i += 1
    tripoint = rand.randint(0, 6)
    x_array[i] = np.abs(x_array[tripoint] + x_array[i-1])/2
    y_array[i] = np.abs(y_array[tripoint] + y_array[i-1])/2

fig, ax = plt.subplots()
ax.scatter(x_array, y_array, s=.001)

plt.show()