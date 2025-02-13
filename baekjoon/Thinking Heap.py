import sys
input = sys.stdin.readline

class Solution:
    def thinking_heap(self):
        n = int(input())
        hp = [None] * (n+1)
        k, p = map(int, input().split())
        used = [False] * (n+1)
        if k-1 < p//2:
            print(-1)
            return
        
        def btk(idx, k):
            if idx < 0 or idx > n or k < 1 or k>n or used[k] or hp[idx]:
                return
            if hp[idx] is None:
                hp[idx] = k
                used[k] = True
            
            btk(idx//2, k-1)
            btk(2*idx, k+1)
            btk(2*idx + 1, k+2)
        
        btk(p, k)
        for j in range(1,n+1):
            for i in range(1,n+1):
                if hp[i] is None and not used[j]:
                    hp[i] = j
                    break

        for h in hp[1:]:
            print(h)
   

if __name__ == "__main__":
    s = Solution()
    s.thinking_heap()