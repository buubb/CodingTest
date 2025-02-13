import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def missing(self):
        S = list(input().rstrip().split('-'))
        res = deque()
        for s in S:
            k = 0
            tmp = s.split('+')
            for t in tmp:
                k += int(t)
            res.append(k)
        a = res.popleft()
        while res:
            a -= res.popleft()
        print(a)

if __name__ == "__main__":
    s = Solution()
    s.missing()