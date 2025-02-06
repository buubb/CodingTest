import sys
input = sys.stdin.readline

class Solution:
    def subarrsum(self):
        n, s = map(int, input().split())
        arr = list(map(int, input().split()))
        cnt = 0
        a = []
        def backtracking(idx, res):
            nonlocal cnt
            if res == s:
                cnt += 1
       
            for i in range(idx+1, n):
                backtracking(i, res + arr[i])
        
        for i in range(n):
            backtracking(i, arr[i])

        print(cnt)

if __name__ == "__main__":
    s = Solution()
    s.subarrsum()