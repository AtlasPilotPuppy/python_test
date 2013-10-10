"""Write a program to find the 10 001st prime number using the sieve of
aristothanes."""

from math import log

# which prime do we want to find
find = 10001

# as a consqeuence of the prime number theorem a rough (but close) estimate
# of the nth prime is given below.
limit = find * int(log(find) + log(log(find))+1)

# list of appropriate length to contain all the primes we need
# start by assuming they are prime, the sieve will mark which are 
# not prime. 
p = [True] * limit

# mark 0 and 1 as not prime.
p[0] = p[1] = False

# apply the sieve to our list of numbers
for i, is_prime in enumerate(p):
    if is_prime:
        for n in xrange(2*i, limit, i):
            p[n] = False

# create a list containing only the primes, so primes[0] = 2.
primes = [ i for i, b in enumerate(p) if b]

print "The {:,} prime is {:,}.".format(find, primes[find-1])

