#!/bin/python

# HCF of (4, 6) is 2

x, y = raw_input("Enter first No.'s : ").split(' ')
x = int(x)
y = int(y)

xy = x*y

n = 0

for l in range(1, xy):
    if((x%l==0) & (y%l==0)):
        n = l

print n

