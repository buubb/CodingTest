import sys
input = sys.stdin.readline

class Solution:
    def sort_inside(self):
        arr = list(map(int, input().strip()))
        arr.sort(reverse=True)
        print(''.join(map(str, arr)))

if __name__ ==  "__main__":
    s = Solution()
    s.sort_inside()