#!/usr/bin/env python

import argparse
import sys
from primes.sieves import WheelSieve

desc = '''Find the nth prime number using the sieve of Eratosthenes'''

parser = argparse.ArgumentParser(description=desc)
parser.add_argument('nth', metavar='n', type=int,
                    help='\'n\' as in the nth prime number')
args = parser.parse_args()


if args.nth < 1:
    msg = 'Must specify an number greater than 0'
    raise argparse.ArgumentTypeError(msg)

if args.nth > 1000000:
    msg = 'Umm... that\'s a really big number... maybe try something smaller?'
    raise argparse.ArgumentTypeError(msg)


primes = WheelSieve().sieve()
last_prime = 0
for i in xrange(args.nth):
    last_prime = primes.next()

msg = '''The nth prime for n={0:,} is {1:,}'''

print msg.format(args.nth, last_prime)
