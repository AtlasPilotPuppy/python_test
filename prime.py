#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Michael John
# Usage: python prime.py [options]



"""Write a program to find the 10 001st prime number using the sieve of
aristothanes."""

'''The algorithm design does the following:
    1) Create a list of consecutive integers from 2 to 10 million.
    2) Set p=2 as the first prime number
    3) Starting from p, enumerate its multiples, and mark them in the list
    4) Find the first number greater than p not marked. This is the next
        prime number. Repeat starting back at step 3.
'''


from optparse import OptionParser, OptionGroup
import sys

SEARCH_MAX = 1000000   #just a randomly chosen default
NPRIME_NUMBER = 10001 #default prime number to return


def define_options(parser):
    '''Defind options to set for this script'''
    # Max search
    parser.add_option("-m", "--max", dest="max", type="int",
            default=SEARCH_MAX, action="store",
            help="Max integer to search up to for Primes [default: %default]")
    # Nth Prime
    parser.add_option("-p", "--prime", dest="nprime", type="int",
            default=NPRIME_NUMBER, action="store",
            help="Nth Prime number to find [default: %default]")
    # Verbose flag
    parser.add_option("-v", "--verbose", dest="verbose",
            action="store_true", help="More output")

    # Example section
    group_ex = OptionGroup(parser, "Examples","")
    group_ex1 = OptionGroup(parser, "To find the 10,001st Prime number",
            "prime.py -p 10001")
    parser.add_option_group(group_ex)
    parser.add_option_group(group_ex1)



if __name__ == '__main__':
    parser = OptionParser()
    define_options(parser)
    (options, args) = parser.parse_args()

    if options.verbose:
        print("Max Search limit: {0}".format(options.max))
        print("Looking for the {0} Prime".format(options.nprime))

    # Define variables before algorithm
    PRIME = 1       # Constant: ID for a prime
    NOT_PRIME = 0   # Constant: ID for a non prime
    prime_list = [] # list of prime numbers
    num_list = []   # list of consecutive integers

    # Create list of consecutive integers
    for x in range(2, options.max):
        # Initially all index are set as primes
        num_list.append([x, PRIME])

    # Start of algorithm, find the Primes
    for index in num_list:
        if index[1] == NOT_PRIME:
            continue
        prime_list.append(index[0])
        p = index[0]
        mult = 2 #multiple, start at 2, then 3,4,5,... till out-of-bounds
        while p*mult-2 < len(num_list):
            num_list[p*mult-2][1] = NOT_PRIME
            mult = mult + 1

    # Finished, see if we were able to find what the user wanted
    if options.nprime-1 > len(prime_list):
        print("Could not find the {0} prime number.".format(options.nprime))
        print("Try increasing the search limit. (Option: '-max=')")
    else:
        print("The {0} Prime Number: {1}".format(options.nprime,
            prime_list[options.nprime-1]))
