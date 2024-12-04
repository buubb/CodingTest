import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
class Solution:
    def safe_zone(self):
        N = int(input())
        grid = []
        max_int = 0
        min_int = sys.maxsize
        for _ in range(N):
            arr = list(map(int, input().split()))
            grid.append(arr)
            max_int = max(max_int, max(arr))
            min_int = min(min_int, min(arr))
        
        def dfs(i, j, k):
            if i < 0 or j < 0 \
                or i >= N or j >= N or visited[i][j] or grid[i][j] < k:
                return
            
            visited[i][j] = True
            
            dfs(i+1, j, k)
            dfs(i-1, j, k)
            dfs(i, j-1, k)
            dfs(i, j+1, k)

        max_count = 0
        k = max_int
        while min_int <= k:
            count = 0
            visited = [[False for _ in range(N)] for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    if not visited[i][j] and grid[i][j] >= k:
                        dfs(i,j,k)
                        count += 1
            max_count = max(max_count, count)
            k -= 1
        print(max_count)


if __name__ == "__main__":
    s = Solution()
    s.safe_zone()