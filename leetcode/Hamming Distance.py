import sys
input = sys.stdin.readline

class Solution:
    def hamming_dist(self):
        x,y = map(int, input().split())
        print(bin(x^y).count('1'))

if __name__ == "__main__":
    s = Solution()
    s.hamming_dist()