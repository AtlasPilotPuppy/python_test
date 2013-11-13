import itertools

# Thanks to Jach for this gist giving the baseline implementations for
# the candidate and sieve generators
# https://gist.github.com/Jach/1761175


class SieveGenerator:

    def sieve(self):
        return self.sieve_generator


class NaiveSieve(SieveGenerator):

    def __init__(self):
        self.sieve_generator = self.naive_sieve(
            self.naive_candidate_generator(2))

    def naive_candidate_generator(self, start):
        n = start
        while True:
            yield n
            n += 1

    def naive_sieve(self, candidate_generator):
        composites = {}
        while True:
            x = candidate_generator.next()
            if x not in composites:
                yield x
                composites[x*x] = [x]
            else:
                for prime in composites[x]:
                    composites.setdefault(x + prime, []).append(prime)
                del composites[x]


class WheelSieve(SieveGenerator):

    def __init__(self):
        self.sieve_generator = self.wheel_sieve(
            self.wheel_candidate_generator(5))

    def wheel_candidate_generator(self, start):
        yield 2
        yield 3

        n = start
        wheel = itertools.cycle([2, 4])
        while True:
            yield n
            n += wheel.next()

    def wheel_sieve(self, candidate_generator):
        composites = {}
        while True:
            x = candidate_generator.next()
            if x not in composites:
                yield x
                composites[x*x] = [x]
            else:
                for prime in composites[x]:
                    composites.setdefault(x + prime * 2, []).append(prime)
                    composites.setdefault(x + prime * 4, []).append(prime)
                del composites[x]


class WideWheelSieve(SieveGenerator):

    def __init__(self):
        self.sieve_generator = self.wide_wheel_sieve(
            self.wide_wheel_candidate_generator(7))

    def wide_wheel_candidate_generator(self, start):
        yield 2
        yield 3
        yield 5

        n = start
        wheel = itertools.cycle([4, 2, 4, 2, 4, 6, 2, 6])
        while True:
            yield n
            n += wheel.next()

    def wide_wheel_sieve(self, candidate_generator):
        composites = {}
        while True:
            x = candidate_generator.next()
            if x not in composites:
                yield x
                composites[x*x] = [x]
            else:
                for prime in composites[x]:
                    composites.setdefault(x + prime * 2, []).append(prime)
                    composites.setdefault(x + prime * 4, []).append(prime)
                    composites.setdefault(x + prime * 6, []).append(prime)
                del composites[x]
