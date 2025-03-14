import sys
from collections import defaultdict
input = sys.stdin.readline

class Solution:
    def find(self, k, parent):
        if parent[k] != k:
            parent[k] = self.find(parent[k], parent)
        return parent[k]
    
    def union(self, a, b, parent, planets, cnt):
        r1 = self.find(a, parent)
        r2 = self.find(b, parent)
        if r1 != r2:
            if r1 < r2:
                planets[r1] += planets[r2]
                parent[r2] = r1
            else:
                parent[r1] = r2
                planets[r2] += planets[r1]
            
        print(planets[self.find(r1, parent)])

    def answer(self):
        n, m = map(int, input().split())
        planets = [0] + list(int(input()) for _ in range(n))
        parent = list(range(n+1))
        cnt = defaultdict(int)
        for _ in range(m):
            a, b = map(int, input().split())
            self.union(a,b,parent, planets, cnt)

if __name__ == "__main__":
    s = Solution()
    s.answer()