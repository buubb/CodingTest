import sys
input = sys.stdin.readline

class Solution:
    def triangle(self):
        while True:
            x,y,z = map(int, input().split())
            if x == 0 and y==0 and z==0:
                return
            arr = sorted([x,y,z])
            if arr[2] < arr[0] + arr[1]:
                if arr[0] == arr[1] == arr[2]:
                    print("Equilateral")
                elif (arr[0] == arr[1] and arr[1] != arr[2]) \
                    or (arr[0] == arr[2] and arr[1] != arr[2]) \
                    or (arr[1] == arr[2] and arr[0] != arr[2]):
                    print("Isosceles")
                else:
                    print("Scalene")
            else:
                print("Invalid")


if __name__ == "__main__":
    s = Solution()
    s.triangle()