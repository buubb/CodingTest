
class Solution:
    def singleNumber(self, nums:list):
        result = 0
        for num in nums:
            result ^= num
        print(result)

if __name__ == "__main__":
    s = Solution()
    arr = [4,1,2,1,2]
    s.singleNumber(arr)