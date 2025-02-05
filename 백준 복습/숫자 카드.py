import sys, bisect
input = sys.stdin.readline

class Solution:
    def number_card(self):
        N = int(input())
        A = list(map(int, input().split()))
        M = int(input())
        B = list(map(int, input().split()))
        A.sort()
        for b in B:
            idx = bisect.bisect_left(A, b)
            if idx >= N:
                print(0)
                continue
            if A[idx] == b:
                print(1, end=' ')
            else:
                print(0, end=' ')

    def number_cards(self):
        N = int(input())
        A = set(map(int, input().split()))
        M = int(input())
        B = list(map(int, input().split()))
        for k in B:
            print(1 if k in A else 0, end=' ')
            
if __name__ == "__main__":
    s = Solution()
    s.number_cards()