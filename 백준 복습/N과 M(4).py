import sys
from itertools import product
input = sys.stdin.readline

class Solution:
    def n_m_(self):
        n,m = map(int, input().split())
        for a in product(range(1,n+1), repeat = m):
            isOk = True
            for i in range(m-1):
                if a[i] > a[i+1]:
                    isOk = False
                    break  
            if isOk:  
                print(*a)

    def n_m_4(self):
        n,m = map(int, input().split())
        s = []
        def dfs(k):
            if len(s) == m:
                print(*s)
                return
            
            for i in range(k,n+1):
                s.append(i)
                dfs(i)
                s.pop()
        
        dfs(1)
        
if __name__ == "__main__":
    s = Solution()
    s.n_m_4()