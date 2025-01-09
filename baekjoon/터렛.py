import sys, math
input = sys.stdin.readline

class Solution:
    def answer(self):
        T = int(input())
        for _ in range(T):
            x1,y1,r1,x2,y2,r2 = map(int, input().split())
            dist = math.sqrt((x1-x2)**2 + (y1-y2)**2) # 두 접점의 거리
            if dist ==0 and r1==r2: # 두 원이 동심원이고 반지름이 같을 때
                print(-1)
            elif abs(r1-r2) == dist or r1+r2==dist: # 외접 or 내접일 때
                print(1)
            elif abs(r1-r2) < dist < r1+r2: # 두 원이 서로 다른 두 점에서 만날 때때
                print(2)
            else: # 그 외
                print(0)

if __name__ == "__main__":
    s = Solution()
    s.answer()