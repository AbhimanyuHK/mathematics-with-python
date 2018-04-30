#!/bin/sh

# GCD of 60 and 36 is 12 

def get_gcd(a, b):
    if(a==0&b==0):
        return 0
    r = 1
    if(a>b):
        high, low = a, b
    elif(a<b):
        high, low = b, a
    elif(a==b):
        high, low = b, a

    while(r>0):
        r = high%low
        high = low 
        low = r
    return high



if __name__ == "__main__":
    a, b = raw_input("Enter two No.'s : ").split(' ')
    a = int(a)
    b = int(b)
    print get_gcd(a, b)

