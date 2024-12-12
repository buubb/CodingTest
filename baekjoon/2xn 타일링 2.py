import sys
input = sys.stdin.readline

class Solution:
    def tiling_2(self):
        N = int(input())
        if N == 1:
            print(1)
            return
        dp = [0] * (N+1)
        dp[1], dp[2] = 1,3
        for i in range(3, N+1):
            dp[i] = (dp[i-1] + dp[i-2] * 2)%10007
        print(dp[N])

if __name__ == "__main__":
    s = Solution()
    s.tiling_2()