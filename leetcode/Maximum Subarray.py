import sys
input = sys.stdin.readline

class Solution:
    def max_subarr(self):
        arr = list(map(int, input().split()))
        for i in range(1, len(arr)):
            arr[i] += arr[i-1] if arr[i-1] > 0 else 0
            print(arr)
        print(max(arr))
    
    # 카데인 알고리즘즘
    def max_subar(self):
        arr = list(map(int, input().split()))
        best_sum = float('-inf')
        current_sum = 0
        for a in arr:
            current_sum = max(a, current_sum + a)
            best_sum = max(best_sum, current_sum)
        print(best_sum)

if __name__ == "__main__":
    s = Solution()
    s.max_subar()