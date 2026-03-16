#!/bin/python3
# Lab 1: approx math const
import random
n=0

# #12.
# print('Nu kör vi!')

#13.
# n=1000000
for k in range(1000000):
    # print('nu kör vi!') #15.
    #14.
    x=random.random()
    # print(x)
    #16.
    y=random.random()
    #17.
    z=x**2+y**2
    # print(z)
    if z < 1:
        n=n+1
        # print('Innanför!')
    #18.
# print(f'n={n}')
ratio = n / 1000000
print(f'ratio={4*ratio}')
