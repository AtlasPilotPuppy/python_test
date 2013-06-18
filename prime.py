"""Write a program to find the 10 001st prime number using the sieve of
aristothanes."""


def sieve_of_aristothanes(limit):
    
    limitn = limit + 1
    
    # Create a list of prime markers
    not_prime = [False] * limitn
    # Create a list of primes
    primes = []

    
    for x in range(2, limitn):
        # Get the next not marked # in the list
        if not_prime[x]:
            continue
        
        for f in xrange(x+x, limitn, x):
            # Mark each sequential instance in the list as not prime
            not_prime[f] = True
        
        # Add our not prime # to the list of primes
        primes.append(x)

    return primes

# adjusted the list in include at least 10001 prime numbers
primes =  sieve_of_aristothanes(200000)
print primes[10001]  # 104759

