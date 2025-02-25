import sys
from itertools import combinations
input = sys.stdin.readline

class Solution:
    def answer(self):
        n = int(input())
        m = n-2
        parent = [i for i in range(n+1)]
        def isFind(k, parent):
            if parent[k] != k:
                parent[k] = isFind(parent[k], parent)
            return parent[k]
        
        def union(a, b, parent):
            r1 = isFind(a, parent)
            r2 = isFind(b, parent)

            if r1 < r2:
                parent[r2] = r1
            else:
                parent[r1] = r2

        for _ in range(m):
            v1, v2 = map(int, input().split())
            union(v1, v2, parent)
        
        for a, b in combinations(range(1, n+1), 2):
            if isFind(a, parent) != isFind(b, parent):
                print(a, b)
                break

        
if __name__ == "__main__":
    s = Solution()
    s.answer()