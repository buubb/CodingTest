import sys
input = sys.stdin.readline

class Solution:     
    def answer(self):
        # 소수 구하기
        arr = [0]*2 + [1]*246911
        for i in range(2, 123456+1):
            if arr[i] == 1:
                k = 2
                while i*k < 246912+1:
                    arr[i*k] = 0
                    k += 1

        while True:
            n = int(input())
            if n == 0:
                break
            print(sum(arr[n+1:2*n+1]))

if __name__ == "__main__":
    s = Solution()
    s.answer()