import sys
from itertools import combinations
input = sys.stdin.readline

class Solution:
    def make_triangle(self):
        N = int(input())
        nums = [int(input()) for _ in range(N)]
        max_num = -1
        nums.sort()
        for i in range(N - 2):
            if nums[i] + nums[i+1] > nums[i+2]:
                max_num = max(max_num, nums[i]+nums[i+1]+nums[i+2])
        
        print(max_num)
            

if __name__ == "__main__":
    s = Solution()
    s.make_triangle()