# ex 9-1
file = open("test.txt", "w")
file.write('Hello World!!\n파이썬 월드')
file.write('\n컴퓨터공학과')
file = open("test.txt", "r")
read = file.read()
print(read)
file.close()

file = open("test.txt", "w")
file.write('동승현')
file = open("test.txt", "r")
read = file.read()
print(read)

# ex 9-6
with open('test1.txt', 'x') as file:
    file.write('대한민국 만세!!!')

with open("test1.txt", 'r') as file:
    read = file.read()
    print(read)

# ex 9
import csv
listing = [['소나타', '현대', 22965],
['아이오닉', '현대', 23735],
['프리우스', '도요타', 24615],
['아맅마', '닛산', 23185],
['말리부', 'GM', 24645],
['티볼리', '쌍용', 24765]]

with open("car.csv", "w", newline='') as f:
    car_writer = csv.writer(f)
    car_writer.writerows(listing)

with open("car.csv", "r") as f:
    car_reader = csv.reader(f)
    for row in car_reader:
        names = row[0]
        makers = row[1]
        price = row[2]

        print(names, makers, price)

# ex 9-7
def divide(x, y):

    try:
        result = x/ y

    except ZeroDivisionError as zero_div_err:
        print("0으로 나눌 수 없습니다.", zero_div_err)

    else:
        print("정상적으로 나눗셈이 실행되었습니다. 결과는 =", result)

    finally:
        print("\n프로그램을 종료합니다.")

input_a = int(input('피제수를 입력해 주세요: '))
input_b = int(input('제수를 입력해 주세요: '))
print()
divide(input_a, input_b)

# ex 9-8
try:
    input_x = int(input('짝수를 입력하세요: '))
    if input_x % 2 != 0:
        raise Exception('짝수가 아닙니다.')

    if input_x == 0:
        raise Exception('0을 입력했군요')

except Exception as e:
    print('예외가 발생했습니다.', e)

else:
    print('잘했습니다. 입력한 수는 짝수입니다.')

finally:
    print("\n프로그램을 종료합니다.")

# ex 10-1
# 값의 절대값을 반환한다
print("abs(-3) = ", abs(-3))

#가장 큰 값을 반환한다.
print("max(2, 3, 5) = ", max(2, 3, 5))

#가장 작은 값을 반환한다.
print("min(2, 3, 5) = ", min(2, 3, 5))

#a^b를 반환한다(=a**b)
print("pow(2, 3) = ", pow(2, 3))

#소수점을 가까운 정수까지 반올림, 버림하여 반환한다.
print("round(2.5) = ", round(2.5))
print("round(2.7) = ", round(2.7))

#소수점을 가까운 정수까지 반올림, 버림하여 반환한다.
print("round(3.5) = ", round(3.5))
print("round(0.5) = ", round(0.5))

# ex 10-3
import math

print("math.fab(-2) = ", math.fabs(-2))
print("math.ceil(2.1) = ", math.celi(2.1))
print("math.celi(-2.1) = ", math.celi(-2.1))
print("math.floor(2.1) = ", math.floor(2.1))
print("math.floor(-2.1) = ", math.floor(-2.1))