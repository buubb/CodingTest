import sys
input = sys.stdin.readline

class Solution:
    def coin1(self):
        n,k = map(int, input().split())
        coins = [int(input()) for _ in range(n)]
        dp = [0]*(k+1)
        dp[0]=1
        for c in coins:
            for i in range(c,k+1):
                dp[i] = dp[i]+dp[i-c]
        print(dp[k])

if __name__ == "__main__":
    s = Solution()
    s.coin1()