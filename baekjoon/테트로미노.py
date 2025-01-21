import sys, heapq
input = sys.stdin.readline

class Solution:
    max_num: int=0
    def tetromino(self):
        n,m = map(int, input().split())
        grid = []
        for _ in range(n):
            grid.append(list(map(int, input().split())))
        
        def is_valid(x,y) -> bool:
            return 0 <= x < n and 0 <= y < m
        
        dx = [0,0,-1,1]
        dy = [1,-1,0,0]

        visited = [[False]*m for _ in range(n)]
        def dfs(x,y,cnt,sum):
            if not is_valid(x,y):
                return
            if cnt == 4:
                self.max_num = max(self.max_num, sum)
                return

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if is_valid(nx,ny) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    dfs(nx, ny, cnt+1, sum + grid[nx][ny])
                    visited[nx][ny] = False
            
        def plus(x,y):
            arr = []
            for i in range(4):
                nx, ny = dx[i] + x, dy[i] + y
                if is_valid(nx,ny):
                    arr.append(grid[nx][ny])
            
            arr_len = len(arr)
            if arr_len == 3:
                self.max_num = max(self.max_num, grid[x][y] + sum(arr))

            if arr_len == 4:
                arr.remove(min(arr))
                self.max_num = max(self.max_num, grid[x][y] + sum(arr))

        for i in range(n):
            for j in range(m):
                visited[i][j] = True
                dfs(i,j,1,grid[i][j])
                plus(i,j)
                visited[i][j] = False

                
        
        print(self.max_num)
            
if __name__ == "__main__":
    s = Solution()
    s.tetromino()
            

            

            

