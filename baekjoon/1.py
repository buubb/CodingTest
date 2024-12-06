import sys
input = sys.stdin.readline

class Solution:
    def one(self):
        while True:
            try:
                N = int(input())
            except:
                break
            if N%2 ==0 or N%5==0:
                return
            c = 0
            num = 1
            while True:
                if num % N == 0:
                    print(c+1)
                    break
                else:
                    c += 1
                    num += 10**c

if __name__ == "__main__":
    s = Solution()
    s.one()