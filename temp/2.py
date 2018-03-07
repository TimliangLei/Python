# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 23:48:24 2016

@author: Administrator
"""
from scipy.optimize import fsolve
def f(x):#定义要求解的方程组
    x1 = x[0]
    x2 = x[1]
    return [2*x1 - x2**2 - 1, x1**2 - x2 -2]

result = fsolve(f,[1,1])#输入初值[1,1]并求解
print(result)

#数值积分
from scipy import integrate#导入积分函数
def g(x):
    return (1-x**2)**0.5
pi_2,err = integrate.quad(g, -1, 1)
print(pi_2 *2)