import sys
input = sys.stdin.readline

class Solution:
    def money(self):
        price = int(input())
        m = 1000 - price
        arr = [500,100,50,10,5,1]
        cnt , i = 0, 0
        while m != 0 and i < len(arr):
            if m // arr[i] > 0:
                cnt += m // arr[i]
                m %= arr[i]
            i += 1
        
        print(cnt)


if __name__ == "__main__":
    s = Solution()
    s.money()