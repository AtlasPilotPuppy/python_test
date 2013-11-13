import pytest
from palindrome.products import *


class TestPalindromes:

    @pytest.mark.parametrize(("value", "expected_low", "expected_high"), [
        [2, 10, 100],
        [3, 100, 1000],
        [4, 1000, 10000], ])
    def test_range_for_n_digit_nums(self, value, expected_low, expected_high):
        r = range_for_n_digit_nums(value)
        assert r.low == expected_low and r.high == expected_high

    def test_palindromes(self):
        assert generate_palindromes(num_digits=3)

    def test_palindrome_range(self):
        palindromes = generate_palindromes(num_digits=3)
        assert len(palindromes) == 900
        for p in palindromes:
            assert p > 100000 and p < 1000000

    @pytest.mark.parametrize(("value", "expected"), [
        [411, 114],
        [515, 515],
        [666, 666],
        [723, 327], ])
    def test_reverse_num(self, value, expected):
        assert reverse_num(value) == expected

    @pytest.mark.parametrize(("value", "expected"), [
        [2, 9009],
        [3, 906609], ])
    def test_largest_palindrome(self, value, expected):
        assert largest_palindrome(value).palindrome == expected
