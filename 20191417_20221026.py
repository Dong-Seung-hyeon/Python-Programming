# ex 6-1
def print_10times_star():
    print('*' * 10 )

print_10times_star()

# ex 6-2
def plus(v1, v2):
    result = 0
    result = v1 + v2
    return result

hap = plus(100, 200)
print(hap)

# ex 6-3
def plus(v1, v2):
    """이 함수는 v1과 v2를 더한 뒤 결과를 반환하는 함수입니다."""
    result = 0
    result = v1 + v2
    return result

hap = plus(100, 200)
print(hap)
print(plus.__doc__)

# ex 6-4
def add_multi(n1, n2):
    return n1 + n2, n1 * n2

result = add_multi(5, 10)
print(result)

# ex 6-5
def two_times(n):
    return print(n * 2)

two_times(5)
two_times('abc')

two_times([1, 2, 3])
two_times((1, 2, 3))

# ex 6-6
def add_print(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

add_print(1, 9)
hap = add_print(3, 4)
print(hap)

# ex 6-7
def hi():
    return "Hi 파이썬 프로그래밍"

aha = hi()
print(aha)

# ex 6-8
def hi2():
    print('Hi 파이썬 프로그래밍')

hi2()

# 매개변수와 가변매개변수

#ex 6-9
def student_info(name, phone, id_no='비공개'):
    print('이름: ', name)
    print('휴대폰: ', phone)
    print('주민번호: ', id_no)

student_info('김철수', '010-1234-5678')

# ex 6-10
def student_info(name, phone, id_no='비공개'):
    print('이름: ', name)
    print('휴대폰: ', phone)
    print('주민번호: ', id_no)

student_info('김철수', '010-1234-5678', '20200101-3145312')

# ex 6-11
# def student_info(name, id_no='비공개', phone):
#     print('이름: ', name)
#     print('휴대폰: ', phone)
#     print('주민번호: ', id_no)

# student_info('김철수', '010-1234-5678')

# ex 6-12
def add_m(*args):
    result = 0
    for i in args:
        result = result + i
    return result

r1 = add_m(1, 2, 3)
print('r1 = ', r1)

r2 = add_m(1, 2, 3, 4)
print('r2 = ', r2)

r3 = add_m(1, 2, 3, 4, 5, 6)
print('r3 = ', r3)

# ex 6-13
def value_times(times, *values):
    for value in values:
        print(times * value)

value_times(3, 1, 2, 3, 4, 5)

# 지역 변수와 전역 변수

# ex 6-14
def f_a() :
    num = 20
    print("f_a()의 num값 %d" % num)
def f_b() :
    print("f_b()의 num값 %d" % num)
num = 10
f_a()
f_b()

# ex 6-15
def f_a() :
    global num
    num = 20
    print("f_a()의 num값 %d" % num)
num = 10
f_a()
print("전역변수 num값 %d" % num)

# ex 6-16
def calc(v1, v2, op):
    result = 0
    if op == '+':
        result = v1 + v2
    elif op == '-':
        result = v1 - v2
    elif op == '*':
        result == v1 * v2
    elif op == '/':
        if v2 == 0:
            return 'error'
        else:
            result = v1 / v2
    elif op == '**':
        result == v1 ** v2
    return result

res, var1, var2, oper = 0, 0, 0, ''

while True:
    oper = input("연산자를 입력하세요( +, -, *, /, **, 종료: q ) : ")
    if oper == 'q':
        print('프로그램을 종료합니다.')
        break
    var1 = int(input("첫 번째 수를 입력하세요 : "))
    var2 = int(input("두 번째 수를 입력하세요 : "))
    res = calc(var1, var2, oper)
    if res == 'error':
        print("0으로 나누면 안됩니다.")
    else:
        print("## 계산기 : %d %s %d = %d" % (var1, oper, var2, res))

# 람다 함수

# ex 6-17
def add(n, m):

    return n + m
print(add(2, 5))

#람다함수로 작성
print((lambda n, m: n + m)(2, 5))

# ex 6-18
# reduce()를 사용하지 않는 경우
product1 = 1
list = [1, 2, 3, 4]
for num in list:
    product1 = product1 * num
print('product1 = ', product1)

# reduce()를 사용하는 경우
from functools import reduce
product2 = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print('product2 = ', product2)

# ex 6-19
from functools import reduce
def cube(y):
    return y * y * y;

g = lambda x: x * x * x
print('print(g(7)) = ', g(7))

print('print(cube(5)) = ', cube(5))

# Python code to illustrate filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
print('li = ', li)
final_list = list(filter(lambda x: (x%2 != 0), li))
print('print(final_list) = ', final_list)

# map() with lambda() to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x*2 , li))
print('print(final_list) = ', final_list)

# reduce() with lambda() to get sum of a list
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print('print(sum) = ', sum)

product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print('print(product) = ', product)