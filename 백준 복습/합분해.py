import sys
input = sys.stdin.readline

class Solution:
    def divide_sum(self):
        n, k = map(int, input().split())
        dp = [[0] * (n+1) for _ in range(k+1)]

        for i in range(k+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    continue
                if i == 1:
                    dp[i][j] = 1
                elif j == 1:
                    dp[i][j] = i % 1_000_000_000
                else:
                    dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1_000_000_000
        
        print(dp[k][n])

if __name__ == "__main__":
    s = Solution()
    s.divide_sum()