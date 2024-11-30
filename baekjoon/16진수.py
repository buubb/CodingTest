from sys import stdin
class Solution:
    def sixteen(self):
        N = stdin.readline()
        num_int16 = list(N.zfill(7))
        num = {
            "A": 10,
            "B": 11,
            "C": 12,
            "D": 13,
            "E": 14,
            "F": 15
        }
        res = 0
        for i in range(len(num_int16)-1):
            try:
                res += 16**(len(num_int16)-2-i) * int(num_int16[i])
            except:
                res += 16**(len(num_int16)-2-i) * num[num_int16[i]]
        print(res)
if __name__ == "__main__":
    s = Solution()
    s.sixteen()