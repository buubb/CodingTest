from sys import stdin
from collections import deque
class Solution:
    def findAndHide(self):
        subin, sister = map(int, stdin.readline().split())
        
        def dfs():
            max_limit = 100000
            visited = [False] * (max_limit+1)
            Q = deque()
            Q.append((subin,0))
            visited[subin] = True
            while Q:
                n, k = Q.popleft()
                if n == sister:
                    return k
                x,y,z = 2*n, n+1, n-1
                for i in (x,y,z):
                    if 0 <= i <=max_limit and not visited[i]:
                        Q.append((i, k+1))
                        visited[i] = True
            
        print(dfs())
                

if __name__ =="__main__":
    s = Solution()
    s.findAndHide()