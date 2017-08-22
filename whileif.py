#-*- coding: utf-8 -*-

def toInput():
    while True:                                # 无限循环 相当于 while(true)
         try:                                       # try
             s = input()  
             return s                          # 读取一行的输入
         except:                                    # 当遇到文件终结的时候会扔出 EOFError
             print "EOF"
             break                                  # 跳出循环
    return 

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
'''
if __name__ == '__main__':
    a = testWhile(4)
    print a

    b = testif(4)
    print b
'''