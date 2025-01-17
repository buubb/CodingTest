import sys
input = sys.stdin.readline
from collections import deque
class Solution:
    def beer_walk(self):
        t = int(input())
        for _ in range(t):
            # 맥주를 파는 편의점의 개수
            n = int(input())
            # 상근이네 집
            sx, sy = map(int, input().split())
            # 편의점 좌표
            mart = []
            for _ in range(n):
                mart.append(tuple(map(int, input().split())))
            # 락 페스티벌 좌표
            rx, ry = map(int, input().split())

            def bfs():
                Q = deque()
                Q.append((sx,sy))
                visited = set()
                visited.add((sx,sy))
                
                while Q:
                    x,y = Q.popleft()
                    if abs(x-rx) + abs(y-ry) <= 1000:
                        print("happy")
                        return
                    for nx,ny in mart:
                        if (nx,ny) not in visited:
                            if abs(x-nx) + abs(y-ny) <= 1000:
                                Q.append((nx,ny))
                                visited.add((nx,ny))
                print("sad")
       
            bfs()


if __name__ == "__main__":
    s = Solution()
    s.beer_walk()
                    