# ex 6-1
def print_10times_star():
    print('*' * 10 )

print_10times_star()

# ex 6-2
def plus(v1, v2):
    result = 0
    result = v1 + v2
    return result

hap = plus(100, 200)
print(hap)

# ex 6-3
def plus(v1, v2):
    """이 함수는 v1과 v2를 더한 뒤 결과를 반환하는 함수입니다."""
    result = 0
    result = v1 + v2
    return result

hap = plus(100, 200)
print(hap)
print(plus.__doc__)