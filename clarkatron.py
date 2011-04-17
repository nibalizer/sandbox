#!/usr/bin/python

import numpy as np
from scipy import linalg
import pylab as plt


#v1(4*s^2+10*s+25) - v2(25) = 200*s
#v1(15) + v2(2*s + 15) = 400

#v1 * (a(s)) - v2 * (25) = 200 * s
#v1 * (15) + v2 * (b(s)) = 400

def a(s):
    t = 4*(s**2) + 10 * s + 25
    return t

def b(s):
    t = 2*s +15
    return t

s = 1
s_array = np.linspace(-2, 2, 1000)
v1 = []
v2 = []

print len(s_array)
for s in s_array:
    p1 = a(s)
    p2 = b(s)
    p3 = 200*s
    A = np.mat('[p1 -25; 15 p2]')
    B = np.mat('[p3;400]')

    z= linalg.solve(A,B)

    print s, float(z[0]), float(z[1]) 
    v1.append(float(z[0]))
    v2.append(float(z[1]))

plt.plot(s_array, v1, '.b')
plt.plot(s_array, v2, '.r')
plt.show()
