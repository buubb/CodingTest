import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def meeting_room(self):
        N = int(input())
        timetable = deque()
        for _ in range(N):
            x,y = map(int, input().split())
            timetable.append((x,y))
        res = []
        temp = -1
        for (x,y) in sorted(timetable, key= lambda x:(x[1], x[0])):
            if x >= temp:
                res.append((x,y))
                temp = y
        print(len(res))

if __name__ == "__main__":
    s = Solution()
    s.meeting_room()