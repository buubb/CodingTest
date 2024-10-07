class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        return sum(sorted(nums)[::2])
        # pair = []
        # nums.sort()
        # result = 0
        # for i in range(len(nums)):
        #     pair.append(nums[i])

        #     if len(pair) == 2:
        #         result += min(pair)
        #         pair = []
            
        # return result
