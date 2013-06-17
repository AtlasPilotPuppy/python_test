"""Complete this program to find the greatest product of five consecutive
digits in the list"""


class GreatestProductFinder(object):
    """
    This class is used to find the greatest product of the values within a file
    """
    def __init__(self, start=0, end=5):
        self.start = start
        self.end = end

    def _product_of_numbers(self, string):
        """
        This function finds the product of a string of numbers and returns it
        """
        product = 1
        for i in string:
            try:
                product *= int(i)
            except ValueError:
                print "Your file of numbers cannot contain letters."
                product = 0
                break
        return product, string

    def _greatest_product_in_line(self, line):
        """
        This function finds the greats product from the line of numbers and returns it, you can specify the length of
        the digits if you like by specifying start and end when you instantiate the class.
        """
        start = self.start
        end = self.end
        greatest = (0, '')
        current_line = line[start:end]
        while '\n' not in current_line or '' not in current_line:
            current_product = self._product_of_numbers(current_line)
            greatest = max(current_product, greatest)
            start += 1
            end += 1
            current_line = line[start:end]
        return greatest

    def greatest_product_from_file(self, file_name):
        """
        This function finds the greatest product from the file
        """
        greatest_line = 0
        with open(file_name, 'r') as reader:
            for line in reader.readlines():
                current_line = self._greatest_product_in_line(line)
                greatest_line = max(current_line, greatest_line)
            reader.close()
        return greatest_line

greatest_product_finder = GreatestProductFinder(0, 5)
greatest = greatest_product_finder.greatest_product_from_file('array.txt')
print "Greatest Product: ", str(greatest[0]), " from these numbers:", greatest[1]
