import sys
input = sys.stdin.readline

class Solution:
    def answer(self):
        l, c = map(int, input().split())
        string = list(input().split())

        def backtracking(arr, a_cnt, b_cnt):
            if len(arr) == l and a_cnt >= 1 and b_cnt >= 2:
                print(''.join(arr))
                return
            
            for k in sorted(string):
                if k not in arr:
                    if not arr:
                        arr.append(k)
                        if k in ('a','e','i','o','u'):
                            a_cnt += 1
                        else:
                            b_cnt += 1
                        backtracking(arr, a_cnt, b_cnt)
                        if k in ('a','e','i','o','u'):
                            a_cnt -= 1
                        else:
                            b_cnt -= 1
                        arr.pop()
                    elif arr and arr[-1] < k:
                        arr.append(k)
                        if k in ('a','e','i','o','u'):
                            a_cnt += 1
                        else:
                            b_cnt += 1
                        backtracking(arr, a_cnt, b_cnt)
                        if k in ('a','e','i','o','u'):
                            a_cnt -= 1
                        else:
                            b_cnt -= 1
                        arr.pop()
        backtracking([], 0, 0)

if __name__ == "__main__":
    s = Solution()
    s.answer()