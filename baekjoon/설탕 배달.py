import sys
input = sys.stdin.readline

class Solution:
    def sugar(self):
        N = int(input())
        dp = [-1] * 5001
        dp[3], dp[4], dp[5] = 1, -1 , 1
        for n in range(6, N+1):
            if n % 5 == 0:
                dp[n] = dp[n-5]+1
            elif n%3 == 0:
                dp[n] = dp[n-3]+1
            elif dp[n-3] > 0 and dp[n-5] >0:
                dp[n] = min(dp[n-3]+1, dp[n-5]+1)
        print(dp[N])

if __name__=="__main__":
    s = Solution()
    s.sugar()