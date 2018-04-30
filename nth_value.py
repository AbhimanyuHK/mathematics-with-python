#!/bin/python

# Tn = a + (n - 1)d

class nth_number:
    """
    Tn = a + (n - 1)d
    [0, 2, 4, 6, 8, 10] if n = 6 => Tn = 12 and so on.
 
    """
    @staticmethod
    def get_nth_number(a, d, n):
        """
        a : initial number
        d : difference of two numbers
        n : number to find the nth number value
        """
        tn = a + (n-1)*d
        return tn


if __name__ == "__main__":
    a = int(raw_input("Enter initial No.         : "))
    d = int(raw_input("Enter difference of No.'s : "))
    n = int(raw_input("Enter last No.            : "))
    tn = nth_number.get_nth_number(a, d, n)
    print "\n" + str(n) + "th value is              : " + str(tn)
