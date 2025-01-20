import sys, string
input = sys.stdin.readline

class Solution:
    def hashing(self):
        l = int(input())
        char = list(input().strip())
        alphabets = [i for i in string.ascii_lowercase]
        num = 0
        for i in range(l):
            for j in range(26):
                if char[i] == alphabets[j]:
                    num = (num + (j+1) * 31**i) % 1234567891
                    break

        print(num)
if __name__ == "__main__":
    s = Solution()
    s.hashing()