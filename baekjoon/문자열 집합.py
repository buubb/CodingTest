import sys
from collections import defaultdict
input = sys.stdin.readline

class Solution:
    def char_set(self):
        N, M = map(int, input().split())
        char = defaultdict(bool)
        for _ in range(N):
            c = input().strip()
            char[c] = True
        cnt = 0
        for _ in range(M):
            i = input().strip()
            if char[i]:
                cnt += 1
        print(cnt)

if __name__ == "__main__":
    s = Solution()
    s.char_set()