import sys
input = sys.stdin.readline

class Solution:
    def nm(self):
        n,m=map(int, input().split())
        arr = []
        def dfs(k):
            if len(arr) == m:
                print(*arr)
                return
            
            for i in range(k, n+1):
                if i not in arr:
                    arr.append(i)
                    # print(arr)
                    dfs(i+1)
                    arr.pop()
        
        dfs(1)

if __name__ == "__main__":
    s = Solution()
    s.nm()