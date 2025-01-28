import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def stack_(self):
        n = int(input())
        Q = deque()
        for _ in range(n):
            Q.append(int(input()))
        
        nums = [i for i in range(n,0,-1)] # [1~8까지 역순으로 저장]
        res, score = [], []
        prev = 0
        while Q:
            # n이 4일 경우
            n = Q.popleft()
            if n > prev:
                for _ in range(prev, n):
                    # 1부터 4까지 res에 넣기
                    res.append(nums.pop())
                    prev += 1
                    score.append("+")
                # n == 4이므로 res에서 빼기
                res.pop()
                score.append("-")
            # prev보다 n이 작을 경우 res에서 찾아야 함
            else:
                if res and n == res[-1]:
                    res.pop()
                    score.append("-")
                else:
                    print("NO")
                    return
        
        # ['+', '+', '+', '+', '-', '-', '+', '+', '-', '+', '+', '-', '-', '-', '-', '-']
        for k in score:
            print(k)


if __name__ == "__main__":
    s = Solution()
    s.stack_()