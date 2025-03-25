import sys
input = sys.stdin.readline

class Solution:
    def answer(self):
        n = int(input())
        s = list(map(int, input().split()))
        s.sort()
        m = int(input())
        nums = list(map(int, input().split()))
        results = []
        for k in nums:
            left, right = 0, n-1
            find = False
            while left <= right:
                mid = left + (right - left) // 2
                if s[mid] > k:
                    right = mid - 1
                elif s[mid] < k:
                    left = mid + 1
                else:
                    results.append(1)
                    find = True
                    break
            if not find:
                results.append(0)
        print(*results)

            

if __name__ == "__main__":
    s = Solution()
    s.answer()