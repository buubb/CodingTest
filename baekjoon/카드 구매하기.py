import sys
input = sys.stdin.readline

class Solution:
    def pay_card(self):
        N = int(input())
        price = [0] + list(map(int, input().split()))
        dp = [0] * (N+1)

        for i in range(1, N+1):
            for j in range(1,i+1):
                dp[i] = max(dp[i], dp[i-j] + price[j])

        print(dp[N])

if __name__ == "__main__":
    s = Solution()
    s.pay_card()