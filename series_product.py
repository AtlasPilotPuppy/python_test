#!/bin/env python2.7

from copy import copy

"""Complete this program to find the greatest product of five consecutive
digits in the list"""

"""
Loop to find the greatest product of five consectuive digits read from a file.
Assumes that line breaks do not count as separation of digits, meaning it
reads line breaks, or any non-integer character, as if it weren't there.

Author:
    Eric Saupe
"""
in_file = open('array.txt')

#Initialize variables
greatest_product = 0
greatest_numbers = []
numbers = []

for c in in_file.read():
    #If we don't have 5 numbers add the character if it's an int
    if len(numbers) < 5:
        try:
            numbers.append(int(c))
        except:
            pass
    #If we have 5 numbers, multiply and check, pop first number
    if len(numbers) == 5:
        product = reduce(lambda x, y: x * y, numbers)
        if product > greatest_product:
            greatest_product = product
            #Make a copy so values aren't changed
            greatest_numbers = copy(numbers)
        numbers.pop(0)

#Output result
print '%s = %s' % (greatest_product, greatest_numbers)
