# ex 4-1
a = int(input('1에서 100 사이의 정수를 입력하세요 : '))
if (a < 100) : 
    print('입력한 정수가 100보다 작음')
    print('a = %d' % a)

print('프로그램 종료')

# ex 4-2
a = int(input('1에서 100 사이의 정수를 입력하세요 : '))
if (a < 100) : 
    print('입력한 a의 값은 %d이며 100보다 작음' % a)
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

