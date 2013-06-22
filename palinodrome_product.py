#!/usr/bin/env python

"""A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 99.Find the largest
palindrome made from the product of two 3-digit numbers."""

# an unadorned 'digit' term implies base-ten

# First order the products.
#
# For a nonnegative integers, n,i,j, such that 0 <= i,j <= n, find the ordering
# of the products of any two integers of the form:
#
# (n - i)*(n - j) = n**2 - (i + j)*n + i*j
#
#

def check(prod):
  print prod
  prod_str = str(prod)
  length = len(prod_str)
  if length%2 == 1: # odd number of digits
    for digit in xrange(length/2):
      if prod_str[digit] != prod_str[-(digit + 1)]:
        return False # return on first inequality
    # don't need to check if middle digit == middle digit
  else: # even number of digits
    for digit in xrange(length/2):
      if prod_str[digit] != prod_str[-(digit + 1)]:
        return False # return on first inequality
  return True # palindrome

def find(n=99):
  if check(n*n):
    print(n*n) # success
  elif check(n*(n - 1)):
    print(n*(n - 1)) # success
  elif n > 0: # don't recurse to -\infty
    find(n - 1) # try again

if __name__ == '__main__' : find()
