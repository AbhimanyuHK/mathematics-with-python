#!/bin/python 

# a*x^2 + b*x + c = 0

a = input('Enter X^2 coeff (a) : ')
b = input('Enter X coeff (b) : ')
c = input('Enter constant C : ')

m = a*c

if(m < 0):
    r = range(m, 0)
elif(b < 0):
    r = range(-m, m+1)
else:
    r = range(1,m+1)

print "\n No. of solutions : "
is_not_exist = True

for x in r: 
     if (x != 0):
         if(m%x==0):
             y = m/x
             if(b ==(x + y)):
                 is_not_exist = False
                 print "(" + str(x) + ", " + str(y) + ")"

if(is_not_exist): print "No solution exist"

