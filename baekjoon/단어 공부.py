import sys
input = sys.stdin.readline
from collections import Counter

class Solution:
    def words_study(self):
        words = list(input().strip().upper())
        if len(words) == 0:
            return
        arr = Counter(words).most_common()
        if len(arr) > 1 and arr[0][1] == arr[1][1]:
            print("?")
            return       
        else:
            print(arr[0][0])

if __name__ == "__main__":
    s = Solution()
    s.words_study()