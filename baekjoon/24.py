from sys import stdin

class Solution:
    def CTUtime(self):
        now = list(map(int, stdin.readline().split(":")))
        start = list(map(int, stdin.readline().split(":")))
        
        res = [0] * 3
        carry = 0

        # 초 계산
        res[2] = start[2] - now[2]
        if res[2] >= 0:
            carry = 0
        else:
            res[2] += 60
            carry = 1
        
        # 분 계산
        res[1] = start[1] - now[1] - carry
        if res[1] >= 0:
            carry = 0
        else:
            res[1] += 60
            carry = 1
        
        # 시 계산
        res[0] = start[0] - now[0] - carry
        if res[0] < 0:
            res[0] += 24


        return f'{str(res[0]).zfill(2)}:{str(res[1]).zfill(2)}:{str(res[2]).zfill(2)}'
        # N = len(res)
        # for i in range(N-1):
        #         if start[N-1-i] < now[N-1-i]:
        #             start[N-1-i] += 60
        #             res[N-1-i] = str(start[N-1-i] - now[N-1-i]).zfill(2)
        #             now[N-2-i] += 1
        #         else:
        #             res[N-1-i] = str(start[N-1-i] - now[N-1-i]).zfill(2)
        # if 0 <= now[0] <= start[0]:
        #     res[0] = str(start[0] - now[0]).zfill(2)
        # elif start[0] < now[0] <= 23:
        #     res[0] = str(24 - (now[0]-start[0])).zfill(2)

        # return ':'.join(res)


if __name__ == "__main__":
    s = Solution()
    print(s.CTUtime())
