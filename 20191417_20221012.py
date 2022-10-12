# ex 4-18
from platform import java_ver


L_1 = ['one', 'two', 'three']
for i in L_1 :
    print(i)
L_2 = [(1, 5), (2, 6), (3, 7)]
for (a, b) in L_2 :
    print(a + b)

# ex 4-19
score = [90, 25, 67, 45, 80]
number = 0
for s in score:
    number = number +1
    if s >= 60:
        print("%d번 학생의 점수는 %d점이며 합격입니다." % (number, s))
    else:
        print("%d번 학생의 점수는 %d점이며 불합격입니다." % (number, s))

# ex 4-20
score = [90, 25, 67, 45, 80]
number = 0
for s in score:
    number = number +1
    if s < 60:
        continue
    print("%d번 학생 %d점으로 합격합니다. 축하합니다!" % (number, s))

# ex 4-21
sxore = [25, 90, 67, 45, 80]
number = 0
for s in score:

    number = number +1
    if s >= 60:
        print("%d번 학생 축하합니다. 합격입니다." % number)
        break

# ex 4-22
x = int(input('숫자를 입력하세요 : '))
for i in range(1, x+1):
    print('⭐️ ' * i)
    
# ex 4-23
x = int(input('숫자를 입력하세요 : '))
for i in range(x, 0, -1) :
    print('⭐️ ' * i)

# ex 4-24
x = int(input('가로의 숫자를 입력하세요 : '))
y = int(input('세로의 숫자를 입력하세요 : '))
for i in range(0,y):
    print('* ' * x) 
print()

# ex 4-25
x = int(input('숫자를 입력하세요 : '))
for i in range(1, x+1, 1):
    print((x-i) * ' '+'★ '* i)

# ex 4-26
x = int(input('숫자를 입력하세요 : '))
for i in range(1, x+1) :
    if not (i % 5 == 0):
        print(i, end = ' ')
print()

# ex 4-27
x = int(input('숫자를 입력하세요 : '))
a = 2
for i in range(0, x + 1) :
    print('{0:6,}'.format(a ** i), end=' ')
print()

x = int(input('숫자를 입력하세요 : '))
a = 1
for i in range(0, x + 1):
    print('{0:6,}'.format(a << i), end=' ')
print()

# ex 4-28
num = 0
while num < 5 :
    print('파이썬 프로그래밍!')
    num += 1

# ex 4-29
num = int(input('반복할 횟수 : '))
i = 0
while i < num :
    print('파이썬 ')

# ex 4-30
i, hap = 0, 0
num1, num2, num3 = 0, 0, 0
num1 = int(input('시작 값을 입력하세요 : '))
num2 = int(input('끝깞을 입력하세요 : '))
num3 = int(input('증감값을 입력하세요 : '))
i = num1
while i < num2+1 :
    hap = hap + i
    i = i + num3
print("%d에서 %d까지 %d씩 증가시킨 값의 합계 : %d" % (num1, num2, num3, hap))

# ex 4-31
import random
i = 0
while i != 5:
    i = random.randint(1, 6)
    print(i)
print('드디어 ', i, '가 나왔네요~~')

# ex 4-32
hap, a, b = 0, 0, 0
while True :
    a = int(input("첫 번째 수를 입력하세요(0을 입력하면 종료) : "))
    if a == 0 :
        break
    b = int(input("두 번째 수를 입력하세요 : "))
    hap = a + b
    print("%d + %d = %d" % (a, b, hap))

print("0을 입력해 반복문을 탈출했습니다")