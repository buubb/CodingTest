import sys
input = sys.stdin.readline

class Solution:
    def sum_123(self):
        n = int(input())
        nums = [int(input()) for _ in range(n)]
        l = max(nums)
        dp = [0] * (l+1)
        dp[1], dp[2], dp[3] = 1, 2, 4
        for i in range(4, l+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        for k in nums:
            print(dp[k])

if __name__ == "__main__":
    s = Solution()
    s.sum_123()