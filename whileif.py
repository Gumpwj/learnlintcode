#-*- coding: utf-8 -*-

def testWhile(n):
    
    while n > 0 and n < 5:
        print "do done"
        n -= 1
        return n
        """
        return True 在while里面会直接终止循环
        """
    #return n

def testif(n):
    if n > 0 and n < 5:
        print "do done"
        n -= 1
        return n
        """
        return n 在while里面会直接终止循环
        """
    #return n

if __name__ == '__main__':
    a = testWhile(4)
    print a

    b = testif(4)
    print b

