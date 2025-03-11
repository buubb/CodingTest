import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def burger(self):
        b, c, d = map(int, input().split())
        b_price = sorted(list(map(int, input().split())), reverse=True)
        c_price = sorted(list(map(int, input().split())), reverse=True)
        d_price = sorted(list(map(int, input().split())), reverse=True)
        menu = sum(b_price) + sum(c_price) + sum(d_price)

        res = 0
        for _ in range(min(b,c,d)):
            res += b_price.pop(0) * 0.9
            res += c_price.pop(0) * 0.9
            res += d_price.pop(0) * 0.9
        
        print(menu)
        print(int(res + sum(b_price) + sum(c_price) + sum(d_price)))

if __name__ == "__main__":
    s = Solution()
    s.burger()