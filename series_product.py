"""Complete this program to find the greatest produdct of five consecutive
digits in the list"""

def string_product(string):
    """
    Return the product of the integers in string.

    Argument:
        string -- a string containing only integers.

    Example:

    >>>  string_product('123')
    6
    
    """
    product = 1

    for i in range(len(string)):
        product *= int(string[i])

    return product



def max_consecutive_product(string, length):
    """
    Iterate over string and find the largest product of a substring with the
    given length.

    Arguments:
        string -- string containing only integers.
        length -- size of substring to consider.

    Example:
    >>> max_consecutive_product('12345', 2)
    20

    """
    max_product = 0

    for i in range(len(string)-length+1):
        sub = string[i:i+length]
        product = string_product(sub)
        if product > max_product:
            max_product = product

    return max_product

if __name__ == "__main__":
    max_product = 0

    # open the file
    with open('array.txt') as in_file:
        # Concatenating the current line with the last 4 characters of the 
        # previous line allows us to consider the product of 5  consecutive 
        # characters spanning those two lines.
        prev_line = ''  # initial empty line
        for line in in_file:
            # needle will be the string we actually iterate through to find
            # the max product. 
            line = line.strip()
            needle = prev_line + line

            # save the last 4 characters of the line for the next stage
            if len(line)>4:
                prev_line = line[-4:]
            else:
                prev_line = line

            # look for the max
            product = max_consecutive_product(needle, 5)
            if product > max_product:
                max_product = product

    print "The greatest product of 5 consecutive digits in the list is\
    {}".format(max_product)
