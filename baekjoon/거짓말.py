import sys
input = sys.stdin.readline

class Solution:
    def find(self, k, parent):
        if parent[k] != k:
            parent[k] = self.find(parent[k], parent)
        return parent[k]
    
    def union(self, a, b, parent, truth):
        r1 = self.find(a, parent)
        r2 = self.find(b, parent)

        if r1 in truth and r2 in truth:
            return
        if r1 in truth:
            parent[r2] = r1
        elif r2 in truth:
            parent[r1] = r2
        else:    
            if r1 < r2:
                parent[r2] = r1
            else:
                parent[r1] = r2

    def lier(self):
        n, m = map(int, input().split())
        t_mem = list(map(int, input().split()))[1:]
        parent = [i for i in range(n+1)]
        parties = []
        
        for _ in range(m):
            party = list(map(int, input().split()))
            party_len = party[0]
            party_m = party[1:]

            for i in range(party_len-1):
                self.union(party_m[i], party_m[i+1], parent, t_mem)
            parties.append(party_m)

        res = 0
        for p in parties:
            for i in range(len(p)):
                if self.find(p[i], parent) in t_mem:
                    break
            else:
                res += 1
        
        print(res)

if __name__ == "__main__":
    s = Solution()
    s.lier()