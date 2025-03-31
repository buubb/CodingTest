import sys
input = sys.stdin.readline
from collections import deque
class Solution:
    def answer(self):
        n = int(input())
        grid = [list(input().strip()) for _ in range(n)]
        def is_valid(x,y):
            return 0<=x<n and 0<=y<n
        # R과 G는 적록색약은 구분 못함
        
        def dfs(x, y, visited, origin):
            if not is_valid(x,y):
                return
            
            for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
                nx ,ny = x + dx, y+dy
                if origin and is_valid(nx, ny) and not visited[nx][ny] and grid[x][y] == grid[nx][ny]:
                    visited[nx][ny] = True
                    dfs(nx, ny, visited, origin)
                elif not origin and is_valid(nx, ny) and not visited[nx][ny]:
                    if (grid[x][y] == 'R' and grid[nx][ny] == 'G')\
                        or (grid[x][y] == 'G' and grid[nx][ny] == 'R')\
                            or grid[x][y] == grid[nx][ny]:
                        visited[nx][ny] = True
                        dfs(nx, ny, visited, origin)

                
        
        visited = [[False]*n for _ in range(n)]
        cnt, cnt2 = 0, 0
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    dfs(i,j,visited,True)
                    cnt += 1
        visited2 = [[False]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if not visited2[i][j]:
                    dfs(i,j,visited2,False)
                    cnt2 += 1
        print(cnt, cnt2)

                

if __name__ == "__main__":
    s = Solution()
    s.answer()