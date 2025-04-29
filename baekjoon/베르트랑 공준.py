import sys
input = sys.stdin.readline

class Solution:
    def is_prime(self, n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
            

    def answer(self):
        while True:
            n = int(input())
            if n == 0:
                break

            # 소수 구하기
            cnt = 0
            for k in range(n+1, 2*n+1):
                if self.is_prime(k):
                    cnt += 1
            print(cnt)

if __name__ == "__main__":
    s = Solution()
    s.answer()