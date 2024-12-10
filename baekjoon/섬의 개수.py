import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def island(self):     
        while True:
            w,h = map(int, input().split())
            if w==0 and h==0:
                return
            graph = []
            for _ in range(h):
                a = list(map(int, input().split()))
                graph.append(a)

            cnt = 0
            check = [[False for _ in range(w)] for _ in range(h)]
            for i in range(h):
                for j in range(w):
                    if graph[i][j]== 1 and not check[i][j] :
                        Q = deque()
                        Q.append((i,j))
                        check[i][j] = True
                        while Q:
                            x,y = Q.popleft()
                            
                            for dx, dy in ((0,-1),(0,1),(-1,0),(1,0),(-1,-1),(1,1),(-1,1),(1,-1)):
                                nx = x+dx
                                ny = y+dy
                                
                                if 0<=nx<h and 0<=ny<w and not check[nx][ny] and graph[nx][ny] == 1:
                                    check[nx][ny]=True
                                    Q.append((nx,ny))
                        cnt += 1
            
            print(cnt)
            
if __name__ == "__main__":
    s = Solution()
    s.island()