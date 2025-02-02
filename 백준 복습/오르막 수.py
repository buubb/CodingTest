import sys
input = sys.stdin.readline

class Solution:
    def ascend_number(self):
        n = int(input())
        dp = [[1]*10 for _ in range(n+1)]
        for x in range(2, n+1):
            for i in range(1,10):
                dp[x][i] = dp[x-1][i] + dp[x][i-1]
        print(sum(dp[n])%10_007)
        # 1차원 배열 활용
        # dp = [1]*10
        # for x in range(n-1):
        #     for j in range(1, 10):
        #         dp[j] += dp[j-1]

if __name__ == "__main__":
    s = Solution()
    s.ascend_number()
