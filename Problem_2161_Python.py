# Partition Array According to Given Pivot, solved Mar 3 2025
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        i, j = 0, 0
        ret_nums = []
        for val in nums:
            if val < pivot:
                ret_nums.insert(i, val)
                i += 1
                j += 1
            elif val == pivot:
                ret_nums.insert(j, val)
                j += 1
            else:
                ret_nums.append(val)
        return ret_nums
