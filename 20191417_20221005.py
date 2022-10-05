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

# ex 4-6
money = int(input('지갑에 얼마 있습니까?  '))
if money >= 3000:
    print('과자를 사먹자~~')
elif money >= 1000:
    print('껌을 사먹어야지^^')
else : 
    print('공기나 마시자 ㅠ.ㅠ')

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
    print('택시 타고 가자~~')
elif 'card' in pocket:
    print('모범택시 타고 가자^^')
else:
    print('걸어가야겠다 :)')

