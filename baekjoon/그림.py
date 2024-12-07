import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def drawing(self):
        N,M = map(int, input().split())
        arr = [list(map(int, input().split())) for _ in range(N)]
        visited = [[False for _ in range(M)] for _ in range(N)]

        def bfs(i,j):
            Q = deque()
            Q.append((i,j))
            
            visited[i][j] = True
            count = 1
            while Q:
                x, y = Q.popleft()
                visited[x][y] = True
                
                for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                        if arr[nx][ny] == 1:
                            Q.append((nx, ny))
                            visited[nx][ny] = True
                            count += 1
            return count
        cnt = 0
        width = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 1 and not visited[i][j]:
                    width = max(width, bfs(i,j))
                    cnt += 1
        print(cnt)
        print(width)

if __name__ == "__main__":
    s = Solution()
    s.drawing()