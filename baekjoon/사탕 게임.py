import sys
input = sys.stdin.readline

class Solution:
    def candy_game(self):
        N = int(input())
        grid = [list(input().strip()) for _ in range(N)]
        
        res = 0
        def calculate():
            max_count = 1
            for i in range(N):
                cnt = 1
                for j in range(1,N):
                    if grid[i][j] == grid[i][j-1]:
                        cnt += 1
                    else:
                        cnt = 1
                    max_count = max(max_count, cnt)
                cnt = 1
                for j in range(1,N):
                    if grid[j][i] == grid[j-1][i]:
                        cnt += 1
                    else:
                        cnt = 1
                    max_count = max(max_count, cnt)
            return max_count
        
        for x in range(N):
            for y in range(N-1):
                if grid[x][y] != grid[x][y + 1]:
                    grid[x][y], grid[x][y+1] = grid[x][y+1], grid[x][y]
                    res = max(res, calculate())
                    grid[x][y], grid[x][y+1] = grid[x][y+1], grid[x][y]
                
                if x < N-1 and grid[x][y] != grid[x+1][y]:
                    grid[x][y], grid[x+1][y] = grid[x+1][y], grid[x][y]
                    res = max(res, calculate())
                    grid[x][y], grid[x+1][y] = grid[x+1][y], grid[x][y]
        
        print(res)
            



                
        

if __name__ == "__main__":
    s = Solution()
    s.candy_game()