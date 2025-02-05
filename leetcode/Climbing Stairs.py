import sys
input = sys.stdin.readline

class Solution:
    def climbing_stairs(self):
        n = int(input())
        if n <= 2:
            return n
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2
        for i in range(3,n+1):
            dp[i] = dp[i-2] + dp[i-1]
        print(dp[n])

if __name__ == "__main__":
    s = Solution()
    s.climbing_stairs()