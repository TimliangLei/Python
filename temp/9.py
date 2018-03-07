# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 18:43:02 2016

@author: Administrator
"""
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']#用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False#用来正常显示负号

import numpy as np
import pandas as pd

x = pd.Series(np.exp(np.arange(20)))#原始数据
x.plot(label = u'原始数据图', legend =True)
plt.show()
x.plot(logy = True, label = u'对数数据图', legend = True)
plt.show()
