#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
# import matplotlib as mpl
# import matplotlib.pyplot as plt

from numpy import random

# random.seed(12)

nsum = 1000000
pwin1 = 0.6

win_cond_min = 5
win_cond_mindiff = 2

matchwin1 = matchwin2 = 0
for i in range(nsum):
    nwin1 = nwin2 = 0
    while ((nwin1 < win_cond_min and
            nwin2 < win_cond_min) or
           np.abs(nwin1-nwin2) < win_cond_mindiff):
        X = random.random()
        if X < pwin1:
            nwin1 += 1
        else:
            nwin2 += 1
###    print("1 - %d : %d - 2\n" % (nwin1, nwin2))
    if nwin1 > nwin2:
        matchwin1 += 1
    else:
        matchwin2 += 1

print("simülasyon sonucu:\n")
print("1 - %d : %d -2\n" % (matchwin1, matchwin2))
