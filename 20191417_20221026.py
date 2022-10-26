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
def student_info(name, id_no='비공개', phone):
    print('이름: ', name)
    print('휴대폰: ', phone)
    print('주민번호: ', id_no)

student_info('김철수', '010-1234-5678')

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

