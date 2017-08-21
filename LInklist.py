#!/usr/bin/python
# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self,val,p=0):
        self.data = val
        self.next = p

    def __repr__(self):

        '''
        用来定义Node的字符输出，
        print为输出data
        '''
        return str(self.data)

class LinkList(object):
    def __init__(self):
        self.head = 0

    def __getitem__(self, key):

        if self.is_empty():
            print 'linklist is empty.'
            return

        elif key < 0  or key > self.getlength():
            print 'the given key is error'
            return

        else:
            return self.getitem(key)



    def __setitem__(self, key, value):

        if self.is_empty():
            print 'linklist is empty.'
            return

        elif key < 0  or key > self.getlength():
            print 'the given key is error'
            return

        else:
            self.delete(key)
            return self.insert(key)

    def initlist(self,data):

        self.head = Node(data[0])

        p = self.head

        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next
        
        return str(self.head.data)

    def getlength(self):

        p = self.head
        length = 0
        
        #print p

        while p != 0:
            length += 1
            p = p.next

        return length

    def is_empty(self):

        if self.getlength() == 0:
            return True
        else:
            return False

    def clear(self):

        self.head = 0


    def append(self,item):

        q = Node(item)
        if self.head == 0:
            self.head = q
        else:
            p = self.head
            while p.next != 0:
                p = p.next
            p.next = q
        return p.next


    def getitem(self,index):

        if self.is_empty():
            print 'Linklist is empty.'
            return
        j = 0
        p = self.head

        while p.next != 0 and j < index:
            p = p.next
            j += 1

        if j == index:
            return p.data

        else:

            print 'target is not exist!'

    def insert(self,index,item):

        if self.is_empty() or index < 0 or index > self.getlength():
            print 'Linklist is empty.'
            return

        if index == 0:
            q = Node(item,self.head)

            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next != 0 and j < index:
            post = p
            p = p.next
            j += 1

        if index == j:
            q = Node(item,p)
            post.next = q
            q.next = p


    def delete(self,index):

        if self.is_empty() or index<0 or index >self.getlength():
            print 'Linklist is empty.'
            return

        if index == 0:
            q = Node(item,self.head)

            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next != 0 and j < index:
            post = p
            p = p.next
            j += 1

        if index == j:
            post.next = p.next

    def index(self,value):

        if self.is_empty():
            print 'Linklist is empty.'
            return

        p = self.head
        i = 0
        while p.next != 0 and not p.data == value:
            p = p.next
            i += 1

        if p.data == value:
            return i
        else:
            return -1


if __name__ == '__main__':
    lst = Node(1, Node(2))
    print lst.next

    lst2 = Node(1)
    lst3 = Node(2)

    print lst2.next
    print lst3.next


    #l = LinkList()
    #print l.head
    #l.head = p
    #print l.head
    #l.initlist([1,2,3,4,5])
    #print l
    #print l.head
    #print l.head.next
    #print l.getlength()
    #print l.head.next.data
    #print l.head.next.next
    #print l.index()
    #print l.getitem(4)
    #print l.append(6)
    #print l.getlength()
    #print l.getitem(5)

    #l.insert(4,40)
    #print l.getitem(3)
    #print l.getitem(4)
    #print l.getitem(5)

    #l.delete(5)
    #print l.getitem(5)

    #l.index(5)