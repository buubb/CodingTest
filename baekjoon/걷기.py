import sys
input = sys.stdin.readline
class Solution:
    def walk(self):
        x,y,w,s = map(int, input().split())
        dist = 0
        if x >= y:
            if w*2 < s:
                dist += w*2*y
            else:
                dist += s*y
            x-=y
            y-=y
        else:
            if w*2 < s:
                dist += w*2*x
            else:
                dist += s*x
            y-=x
            x-=x
            
        while True:
            if x==1 or y==1:
                dist += w
                break
            if x==0 and y==0:
                break
            if x>0:
                if x%2==0:
                    if w < s:
                        dist += w*x
                    else:
                        dist += s*x
                    x-=x
                else:
                    if w < s:
                        dist += w*(x-1)
                    else:
                        dist += s*(x-1)
                    x-=(x-1)
                  
            elif y>0:
                if y%2==0:
                    if w < s:
                        dist += w*y
                    else:
                        dist += s*y
                    y-=y
                else:
                    if w < s:
                        dist += w*(y-1)
                    else:
                        dist += s*(y-1)
                    y-=(y-1)
 
        print(dist)

if __name__ == "__main__":
    s = Solution()
    s.walk()