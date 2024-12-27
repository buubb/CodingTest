import sys, bisect
input = sys.stdin.readline

class Solution:
    def memorize_(self):
        T = int(input())
        for _ in range(T):
            N = int(input())
            n1 = list(map(int, input().split()))
            M = int(input())
            m1 = list(map(int, input().split()))
            n1.sort()
            for m in m1:
                idx = bisect.bisect_left(n1, m)
                if len(n1) > idx and n1[idx] == m:
                    print(1)
                else:
                    print(0)

if __name__ == "__main__":
    s = Solution()
    s.memorize_()