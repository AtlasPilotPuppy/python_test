#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Michael John
# Usage: python palindrome_product.py

"""A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 99.Find the largest
palindrome made from the product of two 3-digit numbers."""



if __name__ == '__main__':
    '''I chose to start from 999 and count down as that just made the most sense
    in my head. If you wanted just the palindrome, the list would not be
    necessary. I just used one here because I wanted to print the palindrome
    along with the two digits.'''

    pal_list = [] # Will hold our list of palindromes
    pmin = 100 # Minimum 3 digit number
    pmax = 999 # Maximum 3 digit number

    # start at the max and count down
    for m in range(pmax,pmin,-1):
        # start at 'm', to avoid duplicate checks of the same combination
        for n in range(m,pmin,-1):
            # Check if Palindrome
            if str(m*n) == str(m*n)[::-1]:
                # For convenience, save as a tuple to the list
                pal_list.append((m*n,m,n))

    # Find the largest palindrome in our list of tuples
    m = max(pal_list, key=lambda x:x[0])
    print("Largest Palindrome: {0}   {1}*{2}".format(m[0],m[1],m[2]))

