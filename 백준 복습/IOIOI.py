import sys
input = sys.stdin.readline

class Solution:
    def ioioi(self):
        n = int(input())
        m = int(input())
        S = input().rstrip()
        cnt = 0
        p = 'IO'
        pn = p * n + 'I'
        for i in range(m):
            if pn in S[i:i+2*n+1]:
                cnt += 1
        print(cnt)

    def ioioi2(self):
        n = int(input())
        m = int(input())
        S = input().rstrip()
        res, i, cnt = 0,0,0
        
        while i < m:
            if S[i:i+3] == 'IOI':
                cnt += 1
                i += 2
                if cnt == n:
                    cnt -= 1
                    res += 1
                
            else:
                i += 1
                cnt = 0

        print(res)


if __name__ == "__main__":
    s = Solution()
    s.ioioi2()
