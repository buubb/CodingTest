import sys
input = sys.stdin.readline

class Solution:
    def demical(self):
        N = int(input())
        nums = list(map(int, input().split()))

        res = 0
        for i in nums:
            if i == 1:
                continue
            is_demical = True
            for j in range(2,i):
                if i % j == 0:
                    is_demical = False
                    break
            if is_demical:
                res += 1

        print(res)
                
                

if __name__ == "__main__":
    s = Solution()
    s.demical()