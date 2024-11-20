class Solution:
    def combinations(self,n:int,k:int):
        def dfs(elements, start:int, k:int):
            if k == 0:
                results.append(elements[:])
                return
            
            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()
        
        results = []

        dfs([], 1, k)
        return results
    
import itertools
class Solution2:
    def combinations(self, n:int, k:int) -> list:
        print(list(itertools.combinations(range(1,n+1), k)))
        
s = Solution2()
print(s.combinations(5,3))


