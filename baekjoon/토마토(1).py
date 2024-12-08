import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def tomato(self):
        N, M = map(int, input().split())
        grid = [list(map(int, input().split())) for _ in range(M)]
        
        ripe_tomato = []
        unriped_tomato = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    unriped_tomato += 1
                elif grid[i][j] == 1:
                    ripe_tomato.append((i,j))
        
        visited = [[False for _ in range(N)] for _ in range(M)]
        
        Q = deque()
        for i,j in ripe_tomato:
            Q.append((i,j,0))
            visited[i][j] = True
        
        max_days = 0
        while Q:
            x, y, day = Q.popleft()
            max_days = max(day, max_days)
            for dx, dy in ((0,-1),(0,1),(-1,0),(1,0)):
                nx = x + dx
                ny = y + dy
                if 0<=nx<M and 0<=ny<N and not visited[nx][ny]:
                    if grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        unriped_tomato -= 1
                        visited[nx][ny] = True
                        Q.append((nx,ny,day+1))
           
        
        if unriped_tomato > 0:
            print(-1)
        elif unriped_tomato == 0:
            print(max_days)

                
            

if __name__ == "__main__":
    s = Solution()
    s.tomato()