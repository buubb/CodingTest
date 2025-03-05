import sys
input = sys.stdin.readline

class Solution:
    def answer(self):
        N = int(input())
        k = int(input())
        
        d = [(1,0), (0,1), (-1, 0), (0,-1)]
        grid = [[0]*N for _ in range(N)]
        x, y, num, i = 0, 0, N**2, 0
        while num > 0:
            grid[x][y] = num

            if num == k:
                rx, ry = x+1, y+1

            dx, dy = d[i][0] + x, d[i][1] + y
            if not (0<=dx<N and 0<=dy<N) or grid[dx][dy] != 0:
                i = (i+1) % 4
                dx, dy = d[i][0] + x, d[i][1] + y
            
            num -= 1
            x, y = dx, dy
        
        for g in grid:
            print(*g)
        print(rx, ry)


if __name__ == "__main__":
    s = Solution()
    s.answer()