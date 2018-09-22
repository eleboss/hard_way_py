#! /usr/bin/python
#coding=utf-8

# 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

list = [1,2,3]

print list[-1:0]



ListNode_1 = ListNode()
print ListNode_1


# 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        newlist = []
        while listNode:
            newlist.insert(0,listNode.val)
            listNode  = listNode.next
        return newlist