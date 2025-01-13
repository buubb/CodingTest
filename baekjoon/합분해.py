import sys
from itertools import combinations
input = sys.stdin.readline

class Solution:
    def divide_sum(self):
        N, K = map(int, input().split())
        dp = [[1 for _ in range(K+1)] for _ in range(N+1)]
        for i in range(1, N+1):
            for j in range(2, K+1):
                if i==1:
                    dp[i][j] = 1*j
                else:
                    dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1_000_000_000
        print(dp[N][K])

    def divide_sum2(self): # 메모리 초과 - combinations 모듈 때문
        N, K = map(int, input().split())
        print(len(list(combinations(range(N+K-1),K-1)))% 1_000_000_000)

if __name__ == "__main__":
    s = Solution()
    s.divide_sum2()