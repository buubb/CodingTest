candi = [2,3,6,7]
target = 7
result = []
class Solution:
    def combine_sum(self, candi:list, target:int, index:int, temp):
        if target < 0:
            return
        
        elif target == 0:
            print(temp[:])
            result.append(temp[:])
            return
        
        for i in range(index, len(candi)):
            self.combine_sum(candi, target-candi[i], i, temp + [candi[i]])
        
            

        return result
    
s = Solution()
print(s.combine_sum(candi, target, 0, []))