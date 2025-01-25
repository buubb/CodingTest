import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def sliding_window(self, nums:list, k:int):
        r = []
        for i in range(len(nums)-k+1):
            r.append(max(nums[i:i+k]))
        print(r)
    
    def sliding_window2(self, nums:list, k:int):
        r = []
        window = deque()
        current_max = float('-inf')
        for i, v in enumerate(nums):
            window.append(v)
            if i < k-1:
                continue

            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max:
                current_max = v

            r.append(current_max)
        
            if current_max == window.popleft():
                current_max = float('-inf')
        print(r)

if __name__ == "__main__":
    s = Solution()
    nums = list(map(int, input().split()))
    k = int(input())
    s.sliding_window2(nums, k)