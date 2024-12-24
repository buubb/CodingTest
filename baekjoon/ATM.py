import sys
input = sys.stdin.readline

class Solution:
    def atm(self):
        N = int(input())
        line = list(map(int, input().split()))
        line.sort()
        
        for i in range(1,N):
            line[i] = line[i] + line[i-1]
        
        print(sum(line))

if __name__ == "__main__":
    s = Solution()
    s.atm()