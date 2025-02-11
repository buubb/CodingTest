import sys
input = sys.sdtin.readline

class Solution:
    def diffWaysToCompute(self):
        char = input().rstrip()
        def divide_(char):
            def compute(left, right, op):
                results = []
                for l in left:
                    for r in right:
                        results.append(eval(str(l)+op+str(r)))
                return results
            
            if char.isdigit():
                return int(char)
            results = []
            for idx, value in enumerate(char):
                if value in "-+*":
                    left = divide_(char[:idx])
                    right = divide_(char[idx+1:])

                    results.extend(compute(left, right, value))
                return results
        print(divide_(char))

        
        
if __name__ == "__main__":
    s = Solution()
    s.diffWaysToCompute()