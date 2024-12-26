import sys
input = sys.stdin.readline

class Solution:
    def ascend_number(self):
        N = int(input())
        dp = [[1] * 10 for _ in range(N+1)]
        for i in range(1,N+1):
            for j in range(1,10):
                if i >= 2:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        print(sum(dp[N])%10007)

if __name__ == "__main__":
    s = Solution()
    s.ascend_number()
    