import sys
input = sys.stdin.readline

class Solution:
    def answer(self):
        n = int(input())
        if n==1:
            print(1)
            return
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2
        for x in range(3, n+1):
            dp[x] = (dp[x-1] + dp[x-2]) % 15746
        print(dp[n])

if __name__ == "__main__":
    s = Solution()
    s.answer()