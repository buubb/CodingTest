import sys
input =sys.stdin.readline

class Solution:
    def zoo(self):
        n = int(input())
        dp = [0] * (n+1)
        if n == 1:
            print(3)
            return
        dp[1], dp[2] = 3, 7
        for x in range(3, n+1):
            dp[x] = (2*dp[x-1] + dp[x-2]) % 9901
        print(dp[n])
        
if __name__ == "__main__":
    s = Solution()
    s.zoo()