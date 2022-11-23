# ex 10-10
import urllib.request

address = urllib.request
check = address.urlopen("https://www.naver.com")
print(check.status)
print(address.urlopen("https://www.naver.com"))

icheck = address.urlopen("http://www.pythonchallenge.com/")
# print(icheck.read())
# print('---------------------------')
print(icheck.read().decode('utf-8'))

import urllib.parse
parse = urllib.parse.urlparse('http://www.sungkyul.ac.kr')
print(parse)

# ex 10-15
import urllib.robotparser
rp = urllib.robotparser.RobotFileParser('http://www.sungkyul.ac.kr')
rp.read()
print(rp.can_fetch('mycrawler', 'http://www.sungkyul.ac.kr'))

# ex 10-16
import time
t = time.time()
print(t)
time_UTC = time.gmtime(t)
print(time_UTC)

time_local = time.localtime(t)
print(time_local)
print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))
print(time.strftime('%B', time.localtime(time.time())))
print(time.strftime('%Z', time.localtime(time.time())))

import datetime

print(datetime.datetime.today())
print(datetime.datetime(2022, 11, 23))
print(datetime.datetime.strptime('2020-11-23', '%Y-%m-%d'))
d = datetime.datetime(2022, 11, 23)
print()
print(d.strftime('%Y-%m-%d'))
print(d.strftime('%c'))

t = time.time()
time.sleep(10)

t2 = time.time()

spendtime = t2 - t
spendtime = int(spendtime)

print("Before timestemp: ", t)
print("After timestemp: ", t2)
print("Wait {} seconds".format(spendtime))

import numpy as np

ar = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(ar)
print(type(ar))
