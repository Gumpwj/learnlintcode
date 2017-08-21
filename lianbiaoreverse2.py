#!/usr/bin/python
# -*- coding: utf-8 -*-

class ListNode(Object):  
    def __init__(self, val, p = None):  
        self.val = val 
        self.next = p 
'''
    def __repr__(self):
        return repr(self.val)
'''

def nonrecurse(head):                       #循环的方法反转链表  
    if head is None or head.next is None:  
        return head 
    pre = None 
    cur = head
    h = head
    while cur:  
        h = cur 
        tmp = cur.next
        cur.next = pre  
        pre = cur 
        cur = tmp  
    return h;  
      
head = ListNode(1)                                    #测试代码  
p1 = ListNode(2)                                    #建立链表1->2->3->4->None;  
p2 = ListNode(3) 
p3 = ListNode(4)  
print p1.next
head.next = p1  
p1.next = p2  
p2.next = p3 
cur = head
h = head
print head, cur, h
p = nonrecurse(head)   #输出链表 4->3->2->1->None  
while p:  
    print p.val  
    p = p.next  