import sys
input = sys.stdin.readline

class Solution:
    def buy_cards(self):
        n = int(input())
        cards = [0] + list(map(int, input().split()))
        
        print(cards)
       

if __name__ == "__main__":
    s = Solution()
    s.buy_cards()