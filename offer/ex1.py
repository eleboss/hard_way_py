#! /usr/bin/python
import numpy as np
import array
anarray = np.array([[1,2,3,4],[1,1,2,3]])
# print anarray
# print anarray[:]

for i in anarray[:]:
    for j in i:
        print 'i',i
        print 'j',j

# 题目描述
# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。



# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        for i in array:
            for j in i:
                if j == target:
                    return True
        return False