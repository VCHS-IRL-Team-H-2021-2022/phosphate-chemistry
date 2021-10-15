"""
x/curr= concentration of h2po4
a = concentration of hpo4
b = concentration of h3po4
a-b = concentration of h+
"""

import math

import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# def equations(p):
#     a,b = p # p = tuple
#     return (a+b-6,a-b-2)

# a,b = fsolve(equations, (0,0))

# print(a,b)
# print(equations((a,b)))

curr = 0

A0 = 0.025

# (a-b)*a/x=6.31*10^-8, b/(x(a-b)) = 1.38*10^-12, find x


def equation(p):
    a, b = p
    return (
        (a-b)*a/curr - 6.31*10 ** -8,
        b/(curr * (a-b)) - 1.38*10 ** -12
    )


def equation2(p):
    a, b = p
    return (
        (a-b)*a/curr - 10**-7.2,
        b/(curr * (a-b)) - 10**(14-2.14)
    )


def equation3(p):
    a, b = p
    return (
        (a-b)*a/curr - 10**-12.37,
        b/(curr * (a-b)) - 10**(14-7.2)
    )


start = 0.0001
end = .1
curr = start
incr = 0.001

cs = []
xs = []

curr = start
while curr < end:
    print(curr)
    # a, b = fsolve(equation, (10**-6, 10**-20))
    a, b = fsolve(equation2, (10**-5, 10**-19))
    print(a, b)
   # cs.append(curr)
   # its garbo lol
   # ima remove those outliers good now
    if(b < 0.08 and a > b):
        cs.append(curr)
        xs.append(-math.log10(a-b))
    # ur mic still sucks
    # if(a > -0.008):
    #     cs.append(curr)
    #     xs.append(a)
    # a, b, c, d, x,y  = fsolve(equations, (10**i,10**i,10**i,10**i,10**i, 10**i))
    # if a > 0 and b > 0 and c > 0 and d > 0 and x > 0 and y >0:
    #     print(curr,':', 'a', a, 'b', b, 'c', c, 'd', d, 'x', x, 'y', y)
    #     cs.append(curr)
    #     xs.append(-math.log10(x))
    # curr += incr
    curr += incr
    # ur  mic sucks # ur cutting out turn off noise cancellation

print(xs)
plt.scatter(cs, xs)
plt.xlabel("x")
plt.ylabel("-log(a-b)")
plt.show()
