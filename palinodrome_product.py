"""A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 99.Find the largest
palindrome made from the product of two 3-digit numbers."""

h=0
for a in xrange(999, 0, -1):
    for b in xrange(999, 0, -1):
        c = a * b
        d, e = len(str(c)) / 2, str(c)
        f, g = e[:d:], e[d:][::-1]
        if c > h and f == g:
            h = c
print h