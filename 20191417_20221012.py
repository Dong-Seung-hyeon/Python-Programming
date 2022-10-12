# ex 4-18
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
x = int(input('숫자를 입력하세요 : '))
for i in range(x, 0, -1):
    print('⭐️ ' * i)