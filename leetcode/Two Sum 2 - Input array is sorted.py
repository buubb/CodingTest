import bisect
class Solution:
    def twoSum(self, numbers:list, target:int) -> list:
        left, right = 0, len(numbers)-1
        while not left == right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                print([left+1, right+1])
                break
    
    def twoSum_2(self, numbers:list, target:int) -> list:
        for k, v in enumerate(numbers):
            left, right = k+1, len(numbers)-1
            value = target - v
            while left <= right:
                mid = left + (right-left) // 2
    
                if numbers[mid] > value:
                    right -= 1
                elif numbers[mid] < value:
                    left += 1
                else:
                    print([k+1, mid +1])
                    break
    
    def twoSum_3(self, numbers:list, target:int) -> list:
        for k, v in enumerate(numbers):
            value = target - v
            i = bisect.bisect_left(numbers, value, k+1)
            if i < len(numbers) and numbers[i] == value:
                print([k+1, i+1])



if __name__ == "__main__":
    s = Solution()
    s.twoSum_3([2,7,11,15],9)