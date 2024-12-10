import sys
input = sys.stdin.readline

class Solution:
    def number(self):
        N = int(input())
        A = [i for i in map(int, input().split())]
        M = int(input())
        B = [i for i in map(int, input().split())]
        A = sorted(A)
        
        for i in range(M):
            isT = False
            low = 0
            high = len(A)-1
            while (low <= high):
                mid = (low+high) // 2
                if A[mid] > B[i]:
                    high = mid-1    
                elif A[mid] < B[i]:
                    low = mid + 1 
                else:
                    print(1)
                    isT = True
                    break
            if not isT:
                print(0)
            
        
            
            

if __name__ == "__main__":
    s = Solution()
    s.number()