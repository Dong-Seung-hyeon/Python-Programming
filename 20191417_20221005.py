# ex 4-1
a = int(input('1에서 100 사이의 정수를 입력하세요 : '))
if (a < 100) : 
    print('입력한 정수가 100보다 작음')
    print('a = %d' % a)

print('프로그램 종료')

# ex 4-2
a = int(input('1에서 100 사이의 정수를 입력하세요 : '))
if (a == 100) : 
    print('입력한 정수는 100입니다.')
elif(a<100) :
    print('입력한 정수가 100보다 작음')
    print('a = %d' % a)
else :
    print('입력한 a의 값은 %d이며 100보다 큼' % a)

print('프로그램 종료')

# ex 4-3
a = int(input('1에서 10 사이의 정수를 입력하세요 : '))
if (a % 2 == 0) :
    print('입력한 정수는 %d이고 짝수임' % a)
else : 
    print('입력한 정수는 %d이고 홀수임' % a)

print('프로그램 종료')

age = int(input('나이를 입력하세요: '))
if(age >= 18):
    score = int(input('점수를 입력하세요: '))
    if(score >= 80):
        print('%d점으로 합격입니다.'%score)
    else:
        print('%d점으로 불합격입니다.'%score)
else:
    print('나이가 %d세로 18살 미만으로 불합격입니다.')
print()

# ex 4-4
a = int(input('1에서 10 사이의 정수를 입력하세요 : '))
if (a >= 0) : 
    if (a == 0) :
        print('입력한 정수는 0임')
    else :
        print('입력한 정수는 %d이고 양수임' % a)
else : 
    print('입력한 정수는 %d이고 음수임' % a)

# ex 4-5
age = int(input('나이를 입력하세요 : '))
score = int(input('점수를 입려하세요 : '))
if age >= 20 :
    if score >= 80 :
        print('합격입니다!')
    else : 
        print('점수가 낮아 불합격입니다!')
else : 
    print('너무 어려서 불합격입니다!')

# ex 4-6
money = int(input('지갑에 얼마 있습니까?  '))
if money >= 3000:
    print('과자를 사먹자~~')
elif money >= 1000:
    print('껌을 사먹어야지^^')
else : 
    print('공기나 마시자 ㅠ.ㅠ')

money = int(input('지갑에 얼마 있습니까?  '))
if (money >= 10000):
    print('축제에서 사먹자~~')
elif money >= 5000:
    print('학식을 먹자')
else : 
    print('집에가서 라면먹자')

# ex 4-7
a = int(input('-10에서 10 사이의 정수를 입력하세요 : '))
if a > 10 :
    print('입력한 정수는 %d이고 10보다 큼' % a)
elif a > 0 :
    print('입력한 정수는 %d이고 양수임' % a)
elif a == 0 :
    print('입력한 정수는 0임')
elif a < -10 :
 print('입력한 정수는 %d이고 -10보다 작음' % a)
else : 
    print('입력한 정수는 %d이고 음수임' % a)

# ex 4-8
pocket = []
pocket.append(input('주머니에 있는 것은?(money, card, ...) : '))
if 'money' in pocket:
    print('택시 타고 가자')
elif 'card' in pocket:
    print('모범택시 타고 가자')
else:
    print('버스 타고 가자')

# ex 4-9
score = int(input('점수를 입력하세요 : '))
if score >= 90 :
    grade = 'A'
elif score >= 80 :
    grade = 'B'
elif score >= 70 :
    grade = 'C'
elif score >= 60 :
    grade = 'D'
else :
    grade = 'F'
print('{0}점은 "{1}" 학점입니다.'.format(score, grade))

# ex 4-10
score = int(input('점수를 입력하세요 : ')) 
if (score >= 95) and (score <= 100):
    grade = 'A+'
elif score >= 90 :
    grade = 'A'
elif score >= 85 :
    grade = 'B+'
elif score >= 80 :
    grade = 'B'
elif score >= 75 :
    grade = 'C+'
elif score >= 70 :
    grade = 'C'
elif score >= 65 :
    grade = 'D+'
elif score >= 60 :
    grade = 'D'
