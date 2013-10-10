"""A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 99.Find the largest
palindrome made from the product of two 3-digit numbers."""



def isPalindrome(number):
        number = str(number)
        reversed = number[::-1]
        if number==reversed:
                return True
        else:
                return False
# brute force search


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


print "Largest palindrome made from the product of two 3-digit numbers is \
{:,} made from {} * {}.".format(highestPalindrome, factor1, factor2)
