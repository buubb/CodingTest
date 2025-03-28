import sys
input = sys.stdin.readline

class Solution:
    def answer(self): # 나 브루트 포스 왜 못하는겨
        n = int(input())
        arr = []
        res = []
        for _ in range(n):
            w, h = map(int, input().split())
            arr.append((w, h))
            
        for i in range(n):
            count = 0
            for j in range(n):
                if arr[j][1] > arr[i][1] and arr[j][0] > arr[i][0]:
                    count += 1
            res.append(count+1)

        print(*res)
if __name__ == "__main__":
    s = Solution()
    s.answer()