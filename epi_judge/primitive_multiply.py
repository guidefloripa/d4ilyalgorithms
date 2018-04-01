# https://www.geeksforgeeks.org/add-two-numbers-without-using-arithmetic-operators/
def add(x, y):
    while y != 0:
        carry = x & y
        x ^= y
        y = carry << 1
    return x

# https://www.geeksforgeeks.org/russian-peasant-multiply-two-numbers-using-bitwise-operators/
def multiply(x, y):
    result = 0
    while y != 0:
        if y & 1:
            #result += x
            result = add(result, x)
        x <<= 1
        y >>= 1
    return result


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(generic_test.generic_test_main('primitive_multiply.tsv', multiply))
