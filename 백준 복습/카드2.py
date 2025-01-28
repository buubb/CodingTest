import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def card_2(self):
        n = int(input())
        card = deque()
        for i in range(1, n+1):
            card.append(i)
        while len(card) > 1:
            card.popleft()
            k = card.popleft()
            card.append(k)
        print(card.popleft())

if __name__ == "__main__":
    s = Solution()
    s.card_2()