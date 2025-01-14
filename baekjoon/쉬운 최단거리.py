import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def easy_dist(self):
        n,m = map(int, input().split())
        grid = []
        for _ in range(n):
            grid.append(list(map(int, input().split())))
        visited = [[False]*m for _ in range(n)]
        def bfs(i,j):
            Q = deque()
            Q.append((i,j,0))
            visited[i][j] = True
            grid[i][j] = 0
            while Q:
                a,b,k = Q.popleft()
                for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
                    nx, ny = a + dx, b + dy
                    if nx >= 0 and ny >=0 and nx < n and ny < m and not visited[nx][ny] and grid[nx][ny] != 0:
                        Q.append((nx,ny,k+1))
                        grid[nx][ny] = k+1
                        visited[nx][ny] = True
            
        
        found = False
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    bfs(i,j)
                    found = True
                    break
            if found:
                break
        
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == 1:
                    grid[i][j] = -1

        for g in grid:
            print(*g)

if __name__ == "__main__":
    s = Solution()
    s.easy_dist()