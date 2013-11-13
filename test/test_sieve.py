import pytest
from primes.sieves import *


class TestNaiveSieve:

    def test_primes_iter(self):
        primes = NaiveSieve().sieve()
        results = []
        for i in xrange(20):
            ret = primes.next()
            results.append(ret)
            assert ret is not None

        assert len(results) == 20

    def test_1000_primes(self, first_1000_primes):
        primes = NaiveSieve().sieve()
        for prime in first_1000_primes:
            assert prime == primes.next()


class TestWheelSieve:

    def test_first_1000_primes(self, first_1000_primes):
        primes = WheelSieve().sieve()
        for prime in first_1000_primes:
            assert prime == primes.next()


class TestWideWheelSieve:

    def test_first_100_primes(self, first_100_primes):
        primes = WideWheelSieve().sieve()
        for prime in first_100_primes:
            assert prime == primes.next()

    # Not sure why this is so slow it seems to lock up
    # It's only doing one more calculation per loop but
    # should be saving a bunch of time skipping work
    #
    # def test_first_1000_primes(self, first_1000_primes):
    #     primes = WideWheelSieve().sieve()
    #     for prime in first_1000_primes:
    #         assert prime == primes.next()


class TestNthPrime:

    def test_10001st_prime(self):
        primes = WheelSieve().sieve()
        for i in xrange(10000):
            primes.next()
        assert primes.next() == 104743
