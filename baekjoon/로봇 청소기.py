import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def robot_cleaner(self):
        n,m = map(int, input().split())
        r,c,d = map(int, input().split())
        grid = [list(map(int, input().split())) for _ in range(n)]
        def is_valid(x,y) -> bool:
            return 0 <= x < n and 0 <= y < m
        def bfs():
            Q = deque()
            Q.append((r,c,d))
            visited = [[False]*m for _ in range(n)]
            visited[r][c] = True
            cnt = 1
            while Q:
                x, y, k= Q.popleft() # dd 0:북 1:동 2:남 3:서
                d_arr = [(-1, 0), (0, 1), (1,0), (0,-1)]
                is_cleaned = False
                for _ in range(4):
                    nd = (k+3) % 4
                    nx, ny = x + d_arr[nd][0], y+ d_arr[nd][1]

                    if is_valid(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 0:
                        visited[nx][ny]= True
                        cnt += 1
                        Q.append((nx,ny,nd))
                        is_cleaned = True
                        break

                    k = nd
                
                if not is_cleaned:
                    back_d = (k+2)%4
                    bx, by =  x + d_arr[back_d][0], y + d_arr[back_d][1]

                    if is_valid(bx, by) and grid[bx][by] != 1:
                        Q.append((bx,by,k))
                    else:
                        break 
            return cnt
        print(bfs())

if __name__ == "__main__":
    s = Solution()
    s.robot_cleaner()