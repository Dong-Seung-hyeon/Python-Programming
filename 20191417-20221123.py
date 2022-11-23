# ex 10-10
import urllib.request

address = urllib.request
check = address.urlopen("https://www.naver.com")
print(check.status)
print(address.urlopen("https://www.naver.com"))

icheck = address.urlopen("http://www.pythonchallenge.com/")
print(icheck.read())
print('---------------------------')
print(icheck.read().decode('utf-8'))

# ex 10-11
