# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 09:21:09 2021

@author: OPEYEMI IBRAHIM
"""
# Lagrange Interpolation Method

# Importing NumPy Library
import numpy as np

# Reading number of unknowns
n = int(input('Enter number of data points: '))

# Making numpy array of n & n x n size and initializing to zero for storing x and y value along with differences of y
a = np.zeros((n))
b = np.zeros((n))

# Reading data points

print("\nEnter data for x and y: ")
for i in range(n):
    a[i] = float(input( 'x['+str(i)+']='))
    b[i] = float(input( 'y['+str(i)+']='))

# Reading interpolation point
x = float(input("\nEnter interpolation point, x = "))

# Set interpolated value initially to zero
sm = 0

# Implementing Lagrange Interpolation
for i in range(n):

    pr = 1

    for j in range(n):
        if i != j:
            pr = pr * (x - a[j])/(a[i] - a[j])

    sm = sm + pr * b[i]

# Displaying output
print("\nInterpolated value at %.3f is equal to %.3f." % (x, sm))
