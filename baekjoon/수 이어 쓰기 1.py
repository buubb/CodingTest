import sys
input = sys.stdin.readline

class Solution:
    # 메모리 초과
    def relay_number_(self):
        n = int(input())
        nums = ''.join(map(str, range(1,n+1)))
        print(len(nums))
    # 시간 초과
    def relay_number__(self):
        n = int(input())
        res = 0
        for i in range(1, n+1):
            res += len(str(i))
        print(res)

    def relay_number(self):
        n = input().strip() # 12
        x = len(n) # 2
        res = 0
        for i in range(1, x):
            res += 9 * i * (10**(i-1))
        
        res += (int(n) - 10**(x-1) + 1) * x
        print(res)

if __name__ == "__main__":
    s = Solution()
    s.relay_number()