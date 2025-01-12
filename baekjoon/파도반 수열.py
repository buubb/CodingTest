import sys
input = sys.stdin.readline

class Solution:
    def wave(self):
        T = int(input())
        for _ in range(T):
            N = int(input())
            dp = [1] * (N+1)
            if N <= 3:
                print(1)
            elif N==4 or N==5:
                print(2)
            else:
                dp[4]=dp[5]=2
                for i in range(6, N+1):
                    dp[i] = dp[i-1] + dp[i-5]
                print(dp[N])

if __name__ == "__main__":
    s = Solution()
    s.wave()