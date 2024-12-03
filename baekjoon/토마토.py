from sys import stdin, maxsize
from collections import deque
class Solution:
    def tomato(self):
        M, N, H = map(int, stdin.readline().split())
        box = []
        for _ in range(H):
            arr = []
            for _ in range(N):
                arr.append(list(map(int, stdin.readline().split())))
            box.append(arr)

        directions = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
        Q = deque()
        unripe_count = 0

        for h in range(H):
            for n in range(N):
                for m in range(M):
                    if box[h][n][m] == 1:
                        Q.append((h,n,m,0))
                    elif box[h][n][m] == 0:
                        unripe_count += 1
        
        max_days = 0
        while Q:
            h,n,m,days = Q.popleft()
            max_days = max(days, max_days)
            for dh, dn, dm in directions:
                nh, nn, nm = h + dh, n + dn, m + dm
                if 0<=nh<H and 0<=nn<N and 0<=nm<M and box[nh][nn][nm] == 0:
                    box[nh][nn][nm] = 1
                    Q.append((nh, nn, nm, days+1))
                    unripe_count -= 1
        
        if unripe_count > 0:
            print(-1)
        else:
            print(max_days)

if __name__ == "__main__":
    s = Solution()
    s.tomato()