# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 19:16:45 2019

@author: Alan Maldonado
@version: 2.0.0
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
xlim = [-2, 3] #Graph Range

#Default Functions
def algorithmStart(f, grad, x0):
    f_der = f
    p = 0
    for k in range(grad+1):
        p = p + (f_der.evalf(subs={'x': x0})/math.factorial(k))*(x-x0)**k
        f_der = sp.diff(f_der, 'x')
    p = sp.expand(p)
    print(p)
    
    #Graphing
    x_data = np.linspace(xlim[0], xlim[1], 500)
    f_vector = sp.lambdify(x,f,'numpy')
    f_data = f_vector(x_data)
    
    P_vector = sp.lambdify(x,p,'numpy')
    P_data = P_vector(x_data)
    
    fig = plt.figure(1)
    ax = fig.add_subplot(1,1,1)
    ax.cla()
    ax.plot(x_data, f_data, color=(0,0,1), lw=4)
    ax.plot(x_data, P_data, color=(0,1,0), ls='--',lw=4)
    ax.grid(True)
    ax.legend(['Function', 'Taylor'])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    fig.canvas.draw()
    

########### Change
x = sp.Symbol('x') #X is the symbol.
f = sp.exp(x) #Define the function

poly_grad = 3 #Polynomial Grade
center_p = 1 #Center Point
algorithmStart(f, poly_grad, center_p)