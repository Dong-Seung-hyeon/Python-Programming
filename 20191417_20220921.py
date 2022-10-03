str1 = ' Computer Engineering '
print(str1.replace('Engineering', 'Science'))
print(str1.strip())
print(str1)
print(str1.lstrip())
print(str1)
print(str1.rstrip())

str2 = "www.sungkyul.ac.kr"
print(str2)
print(str2.split('.'))
print()

poem = ''' 우리들은 모두
무엇이 되고 싶다.
너는 나에게 나는 너에게
잊혀지지 않는 하나의 눈짓이 되고 싶다'''
print(poem.splitlines())
print()

str3 = 'Computer Security'
str3 = '컴퓨터 공학과'
print("*".join(str3))

print(('Python').isalpha())
print(str3.isalpha())
str4 = '12345'
print(str4.isnumeric())
print(str3.isnumeric())
print(str3.isalnum())
print()

str5 = 'Department of {}'
print(str5.format('Computer Engineering'))
print(str5.format('Business Administration'))
str6 = '{}{}학과'
print(str6.format('컴퓨터', '공'))
print(str6.format('연극', '영화'))
print()

str7 = 'hello, {0} {1}'
print(str7.format('Computer', 'Engineering'))
str8 = 'hello, {1} {0}'
print(str8.format('Computer', 'Engineering'))
str9 = 'hello, {str20}{str21}'
print(str9.format(str20 = '컴퓨터', str21 = '공학과'))
print()

str10 = 'Department of {:20}'
print(str10.format('Engineering')+'/')
str10 = 'Department of {:<20}' #왼쪽 정렬
print(str10.format('Engineering')+'/')
str10 = 'Department of {:>20}' #오른쪽 정렬
print(str10.format('Engineering')+'/')
str10 = 'Department of {:^20}' #가운데 정렬
print(str10.format('Engineering')+'/')
print()

str10 = 'Department of {:*<20}' # *추가 왼쪽 정렬
print(str10.format('Engineering')+'/')
str10 = 'Department of {:*>20}' # *추가 오른쪽 정렬
print(str10.format('Engineering')+'/')
str10 = 'Department of {:*^20}' # *추가 가운데 정렬
print(str10.format('Engineering')+'/')
print()

str11 = '원주율 값은 {:.7f}'
print(str11.format(3.1415926535897))
str11 = '원주율 값은 {:10.4f}'
print(str11.format(3.1415926535897))
print()

str12 = 'Computer Engineering'
L2 = [202, 2021, 2022]
print(len(str12))
print(len(L2)) #리스트 요소 개수출력

str13 = '파이썬은 정말 재미있어요.'
print(len(str13))

print(ord('a'))
print(chr(97))

print(ord('ㄱ'))
print(chr(12593))
print()
print(hex(9))
print(hex(10))
print(hex(11))
print(hex(12))
print(hex(13))
print(hex(14))
print(hex(15))
print(hex(16))
print(hex(32))
print(oct(8))
print(oct(9))
print(oct(10))
print(oct(16))
print()
print(int(3.14159))
print(int(7/3))
print(int('3000'))
#print(int('hi'))

print(float(2))
print(float(6/3))
print(float('3000'))
print(float('3.14159'))
#print(float('hi'))
print()
data = input("정수를 입력하시오 : ")
print(type(data))
print(data)
print(data + '1')
print()
data = int(input("정수를 입력하시오 : "))
print(type(data))
print(data)
print(data + 1)
print()
age = input("나이를 입력하시오 : ")
print(type(age))
print(data)
message = age + '번째 생일을 축하합니다.'
print(message)
print()