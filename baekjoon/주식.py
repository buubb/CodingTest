import sys
input = sys.stdin.readline

class Solution:
    def max_profit(self):
        T = int(input())
        for _ in range(T):
            N = int(input())
            graph = list(map(int, input().split()))
            sell = 0
            max_price = 0

            # 뒤에서부터 역순으로 순회
            for price in reversed(graph):
                if price > max_price:
                    max_price = price
                else:
                    sell += max_price - price

            print(sell)


if __name__ == "__main__":
    s = Solution()
    s.max_profit()