else :
    grade = 'F'
print('{0}점은 "{1}" 학점입니다.'.format(score, grade))

score = int(input('점수를 입력하세요 : ')) 
if score >= 95 :
    grade = 'A+'
elif score >= 90 :
    grade = 'A'
elif score >= 85 :
    grade = 'B+'
elif score >= 80 :
    grade = 'B'
elif score >= 75 :
    grade = 'C+'
elif score >= 70 :
    grade = 'C'
elif score >= 65 :
    grade = 'D+'
elif score >= 60 :
    grade = 'D'
else :
    grade = 'F'
if (score > 100 or score < 0):
    print('점수는 0점부터 100점 까지만 입력 가능합니다.')
else:
    print('{0}점은 "{1}" 학점입니다.'.format(score, grade))

score = int(input('점수를 입력하세요 : ')) 
if score >= 90 :
    grade = 'A'
elif score >= 80 :
    grade = 'B'
elif score >= 70 :
    grade = 'C'
elif score >= 60 :
    grade = 'D'
else :
    grade = 'F'
if score == 100:
    grade += '+'
elif score > 60 :
    if (score % 10 >= 5) :
        grade += '+'
print('{0}점은 "{1}" 학점입니다.'.format(score, grade))

score = int(input('점수를 입력하세요 : ')) 
if score >= 90 :
    grade = 'A'
elif score >= 80 :
    grade = 'B'
elif score >= 70 :
    grade = 'C'
elif score >= 60 :
    grade = 'D'
else :
    grade = 'F'
if score == 100:
    grade += '+'
elif score > 60 :
    if (score % 10 >= 5) :
        grade += '+'
if score > 100 or score < 0 :
    print('점수는 0에서 100까지만 입력해야 합니다')
else : 
    print('{0}점은 "{1}" 학점입니다.'.format(score, grade))

# ex 4-11
year = int(input('연도를 입력하세요 : '))
if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)) :
    print('%d년은 윤년입니다.' % year)
else : 
    print('%d년은 평년입니다.' % year)

# 작은 수를 a에 큰 수를 b에 저장하는 예제
print('작은 수를 a에 큰 수를 b에 저장하는 예제')
a = int(input('a에 수를 입력하세요 : '))
b = int(input('b에 수를 입력하세요 : '))

print(a)
print(b)

if a < b :
    print("a = {0} b = {1}".format(a, b))
else :
    print("a = {0} b = {1}".format(a, b))

# 작은 수를 a에 큰 수를 b에 저장하는 예제 다른 방법
print('작은 수를 a에 큰 수를 b에 저장하는 예제')
a = int(input('a에 수를 입력하세요 : '))
b = int(input('b에 수를 입력하세요 : '))
if(a<b):
    print("입력 a = %d, b = %d"%(a,b))
    print("출력 a = %d, b = %d"%(a,b))
else:
    print("입력 a = %d, b = %d"%(a,b))
    temp = a
    a = b
    b = temp
    print("출력 a = %d, b = %d"%(a,b))

# 반복문
# ex 4-12
for i in range(5):
    print('Hello, World!')

# ex 4-13
sum = 0
for n in range(1, 11):
    print(n)
    sum += n
print(sum)

# ex 4-14
sum_even = 0 # 짝수의 합
sum_odd = 0  # 홀수의 합
for n in range(1, 101): # 1부터 100까지의 반복
    if n % 2 == 0:      # n 이 짝수인 경우,
        sum_even += n
    else :              # n 이 홀수인 경우,
        sum_odd += n
print('짝수의 합 = ' , sum_even)
print('홀수의 합 = ' , sum_odd)

# ex 4-15
for i in range(10):
    print(i, end=' ')
print()

for i in range(1, 15):
    print(i, end=' ')
print()

for i in range(1, 15, 2):
    print(i, end=' ')
print()

for i in range(15, -1, -1):
    print(i, end=' ')
print()

# ex 4-16
L1 = list(range(10))
L2 = list(range(1, 15))
L3 = list(range(1, 15, 2))
L4 = list(range(15, -1, -1))
print(L1); print(L2); print(L3); print(L4)