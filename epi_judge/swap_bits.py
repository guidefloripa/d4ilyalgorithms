def swap_bits(x, i, j):
    bit_i = (x >> i) & 1
    bit_j = (x >> j) & 1

    swap_bit = bit_i ^ bit_j
    if not swap_bit:
        return x

    mask = (swap_bit << i) | (swap_bit << j)
    return x ^ mask


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(generic_test.generic_test_main('swap_bits.tsv', swap_bits))
