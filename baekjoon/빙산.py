import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

class Solution:
    def ice(self):
        N, M = map(int, input().split())
        arr = [list(map(int, input().split())) for _ in range(N)]

        def bfs(i, j, arr, visited):
            Q = deque()
            Q.append((i, j))
            while Q:
                x, y = Q.popleft()

                if visited[x][y]:
                    continue
                visited[x][y] = True

                dx = (0, 1, 0, -1)
                dy = (1, 0, -1, 0)

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                        if arr[nx][ny] == 0:
                            copy[x][y] = max(0, copy[x][y] - 1)  # 빙산이 녹는 부분
                        elif arr[nx][ny] > 0:
                            Q.append((nx, ny))

        def dfs(i, j):
            if i < 0 or j < 0 or i >= N or j >= M or vis[i][j] or arr[i][j] == 0:
                return
            vis[i][j] = True
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        res = 0
        while True:
            count = 0
            
            vis = [[False] * M for _ in range(N)]
            for i in range(N):
                for j in range(M):
                    if not vis[i][j] and arr[i][j] > 0:
                        dfs(i, j)
                        count += 1

            if count >= 2:  # 빙산이 두 덩어리 이상
                print(res)
                return
            if count == 0:  # 빙산이 모두 녹아 없어진 경우
                print(0)
                return

            # 빙산 녹이기
            copy = [row[:] for row in arr]  # 깊은 복사
            visited = [[False] * M for _ in range(N)]
            for i in range(N):
                for j in range(M):
                    if not visited[i][j] and arr[i][j] > 0:
                        bfs(i, j, arr, visited)
            arr = copy  # 녹인 결과를 arr로 업데이트
            
            res += 1

if __name__ == "__main__":
    s = Solution()
    s.ice()
