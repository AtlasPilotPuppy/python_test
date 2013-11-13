from collections import namedtuple


Range = namedtuple('Range', ['low', 'high'])


class Results:

    def __init__(self, palindrome, factor1, factor2):
        self.palindrome = palindrome
        self.factor1 = factor1
        self.factor2 = factor2


def reverse_num(num):
    if num < 0:
        return None
    rev = 0
    while num != 0:
        rev = rev * 10 + num % 10
        num = num / 10
    return rev


def range_for_n_digit_nums(n):
    return Range(low=10 ** (n - 1), high=10 ** n)


def generate_palindromes(num_digits):
    palindromes = []
    factor_range = range_for_n_digit_nums(num_digits)
    uppers = range(factor_range.low, factor_range.high)
    uppers.reverse()
    upper_bound = factor_range.high * factor_range.high
    for u in uppers:
        palindrome = (u * factor_range.high) + reverse_num(u)
        if palindrome <= upper_bound:
            palindromes.append(palindrome)

    return palindromes


def largest_palindrome(num_digits):
    factor_range = range_for_n_digit_nums(num_digits)
    palindromes = generate_palindromes(num_digits)
    factors = range(factor_range.low, factor_range.high)
    factors.reverse()
    for palindrome in palindromes:
        for factor in factors:
            if palindrome % factor == 0:
                if factor_range.low <= palindrome / factor < factor_range.high:
                    return Results(palindrome, factor, palindrome / factor)
