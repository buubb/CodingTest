import sys, bisect
input = sys.stdin.readline

class Solution:
    def guitar_lesson(self):
        N, M = map(int, input().split())
        lesson = list(map(int, input().split()))
        left, right = max(lesson), sum(lesson)
        res = 0
        while left <= right:
            mid = left + (right-left) // 2
            total = 0
            cnt = 1
            for l in lesson:
                if total + l > mid:
                    cnt += 1
                    total = 0
                total += l
                
            if cnt > M:
                left = mid + 1
            elif cnt <= M:
                res = mid
                right = mid - 1
        print(res)


if __name__ == "__main__":
    s = Solution()
    s.guitar_lesson()