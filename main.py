# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 19:16:45 2019

@author: Alan Maldonado
"""

"""
Input: Function, Poly Grade, Center Point
Output: Polynomic Function
"""

# Libraries
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import math

#Default Variables
x_lim = [-2, 3] #Graph Range

#Default Functions
def algorithmStart(f, grad, x0):
    f_der = f
    p = 0
    for k in range(grad+1):
        p = p + (f_der.evalf(subs={'x': x0})/math.factorial(k))*(x-x0)**k
        f_der = sp.diff(f_der, 'x')
    p = sp.expand(p)
    print(p)

########### Change
x = sp.Symbol('x') #X is the symbol.
f = sp.exp(x) #Define the function

poly_grad = 3 #Polynomial Grade
center_p = 1 #Center Point
algorithmStart(f, poly_grad, center_p)