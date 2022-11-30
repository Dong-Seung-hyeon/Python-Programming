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

