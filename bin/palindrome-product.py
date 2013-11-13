#!/usr/bin/env python

import sys
import datetime
from datetime import timedelta
from palindrome.products import largest_palindrome

desc = '''Find the largest palindrome made from the\
product of two 3-digit numbers.'''

start = datetime.datetime.now()
result = largest_palindrome(3)
finish = datetime.datetime.now()

msg = '''That largest palindrome with two 3-digit factors is {0:,}
It's factors are {1} & {2}
Finished in {3} milliseconds'''

delta = finish - start
print msg.format(result.palindrome,
                 result.factor1,
                 result.factor2,
                 (delta.seconds * 1000) + (delta.microseconds/1000.0))
