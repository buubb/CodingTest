import sys
input = sys.stdin.readline

class Solution:
    res: int = 0
    def sum_three_number(self):
        N = int(input())
        arr = [int(input()) for _ in range(N)]
        arr.sort()

        arr_sum = set()
        for x in arr:
            for y in arr:
                arr_sum.add(x+y)
    
        def check():
            global res
            for idx in range(N-1, -1, -1):
                for j in range(idx+1):
                    k = arr[idx] - arr[j]
                    if k in arr_sum:
                        self.res = arr[idx]
                        return
        check()
        print(self.res)


if __name__ == "__main__":
    s = Solution()
    s.sum_three_number()