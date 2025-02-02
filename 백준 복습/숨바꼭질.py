import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def hide_find(self):
        n,k = map(int, input().split())
        def bfs():
            Q = deque()
            Q.append((n,0))
            visited = [False] * 100_001
            visited[n] = True
            while Q:
                x, cnt = Q.popleft()
                if x == k:
                    print(cnt)
                    return
                a, b, c = x-1, x+1, 2*x
                for dx in (a,b,c):
                    if 0 <= dx <= 100_000 and not visited[dx]:
                        Q.append((dx, cnt+1))
                        visited[dx] = True
        bfs()

if __name__ == "__main__":
    s = Solution()
    s.hide_find()