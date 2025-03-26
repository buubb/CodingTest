import sys
from collections import defaultdict
input = sys.stdin.readline

class Solution:
    def answer(self):
        n, k = map(int, input().split())
        ranks = defaultdict(list)
        for _ in range(n):
            country, g, s, d = map(int, input().split())
            ranks[(g, s, d)].append(country)
        
        rank = 0
        for key in sorted(ranks, reverse=True):
            rank += 1
            if k in ranks[key]:
                print(rank)
                break
            if len(ranks[key]) > 1:
                rank += len(ranks[key]) - 1

if __name__ == "__main__":
    s = Solution()
    s.answer()