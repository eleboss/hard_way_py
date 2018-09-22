#! /usr/bin/python
#coding=utf-8
import time 
print time.clock()
print 'Hellow, eleboss!'
print '中文支持'
print '1';print '2'
if True:
    print "True"
else:
    print "False"
alpha = 1 + \
9
print alpha

'''
zhushi'''


# raw_input('press enter to exit .../')


import sys; x = 'runoob'; sys.stdout.write(x+'\n')

a = 1.0
b=  100
c = '123'
print c[-2:-1]



dict = {}
dict['one'] = "this"
dict[2] = "tow"
print dict
print dict.values()

a = [1,2]
b = a
def do_nothong(a):
    pass
do_nothong(1)
print b, b is a 
# print reversed(-1)


rows = 4
for i in range(0, rows):
    for k in range(0, rows - i):
        print " * ", #注意这里的","，一定不能省略，可以起到不换行的作用


    print "\n"

i = 2
while(i < 100):
    j = 2
    # 寻找可以等分的结果
    while(j<=(i/j)):
        #找到可以等分的结果就跳出
        if not(i%j):break
        j=j+1
    #判断能不能被等分，不能就是质数
    if (j>i/j):print i
    i = i + 1
print 'over'

import time 

print time.localtime(time.time())
print time.asctime(time.localtime(time.time()))
print time.clock()
print time.time()