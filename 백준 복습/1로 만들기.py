import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def make_one(self):
        x = int(input())
        def bfs(x):
            Q = deque()
            Q.append((x, 0))
            while Q:
                n, cnt= Q.popleft()
                if n == 1:
                    print(cnt)
                    return
                if n % 3 == 0:
                    Q.append((n // 3, cnt+1))
                if n % 2 == 0:
                    Q.append((n//2, cnt+1))
                Q.append((n-1, cnt+1))
        
        bfs(x)

if __name__ == "__main__":
    s = Solution()
    s.make_one()