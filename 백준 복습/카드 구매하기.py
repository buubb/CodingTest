import sys
input = sys.stdin.readline

class Solution:
    def buy_cards(self):
        n = int(input())
        cards = [0] + list(map(int, input().split()))
        dp = [0] * (n+1)
        for i in range(1, len(cards)):
            for j in range(1, i+1):
                dp[i] = max(dp[i], dp[i-j] + cards[j])
                print(dp)
        print(dp[n])

    def buy_card(self):
        capacity = int(input())
        arr = list(map(int, input().split()))
        cargo = [] # (개수, 가치)
        for i, v in enumerate(arr):
            cargo.append((i+1, v))
        pack = []
        for i in range(len(cargo) + 1):
            pack.append([])
            for c in range(capacity+1):
                if i == 0 or c == 0:
                    pack[i].append(0)
                elif cargo[i-1][0] <= c:
                    pack[i].append(
                        max(
                            cargo[i-1][1] + pack[i][c-cargo[i-1][0]],
                            pack[i-1][c]
                        )
                    )
                else:
                    pack[i].append(pack[i-1][c])
                # print(pack)
        print(pack[-1][-1])



if __name__ == "__main__":
    s = Solution()
    s.buy_card()