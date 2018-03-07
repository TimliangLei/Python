# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 18:52:13 2016

@author: Administrator
"""
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False

import numpy as np
import pandas as pd

error = np.random.randn(10)
y = pd.Series(np.sin(np.arange(10)))
y.plot(yerr = error)#绘制误差图
plt.show()

