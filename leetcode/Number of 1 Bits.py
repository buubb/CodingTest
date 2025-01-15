class Solution:
    def hammingWeight(self):
        n = int(input(),2)
        print(bin(n).count('1'))

    def hammingWeight2(self):
        n = int(input(),2)
        count = 0
        while n:
            n &= n-1
            count +=1
        print(count)

if __name__ == "__main__":
    s = Solution()
    s.hammingWeight2()
