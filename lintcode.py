#-*- coding: utf-8 -*-

### lintcode ###

#不同路径    
def path_1(m, n):
    if m < 0 and n < 0:
        return None

    dp = [[0 for x in range(m)] for y in range(n)]

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = 1
            elif i > 0 and j == 0:
                dp[i][j] = dp[i-1][j]
            elif i == 0 and j > 0:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
    
    return dp[m-1][n-1]


#不同路经2
def path_2(obtacle):
    if len(obstacle) < 0 and len(obstacle[0]) < 0:
        return None

    m = len(obstacle)
    n = len(obstacle[0])
    dp = [[0 for x in range(m)] for y in range(n)]
    
    for i in range(m):
        for j in range(n):
            if obstacle[i][j] == 1:
                dp[i][j] = 0
                continue
            if i == 0 and j == 0:
                dp[i][j] = 1
            elif i > 0 and j == 0:
                dp[i][j] = dp[i-1][j]
            elif i == 0 and j > 0:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
    
    return dp[m-1][n-1]
    
#链表求和
class ListNode(object):  
    def __init__(self, val, P=None):  
        self.val=val  
        self.next=P  


class Listadd(object):
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2
    def addLists(self, l1, l2):
        # write your code here
        if l1 is None: return l2
        if l2 is None: return l1
         
        head1 = l1
        head2 = l2
        flag = 0
         
        while head1.next is not None or head2.next is not None:
            # 存在某一链表next为空时，构造next.val = 0，不影响加法结果
            if head1.next is None:
                head1.next = ListNode(0)
            if head2.next is None:
                head2.next = ListNode(0)
                 
            sumNum = head1.val + head2.val
            if sumNum >= 10:
                
                head1.val = sumNum%10
                flag = 1
                head1.next.val += 1
            else:
                head1.val = sumNum
                flag = 0
            head1 = head1.next
            head2 = head2.next
        else:
            # 链表末尾时，单独处理，其和大于10时，追加节点
            head1.val = head1.val + head2.val
            if head1.val >= 10:
                head1.val = head1.val%10
                head1.next = ListNode(1)
        return l1

#冒泡排序
def bubble(bubblelist):
    lengthlist = len(bubblelist)
    while lengthlist > 0:
        for i in range(lengthlist -1):
            temp = bubblelist[i]
            bubblelist[i] = bubblelist[i+1]
            bubblelist[i+1] = temp
        lengthlist -= 1
    
    return bubblelist

#等价二叉树
"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(this, val):
        this.val = val
        this.left, this.right = None, None

class Solution(object):
    """
    @param a, b, the root of binary trees.
    @return true if they are identical, or false.
    """
    #方法1
    def isIdentical1(self, a, b):
        # Write your code here
        if a == None and b == None:
            return True
        if (a == None and b != None) or (a != None and b == None):
            return False
        L = []
        L1 = self.pre_order(a, L) + self.mid_order(a, L) + self.last_order(a, L)
        L = []
        L2 = self.pre_order(b, L) + self.mid_order(b, L) + self.last_order(b, L)
        if L1 == L2:
            return True
        return False

    def pre_order(self, root, L):
        if root == None:
            return
        L.append(root.val)
        self.pre_order(root.left, L)
        self.pre_order(root.right, L)
        return L

    def mid_order(self, root, L):
        if root == None:
            return
        self.mid_order(root.left, L)
        L.append(root.val)
        self.mid_order(root.right, L)
        return L

    def last_order(self, root, L):
        if root == None:
            return
        self.mid_order(root.left, L)
        self.mid_order(root.right, L)
        L.append(root.val)
        return L
    #方法2
    def isIdentical2(self, a, b):
        if a == None and b == None:
            return True
        if (a == None and b != None) or (a != None and b == None):
            return False
        if a.val != b.val:
            return False
        return isIdentical2(a.left, b.left) and isIdentical2(a.right, b.right)
#克隆二叉树
def cloneTree(root):
    """构造二叉树pNewRoot, root"""
    if root != None:
        pNewRoot = TreeNode(root.val)
        if root.left != 0:
            pNewRoot.left = cloneTree(root.left)
        if root.right != 0:
            pNewRoot.right = cloneTree(root.right)
        return pNewRoot
    return None

                   
#实现x的平方根
def sqrt(x):
    return int(x**2)

#用 O(1) 时间检测整数 n 是否是 2 的幂次
def checkPowerOf2(n):
    return n > 0 and (n & (n-1)) == 0

#阶乘n！
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
        
#整数排列-快速排序
def sortInteger2(A):
    size = len(A)
    if size <= 1:
        return
    Quitsort = quitSort(A, 0, size-1)
    return Quitsort

def quitSort(A, left, right):
    if(left < right):
        i = left
        j = right
        x = A[i]
        while i < j:
            while i < j and A[j] >= x:
                j -= 1
            if  i < j:
                A[i] = A[j]
                i += 1
            while i < j and A[j] < x:
                i += 1
            if i < j:
                A[j] = A[i]
                j -= 1
        A[i] = x;
        quitSort(A, left, i-1)
        quitSort(A, i+1, right)
    return A      

#子数组之和为0, 返回数组索引
def subarraySum(nums):
    """ nums为list """
    size = len(nums)
    #sums = 0
    if size <= 0:
        return "wrong list"
    
    result = []
    last = []
    for i in range(size-1):
        sums = nums[i]
        if sums == 0:
            result.append(i)
            result.append(i)
            #return result
        for j in range(i+1, size-1):
            sums += nums[j]
            if sums == 0:
                result.append(i)
                result.append(j)
    return result
        
    
if __name__ == '__main__':
    s1 = path_1(3, 3)
    print s1
    
    obstacle = [[0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]]

    s2 = path_2(obstacle)
    print s2

    a = sqrt(2)
    print a

    b = fact(7)
    print b

    c = checkPowerOf2(5)
    print c

    d = sortInteger2([3, 2, 4])
    print d

    e = [-3, 1, 2, -3, 4]
    f = subarraySum(e)
    print f