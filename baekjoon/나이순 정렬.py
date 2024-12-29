import sys
input = sys.stdin.readline

class Solution:
    def sort_age(self):
        N = int(input())
        arr = []
        for i in range(N):
            a, name = input().split()
            arr.append((int(a), name, i))
        arr.sort(key=lambda x : (x[0], x[2]))

        for idx in range(N):
            print(arr[idx][0], arr[idx][1])

if __name__ == "__main__":
    s = Solution()
    s.sort_age()