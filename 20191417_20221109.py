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

# ex 8-7
from math import pow, sqrt

a = pow(2, 3)
b = sqrt(4)

print('m.pow(2, 3) = ', a)
print('sqrt(4) = ', b)

# ex 8-8
from math import pow as p

a = p(2, 3)

print('p(2, 3 = ', a)

# ex 8-9
from math import pow as p, sqrt as s

a = p(2, 3)
b = s(4)
print('p(2, 3) = ', a)
print('s(4) = ', b)

# ex 8-10
import importlib
import math

importlib.reload(math)
# print(dir(math))

import plusminus
print(plusminus.plus(1, 2))

importlib.reload(plusminus)
import plusminus
# # del plusminus

# ex 8-18
text = '동승현!!'
with open('python.txt', 'w') as p:
    p.write(text)

# ex 8-20
import pickle

list = ['a', 'b', 'c']
with open('list.txt', 'wb') as f:
    pickle.dump(list, f)

with open('list.txt', 'rb') as f:
    data = pickle.load(f) # 한 줄씩 읽어옴

print(data)

# ex 8-23
import mymod

print('PI = ', mymod.PI)
a = mymod.Circle()
print('반지름이 5일 때 원의 넓이 = ', a.com1(5))

print(mymod.com2(2, 3))