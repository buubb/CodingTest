import sys
from collections import defaultdict
input = sys.stdin.readline

class Solution:
    def major_elem(self):
        nums = list(map(int, input().split()))
        def backtracking(nums):
            if not nums:
                return None
            if len(nums) == 1:
                return nums[0]
            
            half = len(nums) // 2
            a = backtracking(nums[:half])
            b = backtracking(nums[half:])

            return [b, a][nums.count(a) > half]
        print(backtracking(nums))

    def major_elem_(self):
        nums = list(map(int, input().split()))
        counts = defaultdict(int)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)

            if counts[num] > len(nums) // 2:
                print(num)
                break

if __name__ == "__main__":
    s = Solution()
    s.major_elem_()