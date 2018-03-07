# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 18:32:38 2016

@author: Administrator
"""
import matplotlib.pyplot as plt
import numpy as np
x= np.random.randn(1000)#1000个服从正态分布的随机数
plt.hist(x,10)#分成10组进行绘制直方图
plt.show()
