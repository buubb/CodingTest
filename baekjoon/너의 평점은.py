import sys
input = sys.stdin.readline

class Solution:
    def your_score(self):
        sum = 0
        cnt = 0
        for _ in range(20):
            (subj, cla, grade) = input().split()
            cla = float(cla)
            if grade == "A+":
                sum += cla * 4.5
                cnt += cla
            elif grade == "A0":
                sum += cla * 4.0
                cnt += cla
            elif grade == "B+":
                sum += cla * 3.5
                cnt += cla
            elif grade == "B0":
                sum += cla * 3.0
                cnt += cla
            elif grade == "C+":
                sum += cla * 2.5
                cnt += cla
            elif grade == "C0":
                sum += cla * 2.0
                cnt += cla
            elif grade == "D+":
                sum += cla * 1.5
                cnt += cla
            elif grade == "D0":
                sum += cla * 1.0
                cnt += cla
            elif grade == "F":
                sum += cla * 0
                cnt += cla

        print(round(sum/cnt,6))


if __name__ == "__main__":
    s = Solution()
    s.your_score()