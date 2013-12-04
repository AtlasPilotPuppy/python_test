#!/bin/env python2.7

"""Write a program to find the 10 001st prime number using the sieve of
aristothanes."""

"""
Algorithm for Sieve of Eratosthenes modified to stop when the 10,001st prime
has been found.

Author:
    Eric Saupe
"""

#Initialize variables.
#We set the list to be large to ensure we get 10001 prime numbers
numbers = [True] * 250000
#0 and 1 should not be used in the calculation of primes
numbers[0] = False
numbers[1] = False
#Keep track of the primes we've found so we can stop early
primes = []

for (i, prime) in enumerate(numbers):
    #If prime, save it and mark all multiples of it as not prime
    if prime:
        primes.append(i)
        for j in range(i * i, 250000, i):
            numbers[j] = False
    #If we have reached our limit, stop
    if len(primes) == 10001:
        print '%s is the 10,001st prime number' % primes[-1]
        break
