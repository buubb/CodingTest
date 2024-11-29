from sys import stdin
class Solution:
    res: int = 0
    def APT(self):
        N = int(stdin.readline())
        grid = []
        for i in range(N):
            arr = list(map(int, stdin.readline().strip()))
            grid.append(arr)
        
        def dfs(i, j):
            if i < 0 or i >= N or j < 0 or j >= N or grid[i][j] != 1:
                return 0
            
            grid[i][j] = 0

            return 1 + dfs(i, j-1) + dfs(i, j+1) + dfs(i-1,j) + dfs(i+1,j)

        count = 0
        res = []
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    n = dfs(i,j)
                    count += 1
                    res.append(n)

        print(count)
        for i in sorted(res):
            print(i)

if __name__ == "__main__":
    s = Solution()
    s.APT()