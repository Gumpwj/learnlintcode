#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ListNode(object):  
    def __init__(self, val, P=None):  
        self.val=val  
        self.next=P  
'''
    def get_val(self):
        return self._val

    def get_next(self):
        return self._next
'''
    
  
      
def recurse(head,newhead):    #递归，head为原链表的头结点，newhead为反转后链表的头结点  
    if head is None:  
        return None
    if head.next is None:  
        newhead = head 
    else :  
        newhead = recurse(head.next,newhead)  
        head.next.next = head  
        head.next = None 
    return newhead 
      
hd = ListNode(1)               #测试代码  
p1 = ListNode(2)                 # 建立链表1->2->3->4->None  
p2 = ListNode(3)  
p3 = ListNode(4)  
hd.next = p1  
p1.next = p2  
p2.next = p3  
nehead = None  
p = recurse(hd,nehead)          #输出链表4->3->2->1->None  
while p:  
    print p.val 
    p = p.next  