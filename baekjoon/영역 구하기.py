import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def area(self):
        M, N, K = map(int, input().split())
        grid = [[0]*M for _ in range(N)]
        
        for _ in range(K):
            x,y,x2,y2 = map(int, input().split())
            for i in range(x, x2):
                for j in range(y, y2):
                    grid[i][j] += 1
        visited = [[False]*M for _ in range(N)]
        res = []
        def bfs(i,j):
            Q = deque()
            Q.append((i,j))
            visited[i][j] = True
            cnt = 1
            while Q:
                x,y = Q.popleft()

                for dx, dy in ((0,-1),(0,1),(1,0),(-1,0)):
                    nx = x + dx
                    ny = y + dy
                    if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and grid[nx][ny] == 0:
                        Q.append((nx,ny))
                        cnt += 1
                        visited[nx][ny] = True
            res.append(cnt)

        cnt = 0
        for i in range(N):
            for j in range(M):
                if not visited[i][j] and grid[i][j] == 0:
                    bfs(i,j)
                    cnt += 1
        
        print(cnt)
        print(*sorted(res))



if __name__ == "__main__":
    s = Solution()
    s.area()