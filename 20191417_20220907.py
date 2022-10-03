x = 3000
print(x)
import keyword
print(keyword.kwlist)
import builtins
print(dir(builtins))

# 삼각형의 면적 구하기 
base = 3
height = 4
area = base * height / 2
print('삼각형의 면적 =', area)

no = None
print(no)
print(type(no))

b1 = True
b2 = False
# b3 = true
print(b1, type(b1))
print(b2, type(b2))

a = 123
a = -178
a = 0
print(a, type(a))

Oct_a = 0o177
Oct_b = 0o251
hex_a = 0x8ff
hex_b = 0X10

print('8진수 : 0o177 는 십진수', int(Oct_a))
print('8진수 : 0o251 는 십진수', int(Oct_b))
print('16진수 : 0x8ff 는 십진수', int(hex_a))
print('16진수 : 0X10 는 십진수', int(hex_b))

f1 = 1.2
print(type(f1), f1)
f2 = -3.45
print(f2, type(f2))

f3 = 4.24E10
f4 = 4.24e-2
print('f3 = ', f3)
print('f4 = ', f4)

e = 2-3j
print(e.real)
print(e.imag)
print(e, type(e))