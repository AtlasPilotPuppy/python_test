#!/bin/env python2.7

"""A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 99.Find the largest
palindrome made from the product of two 3-digit numbers."""

"""
Finds the largest palindrome of 3-digit numbers multiplied together starting
from the smallest 3-digit number and working up.

Author:
    Eric Saupe
"""

#Initialize variables
largest_palindrome = 0
product_a = 0
product_b = 0

#Loop through all 3-digit numbers
for i in range(100, 1000):
    #We can start at the current number to not waste time with calculations already made
    for j in range(i, 1000):
        val = i * j
        #Check for palindrome and if it is larger
        if str(val) == str(val)[::-1] and val > largest_palindrome:
            largest_palindrome = val
            product_a = i
            product_b = j

#Output result
print '%s = %s %s' % (largest_palindrome, product_a, product_b)
