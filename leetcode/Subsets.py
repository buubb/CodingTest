class Solution:
    def subsets(self):
        result = []
        nums = [1,2,3]  
        def dfs(index:int, temp = []):
            result.append(temp)
            print(temp)
            for i in range(index, len(nums)):
                dfs(i+1, temp+[nums[i]]) # append와 다르게 독립적인 리스트를 생성 / 참조 X
          
        dfs(0, [])
        return result

s = Solution()
print(s.subsets())