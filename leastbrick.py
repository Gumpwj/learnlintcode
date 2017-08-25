class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        """
        _M_rows = 0
        _M_cols = 0
        _M_rows = int(raw_input())
        _M_cols = int(raw_input())

        _M = []
        """
        _M = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
        """
        for _M_i in xrange(_M_rows):
            _M_temp = map(int,raw_input().strip().split(' '))
            _M.append(_M_temp)
        """

        N = len(_M)
        f = range(N)

        def find(x):
            while f[x] != x: x = f[x]
            return x

        for x in range(N):
            for y in range(x + 1, N):
                if M[x][y]: f[find(x)] = find(y)
        return sum(f[x] == x for x in range(N))

_M = int(raw_input())
ret = Solution()
print str(ret.findCircleNum(_M)) + "\n"