import sys
input = sys.stdin.readline

class Solution:
    def answer(self):
        n = int(input())
        arr = []
        
        for idx in range(n):
            w, h = map(int, input().split())
            arr.append((w+h, w, h, idx))
       
        arr.sort()
        ranks = [n] * n
        for i in range(n):
            if arr[i][1] > arr[i+1][1] and arr[i][2] > arr[i+1][2]:
                ranks[arr[i][3]] -= 1
            

if __name__ == "__main__":
    s = Solution()
    s.answer()