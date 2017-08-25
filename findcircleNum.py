import collections

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        rims = collections.Counter()
        print rims[0]
        for bricks in wall:
            cnt = 0
            for b in bricks:
                if cnt: rims[cnt] += 1
                cnt += b
        return len(wall) - max(rims.values() or [0])

_wall = [[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]

ret = Solution()
print ret.leastBricks(_wall)