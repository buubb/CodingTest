import sys
input = sys.stdin.readline

class Solution:
    def substring(self):
        while True:
            line = input().rstrip()
            if not line:
                break
            s, t = line.split()
            
            i = 0
            isSubstring = False
            for char in t:
                if i >= len(s):
                    break
                if char == s[i]:
                    if i == len(s)-1:
                        isSubstring = True
                    i += 1
            if not isSubstring:
                print("No")
            else:
                print("Yes")

if __name__ == "__main__":
    s = Solution()
    s.substring()