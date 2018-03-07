# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 16:29:10 2016

@author: Administrator
"""
import matplotlib.pyplot as plt

#The slices will be ordered and plotted counter-clockwise.
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'#定义标签
sizes = [15, 30, 45, 10]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']#每一块的颜色
explode = (0, 0.1,0,0)
plt.pie(sizes, explode=explode, labels = labels, colors = colors, autopct = '%1.1f%%', shadow = True, startangle = 90)
plt.axis('equal')
plt.show()

                                        