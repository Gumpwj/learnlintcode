#!/usr/bin/env python
#-*- coding : utf-8 -*-

def deco(func):
    def inner():
        print "running inner()"
    return inner

@deco
def target():
    return "I"    

'''
def main():
    target()
    print id(target())

    pass

if __name__ == '__main__':
    main()
'''

target()
deco(target())