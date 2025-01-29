import sys
input = sys.stdin.readline

class Solution:
    def upstairs(self):
        n = int(input())
        nums = [int(input()) for _ in range(n)]
        if len(nums) == 1:
            print(nums[0])
            return
        elif len(nums) == 2:
            print(nums[0] + nums[1])
            return
        elif len(nums) == 3:
            print(max(nums[0] + nums[2], nums[1] + nums[2]))
            return
        dp = [0] * 300
        dp[0] = nums[0]
        dp[1] = nums[0] + nums[1]
        dp[2] = max(nums[0] + nums[2], nums[1] + nums[2])
        for x in range(3, n):
            dp[x] = max(dp[x-2] + nums[x], dp[x-3] + nums[x-1] + nums[x])
            
        print(dp[n-1])
            



if __name__ == "__main__":
    s = Solution()
    s.upstairs()