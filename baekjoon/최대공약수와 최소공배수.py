from sys import stdin
class Solution:
    def main(self):
        m , n = map(int, stdin.readline().split())
        k = self.big(m,n)
        print(k)
        print(m*n//k)

    def big(self, a:int, b:int):
        while b != 0:
            a,b = b, a%b
        return a
    
s = Solution()
s.main()