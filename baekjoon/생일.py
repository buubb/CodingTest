import sys
class Solution:
    def birth(self):
        N = int(sys.stdin.readline())
        arr = []
        for _ in range(N):
            name, d, m, y = sys.stdin.readline().split()
            arr.append([name, int(d), int(m), int(y)])
        sort_list = sorted(arr, key=(lambda x: (-x[3], -x[2], -x[1])))
        print(sort_list[0][0])
        print(sort_list[N-1][0])

if __name__ == "__main__":
    s = Solution()
    s.birth()