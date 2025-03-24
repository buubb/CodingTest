import sys
input = sys.stdin.readline

class Solution:
    def n_m(self):
        n, m = map(int, input().split())
        nums = list(map(int, input().split()))

        def backtracking(arr):
            if len(arr) == m:
                print(*arr)
                return
            
            for i in sorted(nums):
                if i not in arr:
                    arr.append(i)
                    backtracking(arr)
                    arr.pop()

        backtracking([])
        

if __name__ == "__main__":
    s = Solution()
    s.n_m()