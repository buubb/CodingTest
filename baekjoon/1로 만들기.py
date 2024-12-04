import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
class Solution:
    def makeOne(self):
        X = int(input())

        def bfs():
            Q = deque()
            k = 0
            Q.append((X,0))
            while Q:
                x, k = Q.popleft()
                if x == 1:
                    break
                if x % 3 == 0 and x//3 >= 1:
                    Q.append((x//3, k+1))
                if x % 2 == 0 and x//2 >= 1:
                    Q.append((x//2, k+1))
                if x-1 >= 1:
                    Q.append((x-1, k+1))
            return k
        
        print(bfs())

if __name__ == "__main__":
    s = Solution()
    s.makeOne()