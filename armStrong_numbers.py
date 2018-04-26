#!/bin/python

print "EX : Enter the range : 0 1000\n"
x, y = raw_input("Enter the range : ").split(' ')
x = int(x)
y = int(y)

for i in range(y):
    s = list(str(i)) # ['1', '2', '3',....]
    l = len(s) # 2
    n = 0
    for j in s:
        n += int(j)**l
    if(n==i): print i
    
