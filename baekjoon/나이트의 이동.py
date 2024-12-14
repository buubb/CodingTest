import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def chess(self):
        T = int(input())
        for _ in range(T):
            I = int(input())
            check = [[False]*I for _ in range(I)]
            x, y = map(int, input().split())
            a, b = map(int, input().split())

            Q = deque()
            Q.append((x,y,0))
            check[x][y] = True
            while Q:
                i,j,cnt = Q.popleft()
                
                if i==a and j==b:
                    print(cnt)
                    break
                for dx, dy in ((2,-1),(2,1),(1,-2),(1,2),(-1,-2),(-1,2),(-2,-1),(-2,1)):
                    nx = i + dx
                    ny = j + dy
                    if 0<=nx<I and 0<=ny<I and not check[nx][ny]:
                        Q.append((nx, ny, cnt+1))
                        check[nx][ny] = True

if __name__ == "__main__":
     s = Solution()
     s.chess()
