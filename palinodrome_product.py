"""A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 99.Find the largest
palindrome made from the product of two 3-digit numbers."""



def isPalindrome(number):
    """
    Test if the given number is a palindrome.

    Returns a boolean.
    """
    number = str(number)
    reversed = number[::-1]
    if number==reversed:
        return True
    else:
        return False

def brute_force():
    """
    Perform a brute force search for the largest palindrome made from the
    product of two 3-digit numbers.

    Returns a tuple consisting of the palindrom and its 3-digit factors.

    Example:
    >>> brute_force()
    (906609,913,993)

    """
    # parmeters ( we want to search through products of 3-digit numbers )
    floor = 100
    ceiling = 999

    # initialize variables
    factor1 = 0
    factor2 = 0
    product = 0
    highestPalindrome = 0

    # I excpect this search can be reduced by finding appropriate factors
    # or some other number theory math idea about palindromes.
    for i in range(floor,ceiling+1):
            for j in range(floor,ceiling+1):
                    product = i * j
                    if (isPalindrome(product) and (highestPalindrome < product) ):
                        highestPalindrome = product
                        factor1 = i
                        factor2 = j
    return highestPalindrome, factor1, factor2


def brute_force_no_doubles():
    """
    Perform a brute force search for the largest palindrome made from the
    product of two 3-digit numbers.

    Returns a tuple consisting of the palindrom and its 3-digit factors.

    This method eliminates double checking pairs, e.g. brute_force() checks
    both i=500, j=900 and i=900, j=500.  To eliminate this we can assume that
    we always have j>=i.

    Example:
    >>> brute_force()
    (906609,913,993)

    """
    # parmeters ( we want to search through products of 3-digit numbers )
    floor = 100
    ceiling = 999

    # initialize variables
    factor1 = 0
    factor2 = 0
    product = 0
    highestPalindrome = 0

    # I excpect this search can be reduced by finding appropriate factors
    # or some other number theory math idea about palindromes.
    for i in range(floor,ceiling+1):
            for j in range(i,ceiling+1):
                    product = i * j
                    if (isPalindrome(product) and (highestPalindrome < product) ):
                        highestPalindrome = product
                        factor1 = i
                        factor2 = j
    return highestPalindrome, factor1, factor2


def brute_force_count_down():
    """
    Perform a brute force search for the largest palindrome made from the
    product of two 3-digit numbers.

    Returns a tuple consisting of the palindrom and its 3-digit factors.

    If we count down from 999 rather than up to 999, once we run into a palindrome
    there is no need to check smaller factors in that loop, so we can save time
    not checking those pairs.

    Example:
    >>> brute_force()
    (906609,913,993)

    """
    # parmeters ( we want to search through products of 3-digit numbers )
    floor = 100
    ceiling = 999

    # initialize variables
    factor1 = 0
    factor2 = 0
    product = 0
    highestPalindrome = 0

    for i in range(ceiling,floor-1,-1):
        for j in range(ceiling,i-1,-1):
            product = i*j
            factor1 = i
            factor2 = j
            if product <= highestPalindrome:
                break # no need to check smaller j, from this point on i*j will always be too small. 
            if isPalindrome(product):
                highestPalindrome = product

    return highestPalindrome, factor1, factor2

if __name__ == "__main__":
    highestPalindrome, factor1, factor2 = brute_force_count_down()
    print "Largest palindrome made from the product of two 3-digit numbers is \
{:,} made from {} * {}.".format(highestPalindrome, factor1, factor2)
