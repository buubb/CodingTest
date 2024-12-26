import sys
input = sys.stdin.readline

class Solution:
    def slicing_strap_(self):
        K, N = map(int, input().split())
        straps = [int(input()) for _ in range(K)]
        left, right = 1, max(straps)
        res = 0
        while left <= right:
            mid = left + (right-left) // 2
            total = 0
            for strap in straps:
                total += strap // mid
            
            if total >= N:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        print(res)

if __name__ == "__main__":
    s = Solution()
    s.slicing_strap_()