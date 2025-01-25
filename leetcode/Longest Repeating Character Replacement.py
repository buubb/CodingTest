import sys
from collections import Counter
input = sys.stdin.readline

class Solution:
    def replacement_char(self):
        s = input().strip()
        k = int(input())
        left = right = 0
        counts = Counter()
        for right in range(1, len(s)+1):
            print(s[right-1])
            counts[s[right-1]] += 1
            
            max_char_n = counts.most_common(1)[0][1]

            if right - left - max_char_n > k:
                print(counts)
                counts[s[left]] -= 1
                left += 1
                print(counts)
        print(right-left)

if __name__ == "__main__":
    s = Solution()
    s.replacement_char()