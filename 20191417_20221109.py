# ex 8-1
import math
print(dir(math))

def factorial(n):

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

print("5! = ", factorial(5))