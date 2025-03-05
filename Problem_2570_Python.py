# Merge Two 2D Arrays by Summing Values, solved Mar 2 2025
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        x = defaultdict(int)

        for i in nums1:
            x[i[0]] += i[1]
        for i in nums2:
            x[i[0]] += i[1]
        return [[i,x[i]] for i in sorted(x)]
