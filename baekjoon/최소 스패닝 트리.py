import sys, heapq
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
        v, e = map(int, input().split())
        parent = list(range(v+1))
        hq = []
        for _ in range(e):
            v1, v2, w = map(int, input().split())
            heapq.heappush(hq, (w, v1, v2))
        res = 0
        while hq:
            w1, a, b = heapq.heappop(hq)
            if self.find(a, parent) == self.find(b, parent):
                continue
            self.union(a, b, parent)
            res += w1
        print(res)



if __name__ == "__main__":
    s = Solution()
    s.answer()
