import sys
from collections import Counter
input = sys.stdin.readline

class Solution:
    def checker(self):
        N = int(input())
        cnt = N

        for i in range(N):
            word = input()
            for j in range(0, len(word)-1):
                if word[j] == word[j+1]:
                    pass
                elif word[j] in word[j+1:]:
                    cnt -= 1
                    break

        print(cnt)
            

if __name__ == "__main__":
    s = Solution()
    s.checker()
