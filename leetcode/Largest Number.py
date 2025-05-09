class Solution:
    @staticmethod
    def to_swap(n1:int, n2:int) -> bool:
        return str(n1)+str(n2) < str(n2)+str(n1)
    
    def largestNumber(self, nums:list) -> str:
        i=1
        while i < len(nums):
            j=i
            while j>0 and self.to_swap(nums[j-1], nums[j]):
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j-=1
            i+=1

        return str(int(''.join(map(str, nums))))

if __name__ == "__main__":
    s = Solution()
    arr = [3,30,34,5,9]
    print(s.largestNumber(arr))