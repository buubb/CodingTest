import sys
input = sys.stdin.readline

class Solution:
    def house_robber(self):
        house = list(map(int, input().split()))
        dp = [0] * len(house)
        if len(house) <= 2:
            print(max(house))
        dp[0], dp[1] = house[0], max(house[0], house[1])
        for i in range(2, len(house)):
            dp[i] = max(dp[i-1], dp[i-2] + house[i])
        print(dp[len(house)-1])

if __name__ == "__main__":
    s = Solution()
    s.house_robber()