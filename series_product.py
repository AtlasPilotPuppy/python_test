#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Michael John
# Usage: python series_product.py

"""Complete this program to find the greatest product of five consecutive
digits in the list"""


def consecutive_product(digits):
    '''Calculates the product of the consecutive digits
        Param: digits  -list or tuple
    '''
    return reduce(lambda x,y: x*y, digits)


if __name__ == '__main__':
    in_file = open('array.txt')

    intlist = [] # our list of integers

    # Read each line in the file and store it as a list of integers
    for line in in_file.readlines():
        l = list(line.rstrip())  # convert string to list
        intlist.extend([int(x) for x in l]) # convert chars to ints and store

    # Finished with the file
    in_file.close()

    # start at 0 and send to function that produces product of 5 digits
    # if higher than max, save five digits
    start = 0
    end = len(intlist) - 5 #end is the last sequence of 5 digits
    pmax = 0        #max product found
    pseq = None     #sequence that produces max product

    while start != end:
        prod = consecutive_product(intlist[start:start+5])
        if prod > pmax:
            pseq = intlist[start:start+5]
            pmax = prod
        start = start + 1  #slide window forward by one

    # Finished
    print("Max product: {0}     {1}".format(pmax, pseq))

