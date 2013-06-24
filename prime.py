#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""Write a program to find the 10 001st prime number using the sieve of
aristothanes."""

'''
sieve of Eratosthenes (κόσκινον Ἐρατοσθένους)?
'''
from math import sqrt

start = 2        # beginning integer of search range
stop = 8000      # ending integer of search range
target = 10001   # number of primes to find
integers = []    # list of integers
primes = []      # list of primes

def remove_factors(p,integers):
  '''
  removes all factors of prime p from integers, where 1 < p*i < integers[-1]
  '''
  imin = integers[0]       # smallest integer in range
  imax = integers[-1]      # largest integer in range
  smallest = max(imin/p,2) # minimum integer that will have factors that land in
                           # the provided integer list
  largest = imax/p + 1     # largest of these integers
  for i in xrange(smallest,largest):
    factor = p*i
    if factor in integers:
      integers.remove(factor)
    elif factor > imax:
      break

def sieve(start=start,stop=stop):
  '''
  Given a set of positive integers, remove all integer products of known
  primes, since they are thus not prime.  When p is less than sqrt(stop) + 1,
  then all the remaining integers the current range of integers are prime.
  Recurse until the range containing p_target is processed and return that
  prime.
  start: starting integer
  stop:  ending integer
  '''
  integers = [i for i in xrange(start,stop)]
  if len(primes) == 0:                  # base case
    p = start                           # initial working prime
  else:
    for p in primes:                    # first check primes we know
      if p < int(sqrt(stop) + 1):
        remove_factors(p,integers)
    p = integers[0]                     # first integer left is now prime
  while p < int(sqrt(stop) + 1):        # then sift through the new primes
    remove_factors(p,integers)          # remove all factors of p from integers
    p = integers[integers.index(p) + 1] # next integer in integers is now prime
  primes.extend(integers)               # all remaining integers are primes
  if len(primes) < target:              # need to look for more primes
    sieve(stop,2*stop)                  # look at the next range of integers
  else:                                 # found p_target
    print('The %dst prime is %d' % (target,primes[target + 1]))

if __name__ == '__main__' : sieve()
