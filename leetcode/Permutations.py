class Solution:
    def permute(self, nums:list) -> list:
        result = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                result.append(prev_elements[:])
                print(prev_elements[:])
                
            for e in elements:
                next_e = elements[:]
                next_e.remove(e)
                print(e, next_e)

                prev_elements.append(e)
                dfs(next_e)
                prev_elements.pop()

        dfs(nums)
        return result
    
import itertools
class Solution2:
    def permute(self, nums:list) -> list:
        print(list(map(list,itertools.permutations(nums))))

nums = list(map(int, input()))
s = Solution2()
print(s.permute(nums))