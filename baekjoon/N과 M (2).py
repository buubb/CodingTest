import sys
input = sys.stdin.readline

class Solution:
    def n_m(self):
        N, M = map(int, input().split())
        arr = [i for i in range(1, N+1)]

        def make(idx, res):
            if len(res) == M:
                print(*res)
                return
            
            for i in range(idx, N):
                make(i+1, res + [arr[i]])
        
        make(0,[])
            

if __name__ == "__main__":
    s = Solution()
    s.n_m()