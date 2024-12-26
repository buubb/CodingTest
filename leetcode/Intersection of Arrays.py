import bisect
class Solution:
    def intersection(self, nums1:list, nums2:list) -> list:
        res = set()
        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2:
                    res.add(n1)
        print(list(res))
    
    def intersection_2(self, nums1:list, nums2:list) -> list:
        res = set()
        nums2.sort()
        for n1 in nums1:
            idx = bisect.bisect_left(nums2, n1)
            if len(nums2) > 0 and len(nums2) > idx and n1 == nums2[idx]:
                res.add(n1)
        print(list(res))

    def intersection_3(self, nums1:list, nums2:list) -> list:
        res = set()
        nums1.sort()
        nums2.sort()
        i=j=0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                res.add(nums1[i])
                i+=1
                j+=1
        print(list(res))

if __name__ == "__main__":
    s = Solution()
    s.intersection_3([1,2,2,1],[2,2])