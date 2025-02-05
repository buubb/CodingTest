import sys
input = sys.stdin.readline

class Solution:
    def easy_stairs(self):
        N = int(input())
        dp = [[0] * 10 for _ in range(101)]
        for i in range(N+1):
            for j in range(10):
                if i==0:  
                    dp[i][j] = 0
                elif i == 1:
                    dp[i][j] = 1
                elif j == 0:
                    dp[i][j] = dp[i-1][j+1]
                elif j == 9:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        
        print((sum(dp[N][i] for i in range(1,10))) % 1_000_000_000)
        

if __name__ == "__main__":
    s = Solution()
    s.easy_stairs()