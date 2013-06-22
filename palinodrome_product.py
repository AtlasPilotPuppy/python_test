#!/usr/bin/env python

"""A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 99.Find the largest
palindrome made from the product of two 3-digit numbers."""

# an unadorned 'digit' term implies base-ten

# http://stackoverflow.com/questions/4643647/fast-prime-factorization-module
from primefactorization import primefactors

def check(prod):
  '''
  check if prod is a palindrome
  '''
  if str(prod) == str(prod)[::-1]:
    return True # palindrome
  else:
    return False # not palindrome

def find(n,m,found):
  '''
  Find largest base-ten palindrome in the set of integers {0,...,n**2} by
  checking products of the form (n - i)*(n - j), where 0 <= i,j <= n are
  integers.  Recurse over the product set from largest to smallest.
  n:     starting number
  m:     size of domain of input sets over which to search for a palindrome in
         the product set
  found: collect found palindromes
  '''
  if not isinstance(found,set):
    raise TypeError('found argument must be of type set')
  for i in xrange(m):              # iterate over i
    for j in xrange(m):            # and j
      if check((n - i)*(n - j)):
        found.add((n - i)*(n - j)) # success
  if len(found) > 0:               # found at least one between n,n - m
    return
  elif n - m > 0:                  # only check positive input integers
    find(n - m,m,found)            # look at next part of input sets
  else:
    pass
    '''
    a single digit positive integer is a palindrome, and not all single digit
    integers are prime, so the algorithm will always find a palindrome of the
    form (n - i)*(n - j) for any nonnegative integers 0 <= i,j <= n.
    '''

def main(n=999,m=100):
  '''
  n: the largest positive integer used to find palindromes
  m: estimated range of numbers less than n needed to find the largest
     palindrome, [n,n - m]
  '''
  f = set()           # store found palindromes here
  find(n,m,f)         # find palindromes
  pal = sorted(f)[-1] # largest palindrome found given params n,m
  facts = primefactors(pal,True)
  length = len(facts)
  output = 'Largest palindrome in range [0,%d**2]: %d\n' % (n,pal)
  output += 'Its prime factorization is: %s\n' % facts
  output += 'These can be combined in 2**%d = %d different ' % (length,2**length)
  output += 'ways to find the palindrome as a product of two integers in the '
  output += 'range [0,%d].' % n
  print output

if __name__ == '__main__' : main()
