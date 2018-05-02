#!/bin/python

# geometric progression 

class geometric_progression:
    """

    """
    @staticmethod
    def gp(a, r, n):
        return a*(r**(n-1))


if __name__ == "__main__":
    a = int(raw_input("Enter initial No.         : "))
    r = int(raw_input("Enter common ratio        : "))
    n = int(raw_input("Enter last No.            : "))
    An = geometric_progression.gp(a, r, n)
    print "\nGP of " + str(n) + "th value is        : " + str(An)
