import sys
input = sys.stdin.readline

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

    def application(self):
        t = int(input())
        result = []
        for _ in range(t):
            n = int(input())
            k = int(input())
            parent = [i for i in range(n)]
            for _ in range(k):
                v1, v2 = map(int, input().split())
                self.union(v1, v2, parent)
            m = int(input())
            res = []
            for _ in range(m):
                a, b = map(int, input().split())
                if self.find(a, parent) != self.find(b, parent):
                    res.append(0)
                else:
                    res.append(1)
            result.append(res)
        for i in range(t):
            print(f"Scenario {i+1}:")
            for k in result[i]:
                print(k)
            print()
            
if __name__ == "__main__":
    s = Solution()
    s.application()