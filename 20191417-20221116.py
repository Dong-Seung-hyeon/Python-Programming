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