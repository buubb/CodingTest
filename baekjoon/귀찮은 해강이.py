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

    def answer(self):
        n, m = map(int, input().split())
        parent = [i for i in range(n+1)]
        for _ in range(m):
            i, j = map(int, input().split())
            self.union(i,j,parent)
        schedule = list(map(int, input().split()))
        cnt = 0
        for i in range(len(schedule)-1):
            if self.find(schedule[i], parent) != self.find(schedule[i+1], parent):
                cnt += 1
        print(cnt)
if __name__ == "__main__":
    s = Solution()
    s.answer()