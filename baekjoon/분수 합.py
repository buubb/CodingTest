import sys
input = sys.stdin.readline

class Solution:
    def answer(self):
        a1, b1 = map(int, input().split())
        a2, b2 = map(int, input().split())
    
        c, d = a1*b2 + a2*b1, b1*b2
        # 기약분수를 어떻게 구하니
        k = self.gcd(c, d)
        print(c//k, d//k)

    def gcd(self, a, b):
        if b != 0:
            return self.gcd(b, a%b)
        return a

if __name__ == "__main__":
    s = Solution()
    s.answer()