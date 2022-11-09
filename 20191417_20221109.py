# ex 8-1
# import math
# print(dir(math))

#ex 8-2
def factorial(n):

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

print("5! = ", factorial(5))

# ex 8-3
import math

a= math.factorial(5)
print("5! = ", a)

from math import factorial
a= factorial(5)
print("5! = ", a)

# ex 8-4
from math import comb
# from math import *
b = comb(5, 2)
print('5 Combination 2 = ', b)

# ex 8-6
from math import *
print(pi)

