#! /usr/bin/python
# -*- coding:utf-8 -*-

# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。


string = 'we are happy!'
string2 = 'We%20Are%20Happy'
print string,string2
newstring = ''
for i in string:
    print i
    if i == ' ':
        i = '%20'
    newstring = newstring + i
print newstring