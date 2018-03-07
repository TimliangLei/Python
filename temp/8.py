# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 18:35:34 2016

@author: Administrator
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x = np.random.randn(1000)#1000个服从正太分布的随机数
D = pd.DataFrame([x, x+1]).T #构造两列的DataFrame
D.plot(kind = 'box')
plt.show()
