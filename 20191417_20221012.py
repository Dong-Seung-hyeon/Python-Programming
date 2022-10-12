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
for i in range(1):
    print('* ' * x)     
    for j in range(y-1):        
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