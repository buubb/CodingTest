class Solution:
    def zero_one_knapsack(self,cargo:list):
        capacity = 15 # 최대 용량
        pack = [] # 가치 저장장
        for i in range(len(cargo)+1):
            pack.append([])
            for c in range(capacity+1):
                if i == 0 or c == 0:
                    pack[i].append(0)
                elif cargo[i-1][1] <= c: # cargo[i-1][1]은 kg
                    pack[i].append(max(
                        cargo[i-1][0] + pack[i-1][c - cargo[i-1][1]],
                        pack[i-1][c]
                    ))
                else:
                    pack[i].append(pack[i-1][c])
        print(pack[-1][-1])

if __name__ == "__main__":
    s = Solution()
    cargo = [ # (가치, 용량)
        (4, 12),
        (2, 1),
        (10, 4),
        (1, 1),
        (2, 2)
    ]
    s.zero_one_knapsack(cargo)