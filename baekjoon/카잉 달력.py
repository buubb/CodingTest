import sys
input = sys.stdin.readline

class Solution:
    def days(self):
        T = int(input())
        for _ in range(T):
            M,N,x,y = map(int, input().split())
            year = x
            max_year = M*N // self.gcb(M,N)
            isValid= False
            while year <= max_year:
                if (year-x)%M==0 and (year-y)%N==0:
                    isValid = True
                    break
                year+=M
            if isValid:
                print(year)
            else:
                print(-1)
    
    def gcb(self,a,b):
        while b!=0:
            a,b = b, a%b
        return a
if __name__ == "__main__":
    s = Solution()
    s.days()