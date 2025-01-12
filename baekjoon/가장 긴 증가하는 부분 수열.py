import sys
input = sys.stdin.readline

class Solution:
    def num_set(self):
        N = int(input())
        A = list(map(int, input().split()))
        dp = [0] * N
        ma = 0
        for i in range(N):
            dp[i] = 1
            for j in range(i):
                if A[j] < A[i]:
                    dp[i] = max(dp[i], dp[j]+1)
            ma = max(ma, dp[i])
        print(ma)

if __name__ == "__main__":
    s = Solution()
    s.num_set()