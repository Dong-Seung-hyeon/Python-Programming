# ex 3-0
s1 = 'Computer'
s2 = 'Engineering'
print(s1 + '  '+ s2 + '.')
print(s2 * 3)
print('-' * 20)
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1 + l2)
print(l1 * 3)

# ex 3-1
print('-' * 30)
print('2 ** 10 = ', 2 ** 10)
print('5 / 2 = ', 5 / 2)
print('5 // 2 = ', 5 // 2)
print('5 % 2 = ', 5 % 2)
print('5 + 2.0 = ', 5 + 2.0)
print('-20 = ', -20)
print('- -20 = ', - -20)

# ex 3-2
print('산술연산자')
print("-"*20)
a = int(input('첫 번째 정수를 입력하세요 : '))
b = int(input('두 번째 정수를 입력하세요 : '))
print('a = ', a)
print('b = ', b)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
print("-"*20)

# ex 3-3
print('산술연산자')
print("-"*20)
a = int(input('첫 번째 정수를 입력하세요 : '))
b = int(input('두 번째 정수를 입력하세요 : '))
print('a = ', a)
print('b = ', b)
print("{0} + {1} = {2}".format(a, b, a+b))
print("{0} - {1} = {2}".format(a, b, a-b))
print("{0} * {1} = {2}".format(a, b, a*b))
print("{0} / {1} = {2}".format(a, b, a/b))
print("{0} // {1} = {2}".format(a, b, a//b))
print("{0} % {1} = {2}".format(a, b, a%b))
print("{0} ** {1} = {2}".format(a, b, a**b))
print("-"*20)

# ex 3-4
print('산술연산자')
print("-"*20)
a = int(input('첫 번째 정수를 입력하세요 : '))
b = float(input('두 번째 정수를 입력하세요 : '))
print('a = ', a)
print('b = ', b)
print("{0} + {1} = {2}".format(a, b, a+b))
print("{0} - {1} = {2}".format(a, b, a-b))
print("{0} * {1} = {2}".format(a, b, a*b))
print("{0} / {1} = {2}".format(a, b, a/b))
print("{0} // {1} = {2}".format(a, b, a//b))
print("{0} % {1} = {2}".format(a, b, a%b))
print("{0} ** {1} = {2}".format(a, b, a**b))
print("-"*20)

# ex 3-5
print(9/2)
print(9/-2)
print(9//-2)
print(9%-2)
print(-9/2)
print(-9//2)
print(-9%2)

# ex 3-6
x = 5
x += 2
print(x)
x -= 2
print(x)
x *= 2
print(x)
x /= 2 # x = x/2
print(x)
x **= 2 # x = x ** 2
print(x)
x //= 2
print(x)
x %= 2
print(x)

# ex 3-7
birth = int(input('생년월일을 입력하세요 : '))
year = birth // 10000
month1 = birth % 10000 // 100
month2 = birth // 100 % 100
date = birth % 100
print(year, month1, date)
print("생년월일 : {}년 {}월 {}일".format(year, month2, date))