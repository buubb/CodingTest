from sys import stdin
class Solution:
    def star_5(self):
        n = int(stdin.readline())
        m = 0
        k = n
        while m < n:
            for i in range(m):
                print(" ", end='')
            for j in range(k):
                print("*", end='')
            print()
            k-=1
            m+=1
if __name__ == "__main__":
    s = Solution()
    s.star_5()