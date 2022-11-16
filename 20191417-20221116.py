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

# ex 9-4
file = open("test1.txt", "x")
file.write('대한민국 만세!!')
file.close()

file = open("test1.txt", "r")
read = file.read()
print(read)
file.close()
