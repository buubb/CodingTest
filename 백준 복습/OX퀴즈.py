import sys
input = sys.stdin.readline
from collections import deque

class Solution:
    def oxquiz(self):
        n = int(input())
        for _ in range(n):
            Q = deque(input().rstrip())
            i, res = 0,0
            while Q:
                x = Q.popleft()
                if x =='O':
                    i += 1
                    res += i
                else:
                    i = 0
            print(res)

if __name__ == "__main__":
    s = Solution()
    s.oxquiz()