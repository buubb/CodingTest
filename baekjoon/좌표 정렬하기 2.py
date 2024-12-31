import sys
input = sys.stdin.readline

class Solution:
    def x_y(self):
        N = int(input())
        arr = []
        for _ in range(N):
            x,y = map(int, input().split())
            arr.append((x,y))
        for (x,y) in sorted(arr, key= lambda x: (x[1], x[0])):
            print(x, y)

if __name__ == "__main__":
    s = Solution()
    s.x_y()