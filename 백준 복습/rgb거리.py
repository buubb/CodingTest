import sys
input = sys.stdin.readline

class Solution:
    def rgb_(self):
        n = int(input())
        home = [list(map(int, input().split())) for _ in range(n)]
        
        for x in range(1,n):
            home[x][0] = min(home[x][0] + home[x-1][1], home[x][0] + home[x-1][2])
            home[x][1] = min(home[x][1] + home[x-1][0], home[x][1] + home[x-1][2])
            home[x][2] = min(home[x][2] + home[x-1][0], home[x][2] + home[x-1][1])
        
        print(min(home[n-1]))
        

if __name__ == "__main__":
    s = Solution()
    s.rgb_()