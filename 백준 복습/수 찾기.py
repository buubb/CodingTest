import sys, bisect
input = sys.stdin.readline

class Solution:
    def find_number(self):
        N = int(input())
        A = list(map(int, input().split()))
        M = int(input())
        arr = list(map(int, input().split()))
        A.sort()
        
        for k in arr:
            lo, hi = 0, N-1
            find = False
            while lo <= hi:
                mid = lo + (hi-lo) // 2
                if A[mid] < k:
                    lo = mid + 1
                elif A[mid] > k:
                    hi = mid - 1
                else:
                    find = True
                    break
            if find:
                print(1)
            else:
                print(0)
    
    def find_num(self):
        N = int(input())
        A = list(map(int, input().split()))
        M = int(input())
        arr = list(map(int, input().split()))
        A.sort()
        for k in arr:
            idx = bisect.bisect_left(A,k)
            if idx >= N:
                print(0)
                continue
            if A[idx] == k:
                print(1)
            else:
                print(0)

if __name__ == "__main__":
    s = Solution()
    s.find_num()