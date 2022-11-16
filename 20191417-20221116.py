# ex 9-1
file = open("test.txt", "w")
file.write('Hello World!!\n파이썬 월드')

file = open("test.txt", "r")
read = file.read()
print(read)
file.close()
