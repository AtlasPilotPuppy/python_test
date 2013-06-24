#!/usr/bin/env python
"""Complete this program to find the greatest produdct of five consecutive
digits in the list"""

def product(iterable):
  '''
  returns the product of the numbers in iterable
  '''
  prod = 1
  for i in iterable:
    prod *= i
  return prod

def result(num,array,prods,skeys):
  '''
  prints results
  num:   number of consecutive digits in products
  array: array of digits
  prods: dictionary of consecutive products keyed by array position of first
         digit in the product
  skeys: list of keys of prods rsorted by product
  '''
  out = 'The greatest product of %d consecutive digits in the list is ' % num
  out += '%d.  ' % prods[skeys[0]]
  maxes = [skeys[0]] # how many times greatest product occurs
  for i in xrange(len(skeys) - 1): # don't overrun if all products are equal
    if prods[skeys[i]] == prods[skeys[i + 1]]:
      maxes.append(skeys[i])
    else:
      break # found all of them
  out += 'It occurs %d time%s.  ' % (len(maxes),'' if len(maxes) == 1 else 's')
  out += 'The consecutive digits are:\n\n'
  for m in maxes:
    digits = tuple([array[m + i] for i in xrange(num)])
    out += ('  %s\n' % ('%d '*num).rstrip()) % digits
  print(out)

def consecutive_product(num=5):
  array = [] # array of input digits
  with open('array.txt') as in_file:
    for line in in_file:
      digits = line.rstrip('\n') # remove trailing newline
      array.extend([int(d) for d in digits])
  prods = {} # computed products keyed by array position of starting digit
  for i in xrange(len(array) - num): # iterate over possible consecutive products
    prods[i] = product(array[i:i + num]) # each slice of num digits
  skeys = sorted(prods,key=prods.get,reverse=True) # sort by product
  result(num,array,prods,skeys) # print results

if __name__ == '__main__' : consecutive_product()
