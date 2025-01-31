import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
class Solution:
    def apt(self):
        N = int(input())
        grid = []
        for _ in range(N):
            grid.append(list(map(int, input().strip())))

        def is_valid(x,y):
            return 0<=x<N and 0<=y<N
        
        visited = [[False]*N for _ in range(N)]
        cnt = 0
        def dfs(x,y):
            nonlocal cnt
            if not is_valid(x,y) or visited[x][y] or grid[x][y] == 0:
                return
            cnt += 1
            visited[x][y] = True
            dfs(x-1,y)
            dfs(x,y-1)
            dfs(x,y+1)
            dfs(x+1,y)
        res = []
        apt = 0
        for i in range(N):
            for j in range(N):
                if not visited[i][j] and grid[i][j] == 1:
                    dfs(i,j)
                    res.append(cnt)
                    cnt = 0
                    apt += 1
        res.sort()
        print(apt)
        print('\n'.join(map(str,res)))
    
    def apt_bfs(self):
        N = int(input())
        grid = [list(map(int, input().rstrip())) for _ in range(N)]

        def is_valid(x,y):
            return 0<=x<N and 0<=y<N
        visits = set()
        def bfs(x,y):
            Q = deque()
            Q.append((x,y))
            visits.add((x,y))
            cnt = 0
            while Q:
                i,j = Q.popleft()
                cnt += 1
                for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
                    nx,ny = i+dx, j+dy
                    if is_valid(nx,ny) and (nx,ny) not in visits and grid[nx][ny] == 1:
                        Q.append((nx,ny))
                        visits.add((nx,ny))
            return cnt
        res = []
        count = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1 and (i,j) not in visits:
                    res.append(bfs(i,j))
                    count += 1
        res.sort()
        print(count)
        print('\n'.join(map(str, res)))        
if __name__ == "__main__":

    s = Solution()
    s.apt_bfs()