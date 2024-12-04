import sys
input = sys.stdin.readline
class Solution:
    def week(self):
        x, y = map(int, input().split())
        month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
        days = 0
        if x == 1:
            days = y
        else:
            for i in range(1, x):
                days += month[i]
            days += y
        
        res = days % 7
        print(day[res])


if __name__ == "__main__":
    s = Solution()
    s.week()