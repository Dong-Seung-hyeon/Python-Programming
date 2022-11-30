# ex 10-37
import numpy as np

a = np.array([0, 1, 2, 3, 4, ])
print(a[2])
print(a[-1])

# ex 10-38
a1 = np. array(([0, 1, 2], [3, 4, 5]))
print(a1)
print(a1[0, 0]) # 첫번째 행의 첫번째 열
print(a1[0, 1]) # 첫번째 행의 두번째 열
print(a1[-1, -1]) # 마지막 행의 마지막 열

# ex 10-39
b = np.array(([0, 1, 2, 3], [4, 5, 6, 7]))
print(b)
print(b[0, :]) # 첫번째 행 전체
print(b[:, 1]) # 두번째 열 전체
print(b[1, 1:]) # 두번째 행의 두번째 열부터 끝열까지
print(b[:2, :2]) # 모든 행의 두번째 열까지

# ex 10-40
c = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
idx = np.array([True, False, True, False, True, 
                False, True, False, True, False])
print(c[idx])

# ex 10-41
d = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(d % 2)
print( d % 2 == 0 )
print(d[d % 2 == 0])

# ex 10-42
a11 = np.array([11, 22, 33, 44, 55, 66, 77, 88, 99])
idx = np.array([0, 2, 4, 6, 8])
print(a11[idx])

# ex 10-43
a2 = np.array([11, 22, 33, 44, 55, 66, 77, 88, 99])
idx = np.array([0,0,0,0,0,0, 1, 1, 1, 1, 1, 2, 2, 2, 2, ])
print(all[idx])

# ex 10-44
a3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a3)
print(a3[:, [True, False, False, True]])
print(a3[[2, 0, 1], :])

# ex 10-45
a4 = np.zeros(5)
print(64)

b3 = np.zerros((2, 3))
print(b3)

# ex 10-46
c1 = np.ones((5, 2), dtype="i")
print(c1)
print(c1.dtpe)

# ex 10-47
d = np.zeros(5, dtype="U4")
print(d)
d[0] = "abc"
d[1] = "abcd"
d[2] = "ABCDE"
print(d)

# ex 10-51
b = np.zeros((2, 3))
f = np.ones_lie(b, dtype="f")
print(b)
print(f)

# ex 10-
g = np.empty((2, 3))
print(g)

g = np.full((2, 3), 10)
print(g)

print(np.arange(10))            # 0 .. n-1
print(np.arange(2, 19, 2))      # 시작, 끝(포함하지 않음), 증감값
print(np.arange(19, 2, -2))

a5 = np.linspace(10, 20, 5, endpoint = False)   # 시작, 끝(포함), 개수
b2 = np.linspace(1, 2, 5, retstep = True)       #retstep을 이용하여 증감값
print(a5)
print(b2)

a6 = np.logspace(1, 10, 10, base=2)     # 시작, 끝(포함), 개수, 2를 base로 
print(a6)

print(np.eye(3))
print()
print(np.eye(3, k=1))
print()
print(np.eye(3, k=-1))

print(np.arange(20))
print(np.arange(20).reshape(4,5))

from urllib import request
from bs4 import BeautifulSoup
target=request.urlopen("https://www.sungkyul.ac.kr/skukr/342/subview.do")
soup=BeautifulSoup(target, 'html.parser')
title=soup.findAll('td', {'class':'td-subject'})
for i in range(10):
    print(title[i].text)

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 11)
y = x * 10

plt.plot(x,y)

plt.show()

import matplotlib.pyplot as plt
import numpy as np

x_values = [0, 1, 2, 3, 4]
y_values = [0, 1, 4, 9, 16]
plt.plot(x_values, y_values, 'k^-')
plt.rc("font", family = "Gothic")
plt.title("예제 10-61")
plt.xlabel('x line')
plt.ylabel('y line')

plt.show()

x = np.arange(1,5,0.5)

y = x * 10
y2 = 50 - (x * 10)

plt.plot(x, y, 'r', label='red')

plt.plot(x, y2, 'k', label='black')

plt.legend(loc=1)

plt.show()