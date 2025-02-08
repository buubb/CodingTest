import sys
input = sys.stdin.readline

class Solution:
    def sum_three(self):
        N = int(input())
        nums = [int(input()) for _ in range(N)]
        nums.sort()

        sum_arr = set()
        for i in nums:
            for j in nums:
                sum_arr.add(i+j)
        
        def check():
            for i in range(N-1, -1, -1):
                for j in range(i+1):
                    k = nums[i] - nums[j]
                    if k in sum_arr:
                        return nums[i]
        
        print(check())

if __name__ == "__main__":
    s = Solution()
    s.sum_three()