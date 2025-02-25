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
            
    def trip(self):
        N = int(input())
        M = int(input())
        parent = [i for i in range(N+1)]
        arr = []
        for _ in range(N):
            arr.append(list(map(int, input().split())))
        
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 1 and self.find(i+1, parent) != self.find(j+1, parent):
                    self.union(i+1, j+1, parent)
        
        schedule = list(map(int, input().split()))
        for i in range(M-1):
            if self.find(schedule[i], parent) != self.find(schedule[i+1], parent):
                print("NO")
                return
        print("YES")

        

if __name__ == "__main__":
    s = Solution()
    s.trip()