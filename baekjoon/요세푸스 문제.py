import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def anwser(self):
        N, K = map(int, input().split())
        Q = deque()
        for i in range(1,N+1):
            Q.append(i)
        res = []
        
        while Q:
            for _ in range(K-1):
                Q.append(Q.popleft())
            res.append(Q.popleft())
        
        print("<"+', '.join(map(str,res))+">")

if __name__ == "__main__":
    s = Solution()
    s.anwser()
