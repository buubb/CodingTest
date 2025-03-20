import sys
input = sys.stdin.readline

class Solution:
    def answer(self):
        n = int(input())
        company = set()
        for _ in range(n):
            name, log = input().split()
            if log == "enter":
                company.add(name)
            elif log == "leave":
                company.remove(name)
        for na in sorted(company, reverse=True):
            print(na)

if __name__ == "__main__":
    s = Solution()
    s.answer()