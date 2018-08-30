# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 22:00
# @Author  : jf.zhang
# @File    : classification.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,10, 365)
x=t**2
r=np.random.randn(365)*10
y=x+r
plt.plot(t,y)
z=[y[0]]
z2=[y[0]]
for i in range(len(y)-1):
    z.append(z[i]*0.9+y[i+1]*0.1)
    z2.append(z2[i]*0.98+y[i+1]*0.02)
plt.plot(t,z)
plt.plot(t,z2)
plt.legend(['y1','y2','y3'])
plt.show()

