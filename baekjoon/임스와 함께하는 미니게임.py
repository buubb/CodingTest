import sys

input = sys.stdin.readline

class Solution:
    def answer(self):
        N, gameType = input().split()

        mini_games = { # 임스 제외
            'Y':2-1,
            'F':3-1,
            'O':4-1
        }

        users = set()
        for _ in range(int(N)):
            users.add(input().rstrip())
        
        print(len(users) // mini_games[gameType])


if __name__ == "__main__":
    s = Solution()
    s.answer()