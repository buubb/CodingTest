import sys
input = sys.stdin.readline

class Solution:
    def sort_x_y(self):
        N = int(input())
        grid = []
        for _ in range(N):
            (x,y) = map(int, input().split())
            grid.append((x,y))
        for (x,y) in sorted(grid, key=lambda x:(x[0], x[1])):
            print(x,y)

if __name__ == "__main__":
    s = Solution()
    s.sort_x_y()