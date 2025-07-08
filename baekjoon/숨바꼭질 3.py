import sys
from collections import deque

input = sys.stdin.readline

class Solution:
    def answer(self):
        N, K = map(int, input().split())

        def is_valid(k):
            return 0 <= k < 100_001
        
        def bfs():
            Q = deque()
            Q.append((N, 0))
            visited = [False] * 100_001
            visited[N] = True
            
            while Q:
                a, t = Q.popleft()

                if a == K:
                    break

                if is_valid(2*a) and not visited[2*a]:
                    Q.append((2*a, t))
                    visited[2*a] = True
                if is_valid(a-1) and not visited[a-1]:
                    Q.append(((a-1), t+1))
                    visited[a-1] = True
                if is_valid(a+1) and not visited[a+1]:
                    Q.append(((a+1), t+1))
                    visited[a+1] = True
                
            return t

        print(bfs())

if __name__ == "__main__":
    s = Solution()
    s.answer()