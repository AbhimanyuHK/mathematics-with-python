#!/bin/python

# LCM of (4, 6) is 12

x, y = raw_input("Enter first No.'s : ").split(' ')
x = int(x)
y = int(y)

xy = x*y

is_not = True

n = xy

for l in range(2, xy):
    if((x%l==0) & (y%l==0)):
        a = x/l
        b = y/l
        i = l*a*b
        if(n > i):
            is_not = False
            n = i

if(is_not):
    print "\nlcm of " + str(x) + " and " + str(y) + " is " + str(xy)
else:
    print "\nlcm of " + str(x) + " and " + str(y) + " is " + str(n)
    
