import sys
from collections import defaultdict
input = sys.stdin.readline

class Solution:
    def isFind(self, k, parent):
        if parent[k] != k:
            parent[k] = self.isFind(parent[k], parent)
        return parent[k]
    
    def union(self, a, b, parent):
        r1 = self.isFind(a, parent)
        r2 = self.isFind(b, parent)

        if r1 < r2:
            parent[r2] = r1
        else:
            parent[r1] = r2
    
    def answer(self):
        n, m = map(int, input().split())
        parent = [i for i in range(n+1)]
        count = defaultdict(int)
        for _ in range(m):
            v1, v2 = map(int, input().split())
            # union 합치기
            self.union(v1, v2, parent)
        print(parent)
        for i in range(1, len(parent)):
            root = self.isFind(i, parent)
            count[root] += 1
        res = 1
        for c in count.values():
            res *= c
            res %= 1_000_000_007
        
        print(res)
        


if __name__ == "__main__":
    s = Solution()
    s.answer()