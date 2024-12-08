import sys
input = sys.stdin.readline

class Solution:
    def verify(self):
        max_int = 1000000
        non_demical = [False for i in range(max_int)]
        non_demical[0] = non_demical[1] = True
        nums = []
        for num in range(2,int(max_int**0.5)):
            if non_demical[num]:
                continue
            nums.append(num)
            check = 2
            while check*num < max_int:
                non_demical[check*num] = True
                check += 1

        while True:
            n = int(input())
            if n == 0:
                break
            
            flag = False
            for i in range(2, max_int):
                if not non_demical[i] and not non_demical[n-i]:
                    flag = True
                    print(n,"=",i,"+",n-i)
                    break

            if not flag:
                print("Goldbach's conjecture is wrong.")

            

if __name__ == "__main__":
    s = Solution()
    s.verify()