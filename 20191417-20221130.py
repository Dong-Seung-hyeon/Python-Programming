# ex 10-37
from curses import ACS_S3
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
print(b3

)