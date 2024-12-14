import sys
from collections import defaultdict
input = sys.stdin.readline

class Solution:
    def nohear_nolook(self):
        N, M = map(int, input().split())
        person = defaultdict(int)
        res = []
        for _ in range(N+M):
            name = input()
            person[name] += 1
            if person[name] >= 2:
                res.append(name)
        print(len(res))
        print(''.join(sorted(res)), end= '')

if __name__ == "__main__":
    s = Solution()
    s.nohear_nolook()