#Minimum Operations to Exceed Threshold Value II, solved Feb 12 2025
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0
        while nums[0] < k: 
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, x * 2 + y)
            count += 1
        return count
