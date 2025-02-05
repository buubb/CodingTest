import sys
input = sys.stdin.readline

class Solution:
    def coins(self):
        n, k = map(int, input().split())
        coin = [int(input()) for _ in range(n)]
        dp = [0]*(k+1)
        dp[0] = 1 # 동전 없이 0원을 만드는 경우의 수
        for c in coin:
            for i in range(c, k+1):
                dp[i] = dp[i] + dp[i-c]
        print(dp[k])


if __name__ == "__main__":
     s = Solution()
     s.coins()