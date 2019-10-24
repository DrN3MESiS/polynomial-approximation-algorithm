# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 19:16:45 2019

@author: User
"""

"""
Input: Function, Poly Grade, Center Point
Output: Polynomic Function
"""

# Libraries
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

#Default Variables


#Default Functions
def algorithmStart():
    pass

# Change
x = sp.symbol('x') #X is the symbol.
f = sp.exp(x) #Define the function

poly_grad = 1
center_p = 0
algorithmStart(f, poly_grad, center_p)