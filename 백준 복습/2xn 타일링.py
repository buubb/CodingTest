import sys
input = sys.stdin.readline

class Solution:
    def nx2(self):
        n = int(input())
        if n == 1:
            print(1)
            return
        dp = [0] * (n+1)
        dp[1], dp[2] = 1,2
        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2]) % 10_007
        print(dp[n])

if __name__ == "__main__":
    s = Solution()
    s.nx2()