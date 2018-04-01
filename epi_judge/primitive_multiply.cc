#include "test_framework/generic_test.h"

// https://www.geeksforgeeks.org/add-two-numbers-without-using-arithmetic-operators/
static unsigned long long Add(unsigned long long x, unsigned long long y) {
    unsigned long long carry;
    while (y != 0) {
        carry = x & y;
        x ^= y;
        y = carry << 1;
    }
    return x;
}

// https://www.geeksforgeeks.org/russian-peasant-multiply-two-numbers-using-bitwise-operators/
unsigned long long Multiply(unsigned long long x, unsigned long long y) {
    unsigned long long result = 0;
    while (y != 0) {
        if (y & 1)
            //result += x;
            result = Add(result, x);
        x <<= 1;
        y >>= 1;
    }
    return result;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x", "y"};
  return GenericTestMain(args, "primitive_multiply.tsv", &Multiply,
                         DefaultComparator{}, param_names);
}
