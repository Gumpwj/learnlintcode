#!/usr/bin/python
# -*- coding: utf-8 -*-

def BinaryTree(r):
    return [r, [], []]
 
def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root
 
def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root
 
def getRootVal(root):
    return root[0]
 
def setRootVal(root,newVal):
    root[0] = newVal
 
def getLeftChild(root):
    return root[1]
 
def getRightChild(root):
    return root[2]
 
r = BinaryTree(3)
print r
print id(r)
l1 = insertLeft(r,4)
print(l1)
print id(l1)
l2 = insertLeft(r,5)
print(l1)
l3 = insertRight(r,6)
print(l3)
l4 = insertRight(r,7)
print(l4)
l = getLeftChild(r)
print(l) 
print id(l1) == id(l2) == id(l3) == id(l4)

setRootVal(l,9)
#print(r)
insertLeft(l,11)
#print(r)
#print(getRightChild(getRightChild(r)))