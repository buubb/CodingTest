import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
class Solution:
    def find(self, k, parent):
        if parent[k] != k:
            parent[k] = self.find(parent[k], parent)
        return parent[k]
    
    def union(self, a, b, parent):
        r1 = self.find(a, parent)
        r2 = self.find(b, parent)

        if r1 < r2:
            parent[r2] = r1
        else:
            parent[r1] = r2

    def answer(self):
        n, m = map(int, input().split())
        parent = [i for i in range(n+1)]
        for _ in range(m):
            k, v1, v2 = map(int, input().split())
            if k == 0:
                self.union(v1,v2, parent)
            elif k == 1:
                if self.find(v1, parent) == self.find(v2, parent):
                    print("YES")
                else:
                    print("NO")

if __name__ == "__main__":
    s = Solution()
    s.answer()