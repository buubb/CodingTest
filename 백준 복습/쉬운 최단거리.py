import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def short_dist(self):
        n,m = map(int, input().split())
        grid = []
        for _ in range(n):
            grid.append(list(map(int, input().split())))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    start = [i,j]
                    break

        def is_valid(i,j):
            return 0 <= i < n and 0 <= j < m
        visited = [[False]*m for _ in range(n)]
        def bfs(i,j):
            Q = deque()
            Q.append((i,j,0))
            grid[i][j]=0
            visited[i][j] = True
            while Q:
                x, y, k= Q.popleft()
                for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
                    nx, ny = x + dx, y + dy
                    if is_valid(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 1:
                        visited[nx][ny] = True
                        grid[nx][ny] = k+1
                        Q.append((nx,ny,k+1))
        
        bfs(start[0], start[1])
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == 1:
                    grid[i][j] = -1
        for r in grid:
            print(*r)



if __name__ == "__main__":
    s = Solution()
    s.short_dist()