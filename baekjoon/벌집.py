import sys
input = sys.stdin.readline

class Solution:
    def bee(self):
        K = int(input())
        level = 1
        i = 0
        x = 0
        while True:
            if i < K <= (6*x + 1):
                print(level)
                break
            i = 6*x + 1
            x += level
            level += 1
        

if __name__ == "__main__":
    s = Solution()
    s.bee()