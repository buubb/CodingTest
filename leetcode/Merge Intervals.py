class Solution:
    def merge(self, intervals:list)->list:
        merged = []
        for i in sorted(intervals, key=lambda x:x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += i,
        return merged
    
if __name__ == "__main__":
    s = Solution()
    print(s.merge([[1,3],[2,6],[8,10],[15,18]]))