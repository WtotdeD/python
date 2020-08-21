

# We define an S-number to be a natural number, n, that is a perfect square 
# and its square root can be obtained by splitting the decimal representation of n into 2 or more numbers 
# then adding the numbers.

# For example, 81 is an S-number because  wortel 81 =8+1.
# 6724 is an S-number: wortel 6724= 6+72+4.
# 8281 is an S-number: wortel 8281=8+2+81=82+8+1.
# 9801 is an S-number: wortel 9801=98+0+1.

# Further we define T(N) to be the sum of all S numbers n≤N. You are given T(104)=41333.

# Find T(1012)

import math


#lBasis for looping through number until condition is

# i = 1
# while i <= 10:
#     print(math.sqrt(i))
#     i += 1


#take the root of the input numbers (6724, 8281, 9801, 81)
print("Lets take the root of the input numbers")

print(math.sqrt(6724))
print(math.sqrt(8281))
print(math.sqrt(9801))
print(math.sqrt(81))

# https://docs.python.org/3/library/itertools.html#itertools.combinations

i = 1

while i < 100:
    print(i * i)
    i += 1
