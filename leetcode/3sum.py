class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        zero_sum = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i>0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, len(nums)-1
            while left < right:
                result = nums[i] + nums[left] + nums[right]
                if result < 0:
                    left += 1
                elif result > 0:
                    right -=1
                else:
                    zero_sum.append((nums[i], nums[left], nums[right]))
                    
                    while left<right and nums[left] == nums[left+1]:
                        left+=1
                    while left<right and nums[right] == nums[right-1]:
                        right-=1
                    left += 1
                    right -= 1
        
        return zero_sum