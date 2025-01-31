import sys
input = sys.stdin.readline

class Solution:
    def triangle(self):
        n = int(input())
        arr = []
        for _ in range(n):
            arr.append(list(map(int, input().split())))
        for i in range(1, n):
            for j in range(i+1):
                if j == 0:
                    arr[i][j] += arr[i-1][j]
                elif j == i:
                    arr[i][j] += arr[i-1][j-1]
                else:
                    arr[i][j] = max(arr[i-1][j]+arr[i][j], arr[i-1][j-1]+arr[i][j])
        print(max(arr[n-1]))
        
if __name__ == "__main__":
    s = Solution()
    s.triangle()