import sys, string
input = sys.stdin.readline

class Solution:
    def hashing(self):
        L = int(input())
        char = input().strip()
        alphabets = [i for i in string.ascii_lowercase]
        r, m = 31, 1234567891
        res = 0
        for i in range(L):
            for j in range(26):
                if char[i] == alphabets[j]:
                    res = (res + (j+1) * (r ** i)) % m
                    break

        print(res)

    def hashing2(self):
        l = int(input())
        char = input().strip()
        res = 0
        for i in range(l):
            hash_value = (ord(char[i]) - ord('a') + 1) * 31 ** i
            res += hash_value % 1234567891
        print(res)

if __name__ == "__main__":
    s = Solution()
    s.hashing2()