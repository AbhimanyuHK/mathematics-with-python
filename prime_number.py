#!/bin/python

class prime_numbers:


    """
    Prime number is a number which can only divide by 1 and itself
    
    Example of prime number are : 2, 3, 5, 7, 11, 13,....

    """    
    @staticmethod
    def check_prime_number(a):
        a1 = a
        is_prime = True
        if(a==0):
            return "number zero is not prime number"
        elif(a==1):
            return "number 1 is not prime number"
        else:
            if(a<0): a= a*(-1)
            r = range(2,a)
            for x in r:
                if(a%x==0):
                    is_prime = False
            if(is_prime):
                return "number " + str(a1) + " is prime number"
            else:
                return "number " + str(a1) + " is not prime number"



if __name__ == "__main__":
    a = int(raw_input("Enter Number To Check Prime: "))
    print prime_numbers.check_prime_number(a)
