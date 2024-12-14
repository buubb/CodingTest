import sys
input = sys.stdin.readline

class Solution:
    def sorted_words(self):
        N=int(input())
        words = set()
        for _ in range(N):
            w = input()
            words.add((w, len(w)))
        res = sorted(words,key=(lambda x: (x[1], x[0])))
        for i in range(len(res)):
            print(res[i][0], end='')

if __name__ == "__main__":
    s = Solution()
    s.sorted_words()