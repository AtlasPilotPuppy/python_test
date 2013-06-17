"""A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 99.Find the largest
palindrome made from the product of two 3-digit numbers."""


class PalindromeFinder(object):
    """
    PalindromeFinder will help you find the largest palindrome from the product of two numbers you determine the amount
    of digits the power is yours! PEP8!
    """
    def __init__(self, smallest_number, largest_number):
        self.smallest_number = smallest_number
        self.largest_number = largest_number

    def _is_palindrome(self, string):
        """
        takes in a string and determines if it is a paldindrome
        """
        return string[0:len(string)/2][::-1] == string[len(string)/2:len(string)]

    def _find_palindromes(self):
        """
        finds all palindromes created from product of two numbers between smallest_number and largest_number.
        """
        try:
            possible_numbers_1 = (x for x in xrange(self.smallest_number, self.largest_number))
            for first_number in possible_numbers_1:
                possible_numbers_2 = (x for x in xrange(self.smallest_number, self.largest_number))
                for second_number in possible_numbers_2:
                    product = first_number * second_number
                    if self._is_palindrome(str(product)):
                        yield (product, (first_number, second_number))
        except (ValueError, TypeError):
            print "*ERROR* Start and End values must be integers."
            yield 0,(0,0)

    def find_largest_palindrome(self):
        """
        finds the largest palindrome that can be created from the product of 2 numbers between smallest_number and
        largest_number
        """
        return max(self._find_palindromes())


palindrome_finder = PalindromeFinder(100, 1000)
greatest = palindrome_finder.find_largest_palindrome()
print str(greatest[0]), '==', str(greatest[1][0]), '*', str(greatest[1][1])