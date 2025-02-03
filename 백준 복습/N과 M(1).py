import sys
input =sys.stdin.readline

class Solution:
    def n_m(self):
        n, m = map(int, input().split())
        arr = []
        def dfs():
            if len(arr) == m:
                print(*arr)
                return
            
            for i in range(1, n+1):
                if i not in arr:
                    arr.append(i)
                    dfs()
                    arr.pop()

        dfs()

if __name__ == "__main__":
    s = Solution()
    s.n_m()
    