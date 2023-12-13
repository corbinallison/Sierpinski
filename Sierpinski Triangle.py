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
N = 100000
i = 3
x = rand.randint(0, 40)
y = rand.randint(0, x*np.tan(45))
x_array = np.zeros(N)
y_array = np.zeros(N)
tripoint = 0

x_array[0] = 0
y_array[0] = 0
x_array[1] = 20
y_array[1] = 40
x_array[2] = 40
y_array[2] = 0

x_array[3] = x
y_array[3] = y

while i < N-1:
    i += 1
    tripoint = rand.randint(0, 3)
    x_array[i] = np.abs(x_array[tripoint] + x_array[i-1])/2
    y_array[i] = np.abs(y_array[tripoint] + y_array[i-1])/2

fig, ax = plt.subplots()
ax.scatter(x_array, y_array, s=.01)

plt.show()