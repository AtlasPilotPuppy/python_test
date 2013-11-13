# Python Challenge


## Overview

Some programming exercises

### Sieve / Primes

Relied heavily on this [paper](http://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf). Executes in under 20 seconds on my machine when asking for the 1 millionth prime.

 - Implemented the 'failful sieve' according to that paper in three incarnations
   - Naive - tries all candidates (including evens) up to p^2
   -  Used wheel skipping multiples of 2 & 3
   -  Used wheel skipping multiples of 2, 3 & 5 (however, something did not perform well in this implementation)
 - Other optimizations included
   - Uses lazy iteration described in the paper. Does not generate all multiples of p up to limit but only as needed.
 - Optimizations not attempted
   - Composites managed with priority queue. The paper indicated that a priority queue yielded large performance increases. However, after reading [this answer](http://stackoverflow.com/questions/13463417/the-genuine-sieve-of-eratosthenes-in-python-why-is-heapq-slower-than-dict) on stackoverflow  it seems a plain dict is probably just as fast and possibly better.

### Palindrome

The approach taken avoids making a brute force attempt at combing all n-digit numbers and testing for palindrome. Instead, it first generates the list of all palindromes for the expected range and then tests for factors in the n-digit range. This seems like a good approach since the number of palindromes grows slowly in relation to the number of digits in the products.

Other points of interest in the implementation:
 - Implemented a function which takes the number of digits of the factors as a parameter. Tested for n=2 & 3. It should work for larger n without modification.
 - Avoided testing for palindrome-ness or manipulating the data as strings
 - Next optimization that I would address would be to avoid brute forcing the n-digit factor testing of palindromes. For large n this could be expensive. Going after prime factors might be a sensible next step.

## Installation

### Manual installation

#### Virtualenv
Recommended that you create a virtualenv to install this code and it's dependencies into.

See [virtualenv docs](https://pypi.python.org/pypi/virtualenv)

#### Run the install
You can install the code simply by running

`python setup.py test` 

If the tests pass proceed with the intsall. Execute

`python setup.py install` 

from the project's root directory.

## Usage

After installation the following will be available on your path 

`nth-prime.py n`

You can run it without arguments to get a help message or specify an integer of reasonable size to see what the nth prime is.

`palindrome-product.py`


## Testing
You can run the automated tests with

`python setup.py test`

If the package is already installed there might be some conflicts. You can usually clean these up by deleting the build directory

`rm -rf build/`

from the project's root directory.

The run tests from setup.py or by `py.test`

## Information

Source: https://github.com/lakeslc/python_test

Authors: [Jonathan Randall](https://github.com/lakeslc/)
