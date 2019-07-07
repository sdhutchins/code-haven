# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 11:07:33 2016

@author: shutchins2
"""

import numpy as np
from matplotlib import pyplot as plt

def simulate(K, mu, sig, Sbar, T):

    S = np.zeros(T+1)
    W = np.zeros(T+1)
    I = np.zeros(T+1)
    S[0] = K

    for t in range(T):
        W[t] = min(S[t], Sbar)
        I[t+1] = max(np.random.normal(mu, sig), 0)
        S[t+1] = min(S[t] - W[t] + I[t+1], K)

    return S
S = simulate(100, 70, 70, 70, 100)
plt.plot(S)
