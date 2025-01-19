import sys
input = sys.stdin.readline

class Solution:
    def ioioi(self):
        N = int(input())
        M = int(input()) # S의 길이
        S = input()
        
        p = ''
        for _ in range(N):
            p += 'IO'
        p += 'I'
        cnt = 0
        for i in range(M):
            if p == S[i:i+2*N+1]:
                cnt += 1
        
        print(cnt)

    def ioioi2(self):
        N = int(input())
        M = int(input()) # S의 길이
        S = input()
        answer, i, cnt = 0,0,0

        while i < (M-1):
            if S[i:i+3] == 'IOI':
                i += 2
                cnt += 1
                if cnt == N:
                    answer += 1
                    cnt -= 1
            else:
                i += 1
                cnt = 0
        
        print(answer)

if __name__ == "__main__":
    s = Solution()
    s.ioioi2()