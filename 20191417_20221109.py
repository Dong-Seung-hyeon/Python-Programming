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
