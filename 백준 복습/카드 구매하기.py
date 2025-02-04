import sys
input = sys.stdin.readline

class Solution:
    def buy_cards(self):
        n = int(input())
        cards = [0] + list(map(int, input().split()))
        dp = [0] * (n+1)
        for i in range(1, len(cards)):
            for j in range(1, i+1):
                dp[i] = max(dp[i], dp[i-j] + cards[j])
                print(dp)
        print(dp[n])
       

if __name__ == "__main__":
    s = Solution()
    s.buy_cards()