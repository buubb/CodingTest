import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
class Solution:
    def vegetable(self):
        T = int(input())
        for _ in range(T):
            M, N, K = map(int, input().split()) # 가로, 세로, 배추위치
            grid = [[0]*N for _ in range(M)]
            for _ in range(K):
                i,j = map(int, input().split())
                grid[i][j] = 1
            visited = [[False]*N for _ in range(M)]
            def is_valid(x,y):
                return 0<=x<M and 0<=y<N
            def dfs(i,j):
                if visited[i][j] and grid[i][j] == 0:
                    return
                
                visited[i][j] = True

                for (dx, dy) in ((-1, 0),(1,0),(0,-1),(0,1)):
                    nx, ny = i + dx, j + dy
                    if is_valid(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 1:
                        dfs(nx,ny)
                        
            cnt = 0
            for x in range(M):
                for y in range(N):
                    if not visited[x][y] and grid[x][y] == 1:
                        dfs(x,y)
                        cnt += 1
            print(cnt)

if __name__ == "__main__":
    s = Solution()
    s.vegetable()