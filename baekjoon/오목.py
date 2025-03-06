import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def game(self):
        N = int(input())
        grid = [[0]*20 for _ in range(20)]

        def bfs(x, y, d, stone):
            Q = deque()
            Q.append((x, y))
            visit = [[False] * 20 for _ in range(20)]
            visit[x][y] = True
            cnt = 1  # 시작점도 포함해야 하므로 1부터 시작
            while Q:
                i, j = Q.popleft()
                for dx, dy in d:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < 20 and 0 <= ny < 20 and grid[nx][ny] == stone and not visit[nx][ny]:
                        Q.append((nx, ny))
                        visit[nx][ny] = True
                        cnt += 1  # 연결된 돌 개수 증가
            return cnt

        
        def check_bfs(x,y,stone):
            d = [[(-1,0),(1,0)],[(0,-1),(0,1)],[(-1,1),(1,-1)],[(-1,-1),(1,1)]]
            for direction in d: 
                cnt = bfs(x,y,direction,stone)
                if cnt == 5:
                    return True
            return False
        
        res = float('inf')
        save = False
        for i in range(N):
            x, y = map(int, input().split())
            find = False
            if i % 2 == 0:
                grid[x][y] = 1
                find = check_bfs(x,y,1)
            else:
                grid[x][y] = 2
                find = check_bfs(x,y,2)
            
            if find:
                res = min(res, i+1)
                save = True
        
        if save:
            print(res)
        else:
            print(-1)



if __name__ == "__main__":
    s = Solution()
    s.game()