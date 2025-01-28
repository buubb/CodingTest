import sys
input = sys.stdin.readline

class Solution:
    def lan_cable(self):
        k, n = map(int, input().split())
        lan = []
        for _ in range(k):
            lan.append(int(input()))
        lo, hi = 1, max(lan)
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            cnt = 0
            for l in lan:
                cnt += l // mid
            
            if cnt >= n:
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1
        print(res)


if __name__ == "__main__":
    s = Solution()
    s.lan_cable()