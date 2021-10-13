# Canis Li
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

curr = 0  # c2
print(10 ** -2.12)
print(10 ** -7.21)
print(10 ** -12.67)

A0 = 0.025
def equations(p):
    a, b, c, d, x, y = p
    return (
        x * b / a - 10 ** -2.12,
        x * c / b - 10 ** -7.21,
        x * d / c - 10 ** -12.67,
        x * y  - 10 ** -14,
        a + b + c + d - A0,  # C1
        b + 2 * c + 3 * d + y - x - curr, #curr = amount OH added
    )

def equation2(p):
    x = p
    return x**5+x**4*(curr+10**-2.21)+x**3*(10**-2.21*(curr-0.025)+10**-2.12*10**-7.21-10**-14)+x**2*(10**-2.21*10**-7.21*(curr-2*0.025)+10**-2.12*10**-7.21*10**-12.67-10**-2.12*10**-14)+x*(10**-2.12*10**-7.21*10**-12.67*(curr-3*0.025)-10**-2.12*10**-7.21*10**-14)-10**-2.12*10**-7.21*10**-12.67*10**-14
def equation3(p):
    x = p
    return x*(x+curr) - 10**-14
start = 0.02
end = 0.06
curr = start
incr = 0.0001
# start = -0.0005
# end = 0.0005
# curr = start
# incr = 0.0000001 # for without buffer (eq 3)

cs = []
xs = []
for i in range(-10,1):
    curr = start
    while curr < end:
        # print(curr)
        x = fsolve(equation2, 10**i)
        if (x>0):
            cs.append(curr)
            xs.append(-math.log10(x))
        # a, b, c, d, x,y  = fsolve(equations, (10**i,10**i,10**i,10**i,10**i, 10**i))
        # if a > 0 and b > 0 and c > 0 and d > 0 and x > 0 and y >0:
        #     print(curr,':', 'a', a, 'b', b, 'c', c, 'd', d, 'x', x, 'y', y)
        #     cs.append(curr)
        #     xs.append(-math.log10(x))
        # curr += incr
        curr +=incr

print(xs)
plt.scatter(cs, xs)
plt.xlabel("C2")
plt.ylabel("pH")
plt.show()
