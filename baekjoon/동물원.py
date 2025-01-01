import sys
input = sys.stdin.readline

class Solution:
    def zoo(self):
        N = int(input())
        dp = [1] * (N+1)
        dp[1] = 3
        for i in range(2, N+1):
            dp[i] = (2*dp[i-1] + dp[i-2])%9901
        print(dp[N])

if __name__ == "__main__":
    s = Solution()
    s.zoo()