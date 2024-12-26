import bisect
class Solution:
    def search(self, nums:list, target:int) -> int:
        def binary_search(left, right):
            if left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    return binary_search(mid+1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid-1)
                else:
                    return mid
            else:
                return -1
        
        return binary_search(0, len(nums)-1)
    
    def search_2(self, nums:list, target:int) -> int:
        left = 0
        right = len(nums) -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
            else:
                return mid
        
        return -1
    
    def search_3(self, nums:list, target:int) -> int:
        idx = bisect.bisect_left(nums, target)

        if idx < len(nums) and nums[idx] == target:
            return idx
        else:
            return -1

    def search_4(self, nums:list, target:int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1

if __name__ == "__main__":
    s = Solution()
    res = s.search([-1,0,3,5,9,12],9)
    print(res)